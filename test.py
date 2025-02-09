# USAGE: python emotion_based_media_player.py

from keras.models import load_model
from time import sleep, time
from tensorflow.keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Load the pre-trained model
face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
classifier = load_model('./Emotion_Detection.h5')

# Define class labels
class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Define emotion-based playlists (only Happy, Neutral, and Sad)
emotion_playlists = {
    'Happy': 'playlist_happy',
    'Neutral': 'playlist_neutral',
    'Sad': 'playlist_sad'
}

# Function to play music based on emotion
def play_music(emotion):
    playlist_dir = emotion_playlists.get(emotion)
    if playlist_dir and os.path.exists(playlist_dir):
        songs = os.listdir(playlist_dir)
        if songs:
            song = os.path.join(playlist_dir, np.random.choice(songs))
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            print(f"Playing {emotion} song: {song}")
        else:
            print(f"No songs found in {playlist_dir}")
    else:
        print(f"Playlist directory for {emotion} does not exist")

# Initialize video capture
cap = cv2.VideoCapture(0)

current_emotion = None
emotion_start_time = None
emotion_check_duration = 5  # Duration in seconds to check for continuous emotion

while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            # Make a prediction on the ROI, then lookup the class
            preds = classifier.predict(roi)[0]
            label = class_labels[preds.argmax()]
            label_position = (x, y)
            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

            if label in emotion_playlists:
                if label == current_emotion:
                    if emotion_start_time is not None and time() - emotion_start_time >= emotion_check_duration:
                        play_music(current_emotion)
                        emotion_start_time = None
                else:
                    current_emotion = label
                    emotion_start_time = time()
        else:
            cv2.putText(frame, 'No Face Found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow('Emotion Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()