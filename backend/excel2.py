import mysql.connector
import pandas as pd
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Create a connection to the database
cnx = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="", 
    database="quizo"
)

def fetch_data():
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT * FROM sign_up"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def save_data_to_excel(data):
    # Create a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Save the DataFrame to an Excel file
    excel_path = 'exam_data.xlsx'
    df.to_excel(excel_path, index=False, engine='openpyxl')
    
    # Load the workbook and select the active worksheet
    workbook = Workbook()
    worksheet = workbook.active
    
    # Iterate through the DataFrame and add images
    for i, row in df.iterrows():
        candidate_id = row['candidate_id']
        image_path ="C:\Users\gupta\Desktop\Artificial-Intelligence-based-Online-Exam-Proctoring-System-main\exam\images\1.jpg"
        img = Image(image_path)
        
        # Add image to the Excel sheet
        cell = f'G{i + 2}'  # Adjust as needed
        worksheet.add_image(img, cell)
    
    # Save the workbook
    workbook.save(excel_path)

if __name__ == "__main__":
    data = fetch_data()
    save_data_to_excel(data)
    print("Data and images saved to Excel file.")
