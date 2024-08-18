import mysql.connector
import pandas as pd

# MySQL database connection details
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'quizo'
}

# Connect to the MySQL database
connection = mysql.connector.connect(**db_config)

# SQL query to retrieve data
query = "SELECT * FROM sign_up"

# Execute query and load data into a pandas DataFrame
df = pd.read_sql(query, connection)

# Close the database connection
connection.close()

# Write the DataFrame to an Excel sheet
excel_file_path = 'output_file.xlsx'
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"Data has been written to {excel_file_path}")
