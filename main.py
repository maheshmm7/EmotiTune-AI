import cv2
import numpy as np
import time
import spotipy
import random
from spotipy.oauth2 import SpotifyOAuth
from keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from dotenv import load_dotenv
import os
import webbrowser

# Load API keys from .env file
load_dotenv("way.env")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Authenticate with Spotify (Free user mode)
try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="user-read-private"
    ))
except Exception as e:
    print(f"[ERROR] Spotify authentication failed: {e}")
    exit()

# Load face detection model
if not os.path.exists('./haarcascade_frontalface_default.xml'):
    print("[ERROR] Face detection model not found!")
    exit()

face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# Load emotion detection model
if not os.path.exists('./Emotion_Detection.h5'):
    print("[ERROR] Emotion detection model not found!")
    exit()

classifier = load_model('./Emotion_Detection.h5')

# Define class labels
class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Load playlists from text file
def load_playlists(filename="playlists.txt"):
    playlists = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("=")
                if len(parts) == 2:
                    emotion, playlist_list = parts
                    playlists[emotion.strip()] = [p.strip() for p in playlist_list.split(",")]
    except FileNotFoundError:
        print("[ERROR] playlists.txt not found. Using default playlists.")
    return playlists

emotion_playlists = load_playlists()

# Store last opened playlist to prevent re-opening the same one
last_opened_playlist = None

# Function to open a Spotify playlist in a web browser
def open_spotify_playlist(emotion):
    global last_opened_playlist
    
    playlist_options = emotion_playlists.get(emotion, [])
    if not playlist_options:
        print(f"[WARNING] No playlists assigned for emotion: {emotion}")
        return

    # Keep trying until a valid playlist is found
    for _ in range(len(playlist_options)):
        playlist_name = random.choice(playlist_options)

        # Avoid re-opening the same playlist
        if last_opened_playlist == playlist_name:
            continue  

        try:
            results = sp.search(q=playlist_name, type='playlist', limit=1)
            playlists = results.get('playlists', {}).get('items', [])

            if not playlists:
                print(f"[WARNING] No Spotify playlists found for: {playlist_name}")
                continue  # Try another playlist

            playlist_url = playlists[0]['external_urls']['spotify']
            webbrowser.open(playlist_url)
            print(f"[INFO] Opening Spotify playlist in browser: {playlist_name}")

            last_opened_playlist = playlist_name  # Store last opened playlist
            return  # Exit function after successfully opening a playlist

        except Exception as e:
            print(f"[ERROR] Failed to search for playlist: {e}")

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Camera not accessible.")
    exit()

current_emotion = None
emotion_start_time = None
emotion_check_duration = 5  # Time in seconds to confirm an emotion

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    detected_emotion = None

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        if np.sum(roi_gray) != 0:
            roi = roi_gray.astype('float32') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            # Get model predictions
            preds = classifier.predict(roi)[0]
            confidence = np.max(preds)
            label = class_labels[np.argmax(preds)]

            # Display detected emotion
            label_position = (x, y - 10)
            cv2.putText(frame, f"{label} ({confidence:.2f})", label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Open Spotify only if confidence is high
            if confidence > 0.6 and label in emotion_playlists:
                detected_emotion = label

    if detected_emotion:
        if detected_emotion == current_emotion:
            if emotion_start_time and time.time() - emotion_start_time >= emotion_check_duration:
                open_spotify_playlist(current_emotion)
                emotion_start_time = None
        else:
            current_emotion = detected_emotion
            emotion_start_time = time.time()
            last_opened_playlist = None  # Reset last opened playlist when emotion changes

    # Display message if no face is detected
    if len(faces) == 0:
        cv2.putText(frame, 'No Face Detected', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Emotion-Based Music Player', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
