import cv2
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def capture_image(image_path):
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return False

    # Capture a single frame
    ret, frame = cap.read()

    if ret:
        # Save the captured frame to a file
        cv2.imwrite(image_path, frame)
        print(f"Photo captured and saved as {image_path}")
        return True
    else:
        print("Error: Could not capture photo.")
        return False

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

def create_pdf_with_image(image_path, pdf_path):
    # Create a PDF document
    c = canvas.Canvas(pdf_path, pagesize=letter)
    
    # Open the image file
    image = Image.open(image_path)
    
    # Get the dimensions of the image
    width, height = image.size
    
    # Set the page size to match the image size
    c.setPageSize((width, height))
    
    # Draw the image on the PDF
    c.drawImage(image_path, 0, 0, width=width, height=height)
    
    # Save the PDF
    c.save()
    print(f"PDF created and saved as {pdf_path}")

# Paths for the image and PDF
image_path = 'captured_photo.jpg'
pdf_path = 'output.pdf'

def image_in_pdf():
    # Capture the image
    if capture_image(image_path):
        # Create the PDF with the captured image
        create_pdf_with_image(image_path, pdf_path)
