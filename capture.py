import cv2

def capture_image(image_path):
    """
    Captures an image from the webcam and saves it to the specified path.

    Args:
        image_path (str): The path where the captured image will be saved.

    Returns:
        bool: True if the image was captured and saved successfully, False otherwise.
    """
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    try:
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

    finally:
        # Release the webcam and close any open windows
        cap.release()
        cv2.destroyAllWindows()
