import cv2
import imutils
import time
import winsound
from facial_detections import detectFace
from blink_detection import isBlinking
from mouth_tracking import mouthTrack
from object_detection import detectObject
from eye_tracker import gazeDetection
from head_pose_estimation import head_pose_detection
from datetime import datetime
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import os

data_record = []
cheating_scores = []  # To store cheating scores over time
running = True

# For Beeping
frequency = 2500
duration = 1000

# OpenCV videocapture for the webcam
cam = cv2.VideoCapture(0)

# If camera is not opened, try to open it
if not cam.isOpened():
    cam.open()

# Face Count If-else conditions
def faceCount_detection(faceCount):
    if faceCount > 1:
        time.sleep(5)
        remark = "Multiple faces have been detected."
        winsound.Beep(frequency, duration)
    elif faceCount == 0:
        remark = "No face has been detected."
        time.sleep(5)
        winsound.Beep(frequency, duration)
    else:
        remark = "Face detecting properly."
    return remark

def calculate_cheating_probability(faceCount, blinkCount, eyeStatus, mouth_status, objectName, head_pose_status):
    # Adjusted weights for each factor
    weights = {
        'face_count': 0.25,
        'blink': 0.1,
        'eye_status': 0.25,
        'mouth_status': 0.1,
        'object_detected': 0.2,
        'head_pose': 0.1,
    }
    
    # Initialize probability
    probability = 0
    
    # Check face count
    if faceCount > 1 or faceCount == 0:
        probability += weights['face_count'] * 1.0  # 100% chance if multiple/no faces detected
    
    # Check blink count
    if blinkCount > 5:
        probability += weights['blink'] * 1.0  # Excessive blinking
    
    # Check eye status
    if eyeStatus in ['left', 'right', 'Looking Up']:
        probability += weights['eye_status'] * 1.0  # Suspicious eye movement
    
    # Check mouth status
    if mouth_status == "Mouth Open":
        probability += weights['mouth_status'] * 1.0  # Mouth open
    
    # Check object detection
    if len(objectName) > 1:
        probability += weights['object_detected'] * 1.0  # Object detected
    
    # Check head pose
    if head_pose_status in ['Head Left', 'Head Right']:
        probability += weights['head_pose'] * 1.0  # Suspicious head movement

    # Ensure probability is max 100%
    return min(probability, 1.0)

# Main function
def proctoringAlgo():
    blinkCount = 0
    last_capture_time = time.time()  # Track the time of the last image capture
    image_counter = 1  # Counter for naming images

    while running:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame = imutils.resize(frame, width=450)
        record = []

        # Reading the current time
        current_time = datetime.now().strftime("%H:%M:%S.%f")
        print("Current time is:", current_time)
        record.append(current_time)

        # Detect faces and count them
        faceCount, faces = detectFace(frame)
        remark = faceCount_detection(faceCount)
        print(remark)
        record.append(remark)

        if faceCount == 1:
            # Blink Detection
            blinkStatus = isBlinking(faces, frame)
            print(blinkStatus[2])

            if blinkStatus[2] == "Blink":
                blinkCount += 1
                record.append(blinkStatus[2] + " count: " + str(blinkCount))
            else:
                record.append(blinkStatus[2])

            # Gaze Detection
            eyeStatus = gazeDetection(faces, frame)
            print(eyeStatus)
            record.append(eyeStatus)

            # Mouth Position Detection
            mouth_status = mouthTrack(faces, frame)
            print(mouth_status)
            record.append(mouth_status)

            # Object detection using YOLO
            objectName = detectObject(frame)
            print(objectName)
            record.append(objectName)

            if len(objectName) > 1:
                time.sleep(4)
                winsound.Beep(frequency, duration)
                continue

            # Head Pose estimation
            head_pose_status = head_pose_detection(faces, frame)
            print(head_pose_status)
            record.append(head_pose_status)
        
            # Calculate cheating probability
            cheating_probability = calculate_cheating_probability(faceCount, blinkCount, eyeStatus, mouth_status, objectName, head_pose_status)
            print(f"Cheating Probability: {cheating_probability * 100:.2f}%")
            record.append(f"Cheating Probability: {cheating_probability * 100:.2f}%")
            cheating_scores.append(cheating_probability)

        data_record.append(record)

        # Capture and save an image every 10 seconds
        current_time_sec = time.time()
        if current_time_sec - last_capture_time >= 10:
            image_name = f"test_image{image_counter}.jpg"
            cv2.imwrite(image_name, frame)
            print(f"Captured image: {image_name}")
            image_counter += 1
            last_capture_time = current_time_sec

        # Convert the frame to JPEG format for streaming
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
    
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cam.release()
    cv2.destroyAllWindows()

# Create PDF Report with Cheating Probability
def create_pdf_with_data(data_record, avg_cheating_prob):
    # Convert the list to a string with each element on a new line
    activityVal = "\n".join(map(str, data_record))

    # Create instance of FPDF class
    pdf = FPDF()
    pdf.add_page()
    
    # Set font
    pdf.set_font("Arial", size = 12)
    
    # Add a cell
    pdf.cell(200, 10, txt = "Proctoring Data", ln = True, align = 'C')
    
    # Add a line break
    pdf.ln(10)
    
    # Add the activity data
    pdf.multi_cell(0, 10, activityVal)
    
    # Add average cheating probability
    pdf.ln(10)
    pdf.cell(200, 10, txt = f"Average Cheating Probability: {avg_cheating_prob * 100:.2f}%", ln = True, align = 'C')
    
    # Save the pdf to a temporary file
    temp_pdf = "temp_output.pdf"
    pdf.output(temp_pdf)
    return temp_pdf

def append_to_pdf(existing_pdf, new_pdf):
    pdf_writer = PdfWriter()

    # Read the existing PDF
    pdf_reader = PdfReader(existing_pdf)
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    # Read the new PDF
    new_pdf_reader = PdfReader(new_pdf)
    for page in new_pdf_reader.pages:
        pdf_writer.add_page(page)

    # Write the updated PDF
    with open(existing_pdf, "wb") as f:
        pdf_writer.write(f)

def main_app():
    # Calculate the average cheating probability
    if cheating_scores:
        avg_cheating_prob = sum(cheating_scores) / len(cheating_scores)
    else:
        avg_cheating_prob = 0

    # Create a new temporary PDF with the latest data
    temp_pdf = create_pdf_with_data(data_record, avg_cheating_prob)

    # Check if the output.pdf exists
    output_pdf = "output.pdf"
    try:
        # Append the new content to the existing PDF
        append_to_pdf(output_pdf, temp_pdf)
    except FileNotFoundError:
        # If output.pdf does not exist, rename the temp PDF to output.pdf
        import shutil
        shutil.move(temp_pdf, output_pdf)

if __name__ == "__main__":
    main_app()
