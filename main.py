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

data_record = []

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

# Main function
def proctoringAlgo():
    blinkCount = 0

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
        
        data_record.append(record)

        # Convert the frame to JPEG format for streaming
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
    
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cam.release()
    cv2.destroyAllWindows()
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter

def create_pdf_with_data(data_record):
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
    print(data_record)
    
    # Create a new temporary PDF with the latest data
    temp_pdf = create_pdf_with_data(data_record)

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
