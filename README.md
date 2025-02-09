# 🎵 Emotion-Based Media Player Using AI 🎭  

## About  
**Emotion-Based Media Player** is an AI-powered application that detects facial emotions in real time and plays music based on the user's mood. Using deep learning for emotion recognition and computer vision for face detection, the system categorizes emotions into **Happy, Neutral, and Sad** and selects songs accordingly.  

## Key Features  
✔️ Real-time facial emotion detection using OpenCV and Keras  
✔️ AI-driven music selection based on mood  
✔️ Dynamic playlist handling for different emotions  
✔️ Simple and interactive interface  

## Installation  
### Prerequisites  
Ensure you have the following installed:  
- Python 3.7+  but Python < 3.10
- TensorFlow & Keras  
- OpenCV  
- NumPy  
- pygame  

### Setup  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/emotion-based-media-player.git  
   cd emotion-based-media-player  
   ```  
2. Install required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Ensure the required files are in place:  
   - `haarcascade_frontalface_default.xml` (Face detection model)  
   - `Emotion_Detection.h5` (Trained emotion classification model)  
   - `playlist_happy`, `playlist_neutral`, and `playlist_sad` directories containing songs  

## Usage  
Run the following command to start the media player:  
```bash  
python test.py  
```  
The application will:  
1. Open a webcam feed and detect faces.  
2. Analyze facial expressions and classify emotions.  
3. Play music from the corresponding playlist based on detected emotion.  

## Controls  
- **Press 'q'** to exit the program.  
- **Press 'p'** to pause music.  
- **Press 'r'** to resume music.  

## Directory Structure  
```  
📂 emotion-based-media-player  
├── 📜 test.py  
├── 📜 requirements.txt  
├── 📂 playlist_happy  
├── 📂 playlist_neutral  
├── 📂 playlist_sad  
├── 📜 haarcascade_frontalface_default.xml  
├── 📜 Emotion_Detection.h5  
```  

## Contributing  
Feel free to submit issues or contribute by creating a pull request.  

## License  
This project is licensed under the MIT License.  

## Contact  
For any inquiries or feedback, reach out via [GitHub Issues](https://github.com/your-username/emotion-based-media-player/issues).

