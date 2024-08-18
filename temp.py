import cv2
import threading
import time
import multiprocessing
from facial_detections import detectFace
from eye_tracker import gazeDetection
from blink_detection import isBlinking
from head_pose_estimation import head_pose_detection
from mouth_tracking import mouthTrack
from object_detection import detectObject
from audio_detection import process_audio_and_text

# Initialize variables
frame = None
frame_rate = 20000  # Target frame rate
prev_frame_time = 0

def video_capture_thread(cap):
    global frame
    while True:
        ret, temp_frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(temp_frame, (320, 240))  # Resize frame to reduce processing load

def processing_thread():
    global frame, prev_frame_time
    while True:
        if frame is not None:
            current_time = time.time()
            if current_time - prev_frame_time >= 1./frame_rate:
                prev_frame_time = current_time
                try:
                    # FUNCTION 1
                    faceCount, faces = detectFace(frame)
                    print(f"Face Count: {faceCount}")

                    # FUNCTION 2
                    eyeStatus = gazeDetection(faces, frame)
                    print(f"Eye Status: {eyeStatus}")

                    # FUNCTION 3
                    blinkStatus = isBlinking(faces, frame)
                    print(f"Blink Status: {blinkStatus[2]}")

                    # FUNCTION 4
                    head_pose_detection(faces, frame)

                    # FUNCTION 5
                    print(f"Mouth Tracking: {mouthTrack(faces, frame)}")

                    # FUNCTION 6
                    print(f"Object Detection: {detectObject(frame)}")

                except Exception as e:
                    print(f"Error during processing: {e}")

                cv2.imshow('Frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

def audio_processing_process():
    while True:
        process_audio_and_text()

# Start video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

# Create and start threads
capture_thread = threading.Thread(target=video_capture_thread, args=(cap,))
process_thread = threading.Thread(target=processing_thread)
audio_process = multiprocessing.Process(target=audio_processing_process)

capture_thread.start()
process_thread.start()
audio_process.start()

# Wait for threads and processes to finish
capture_thread.join()
process_thread.join()
audio_process.join()

# Release resources
cap.release()
cv2.destroyAllWindows()
