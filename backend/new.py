import os
import pandas as pd

# Define the path to the images folder and the Excel file
images_folder = 'exam/images'
excel_file = 'exam_data.xlsx'

# Get a list of image filenames in the images folder
image_files = os.listdir(images_folder)

# Create a DataFrame from the list of filenames
df_images = pd.DataFrame(image_files, columns=['Image Names'])

# Load the existing Excel file
df_existing = pd.read_excel(excel_file)

# Add the new column to the existing DataFrame
df_existing['Image Names'] = df_images

# Save the updated DataFrame back to the Excel file
df_existing.to_excel(excel_file, index=False)
