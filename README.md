## 🚦 Traffic Analyser and Perception-Based Detection

## 📘 Project Description
An AI-powered smart traffic control system that analyzes real-time or uploaded traffic images to dynamically decide which road should get the green light. The system uses computer vision and YOLO object detection to manage traffic flow efficiently.

## 🔧 Features
- Upload image to analyze traffic
- Detects traffic density using YOLO
- Determines which lane gets the green light
- Dynamically updates UI and background colors
- Visual feedback through traffic light icons
- Audio beep when green light is assigned
- Real-time chart for traffic patterns (Chart.js)
- Live camera feed support (WebRTC)

## 🚀 Tech Stack
- Python
- Flask
- HTML, CSS, JavaScript
- YOLOv3 (or YOLOv8 if used)
- OpenCV
- Chart.js
- WebRTC (for live camera feed)

## 📂 How to Run the Project
1. Clone the repository
2. Install the dependencies:
   pip install -r requirements.txt

3. Download YOLO weights and config files:
   - yolov3.weights
   - yolov3.cfg
   - coco.names
   Place them in the `yolo-cfg/` directory.

4. Run the Flask app:
   ```bash
   python app.py

6. Open the browser and go to:
   http://127.0.0.1:5000

## 🎥 Demo
https://github.com/user-attachments/assets/834a8892-9aef-4ff1-bd5b-3c49646c497f

