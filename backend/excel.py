import mysql.connector
from PIL import Image
import io
import os

# Create a connection to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="quizo"
)

def save_images_from_db():
    try:
        cursor = cnx.cursor()
        
        # Query to fetch all records with BLOB data
        query = "SELECT candidate_id, candidate_image FROM sign_up WHERE candidate_image IS NOT NULL"
        cursor.execute(query)
        
        # Fetch all records
        records = cursor.fetchall()
        
        # Create images directory if it doesn't exist
        if not os.path.exists('images'):
            os.makedirs('images')
        
        for record in records:
            candidate_id, image_blob = record
            
            # Convert BLOB data to an image
            image = Image.open(io.BytesIO(image_blob))
            
            # Save the image as a JPG file
            image_path = f"exam/images/{candidate_id}.jpg"
            image.save(image_path, format='JPEG')
            
            print(f"Image for candidate_id {candidate_id} saved as {image_path}")
        
        cursor.close()
        
    except mysql.connector.Error as err:
        print("Error fetching data from the database:", err)
    
    except Exception as e:
        print(f"An error occurred while saving images: {e}")

if __name__ == "__main__":
    save_images_from_db()
