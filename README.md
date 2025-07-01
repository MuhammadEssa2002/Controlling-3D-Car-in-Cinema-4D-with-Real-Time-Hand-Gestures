# Controlling-3D-Car-in-Cinema-4D-with-Real-Time-Hand-Gestures

A simple Python application that uses OpenCV and MediaPipe to track your hand via webcam, draw landmarks, measure the distance between thumb and index‐finger tips, display it on the video feed (as an approximate real‐world value), and write the raw values to text files (`api.txt` and `api2.txt`).

---

## Features

- Detects hand landmarks in real time  
- Draws circles on thumb tip (landmark 4) and index‐finger tip (landmark 8)  
- Draws a line between those two points  
- Converts pixel distance into an approximate real‐world distance  
- Displays current FPS on the video window  
- Logs normalized x‐coordinate of wrist landmark (landmark 0) to `api.txt`  
- Logs measured distance to `api2.txt`  

---

## Requirements

- Python 3.7+  
- [OpenCV](https://pypi.org/project/opencv-python/)  
- [MediaPipe](https://pypi.org/project/mediapipe/)  

---

## Installation

1. **Clone this repository**  
   ```bash
   git clone https://github.com/your-username/hand-distance-tracker.git
   cd hand-distance-tracker
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate      # on Linux/Mac
venv\Scripts\activate         # on Windows
Install dependencies

bash
Copy
Edit
pip install opencv-python mediapipe
Usage
Run the script

bash
Copy
Edit
python hand_distance.py
(Assuming you named the file hand_distance.py.)

Interact

A window titled “Image” will open showing your webcam feed.

Place your hand in frame; you’ll see white circles at the thumb and index‐finger tips and a connecting line.

The on‐screen label “Current FPS” shows the frame rate.

The script writes:

Wrist x‐coordinate (normalized) → api.txt

Distance between thumb & index (scaled) → api2.txt

Exit

Press Ctrl+C in the terminal or close the video window.

Configuration
You can tweak the following parameters at the top of the script:

python
Copy
Edit
wCam, hCam = 400, 225    # Camera resolution (width × height)
min_detection_confidence = 0.7  # MediaPipe hand detection threshold
scale_factor = 60 / 355  # Scale pixel distance → “real” units
File Structure
bash
Copy
Edit
.
├── hand_distance.py   # Main script
├── api.txt            # Wrist x-coordinate (overwritten each frame)
├── api2.txt           # Measured distance (overwritten each frame)
└── README.md          # This document
Troubleshooting
Webcam not found:
Make sure no other program is using the webcam and that your device index (cv2.VideoCapture(0)) is correct.

Low FPS:

Reduce wCam/hCam values.

Close other CPU-intensive applications.

Landmarks not detected:

Ensure your hand is well‐lit and fully in the camera frame.

Increase min_detection_confidence if you get too many false positives, or decrease it if you get no detections.

License
This project is licensed under the MIT License. See LICENSE for details.

Acknowledgements
MediaPipe Hands

OpenCV
