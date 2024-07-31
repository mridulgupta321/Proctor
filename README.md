### Important

Download

1. **yolov3-tiny.weights**

   Download from [yolov3-tiny.weights GitHub link](https://github.com/smarthomefans/darknet-test/blob/master/yolov3-tiny.weights) and save the file in:  "object_detection_model\weights\yolov3-tiny.weights"

2. **shape_predictor_68_face_landmarks.dat**

   Download from [shape_predictor_68_face_landmarks.dat GitHub link](https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat) and save it in:  "shape_predictor_model\shape_predictor_68_face_landmarks.dat"

### Prerequisites
To run the programs in this repo, do the following:
- create a virtual environment using the command:
  - `python -m venv venv`
- activate the virtual environment
  - `cd ./venv/Scripts/activate` (windows users)
  - `source ./venv/bin/activate` (mac and linux users)
- install the requirements
  - `pip install --upgrade pip` (to upgrade pip)
  - `pip install -r requirements.txt`

Once the requirements have been installed, the programs will run successfully.
To run the software use: 
```python 
python server.py
```

## Key Features and Functions 
1. Face Detection using Dlib
2. Eye Gaze Detection
3. Mouth Tracking
4. Blink Detection
5. Head Pose Estimation
6. Object Detection using Yolo
7. Audio Detection

## Technology Used 
1. Python
2. Comuter Vision 
3. OpenCV
4. Dlib
5. Pyaudio
6. Winsound
7. Web Skills (HTML, CSS, JS)
8. Flask Server
9. SQL Database
