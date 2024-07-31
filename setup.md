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
