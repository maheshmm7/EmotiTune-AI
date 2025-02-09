# 🎭 Emotion-Based Media Player 🎵  

## 📌 About  
The **Emotion-Based Media Player** is an AI-powered application that detects facial emotions in real-time and plays music based on the user's mood. Using deep learning for **emotion recognition** and **computer vision** for face detection, the system categorizes emotions into **Happy, Neutral, Sad, Angry, and Surprise** and selects music accordingly.  

## 🚀 Features  
✅ **Real-time Facial Emotion Detection** using OpenCV & Keras  
✅ **AI-Driven Music Selection** based on facial expressions  
✅ **Spotify Integration** (Opens relevant playlists)  
✅ **Automatic Playlist Handling** for different emotions  
✅ **Lightweight & User-Friendly Interface**  

---

## 🛠 Installation  

### **📌 Prerequisites**  
Ensure you have the following installed:  
- **Python 3.7 - 3.9** (Not compatible with Python 3.10+)  
- **TensorFlow & Keras** (Deep learning models)  
- **OpenCV** (Computer vision for face detection)  
- **Spotipy** (Spotify API integration)  
- **NumPy** (Array processing)  
- **pygame** (For local media playback)  

### **📌 Setup**  
#### **1️⃣ Clone the repository**  
```bash  
git clone https://github.com/your-username/emotion-based-media-player.git  
cd emotion-based-media-player  
```  
#### **2️⃣ Set up a Virtual Environment (If Python is not 3.7 - 3.9)**  
**For Windows:**  
```bash  
python -m venv env  
env\Scripts\activate  
```  
**For macOS/Linux:**  
```bash  
python3 -m venv env  
source env/bin/activate  
```  
#### **3️⃣ Install dependencies**  
```bash  
pip install -r requirements.txt  
```  
#### **4️⃣ Set up your Spotify API Credentials**  
   - Create a `.env` file and add your credentials:  
     ```ini  
     SPOTIFY_CLIENT_ID=your_client_id  
     SPOTIFY_CLIENT_SECRET=your_client_secret  
     SPOTIFY_REDIRECT_URI=http://localhost:8888/callback  
     ```  
   - You can obtain these credentials from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).  

#### **5️⃣ Ensure the required files are in place**  
   - `haarcascade_frontalface_default.xml` (Face detection model)  
   - `Emotion_Detection.h5` (Trained deep learning model)  
   - `playlists.txt` (Contains playlists for different emotions)  

---

## 🎮 Usage  
Run the following command to start the application:  
```bash  
python main.py  
```  
The application will:  
1️⃣ **Open the webcam feed** and detect faces.  
2️⃣ **Analyze facial expressions** and classify the detected emotion.  
3️⃣ **Play music** from either local files or Spotify playlists based on the emotion.  

---

## 🎵 Controls  
- **Press 'q'** → Exit the program  
- **Press 'p'** → Pause music  
- **Press 'r'** → Resume music  

---

## 📂 Directory Structure  
```  
📂 emotion-based-media-player  
├── 📜 main.py                 # Main application script  
├── 📜 requirements.txt         # Required dependencies  
├── 📜 way.env                  # Spotify API credentials (not included in repo)  
├── 📜 playlists.txt            # Emotion-based playlist mappings  
├── 📜 haarcascade_frontalface_default.xml  # Face detection model  
├── 📜 Emotion_Detection.h5     # Trained emotion detection model    
```  

---

## 📝 Sample `playlists.txt`  
This file maps emotions to playlists:  
```ini  
Happy = Happy Hits, Party Time, Feel Good Vibes  
Neutral = Chill Vibes, Relaxing Music, Study Playlist  
Sad = Sad Songs, Melancholy Mix, Deep Feels  
Angry = Rock Anthems, Metal Hits, Workout Motivation  
Surprise = Trending Now, Discover Weekly, Fresh Finds  
```  

---

## 🤝 Contributing  
Feel free to submit **issues**, suggest **improvements**, or create a **pull request**.  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 📬 Contact  
For any questions or feedback, reach out via [GitHub Issues](https://github.com/your-username/emotion-based-media-player/issues).