import mysql.connector
from datetime import datetime
from capture import *

# Create a connection to the database
cnx = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="", 
    database="quizo"
)

def get_all_details():
    cursor = cnx.cursor()

    query = "SELECT * FROM sign_up"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()

def insert_signup(name, gender, dob, mobile, email, password):
    try:
        cursor = cnx.cursor()

        query = """
        INSERT INTO sign_up (name, gender, dob, mobile, email, password)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, gender, dob, mobile, email, password))
        cnx.commit()
        cursor.close()
        print("Sign-Up data credentials inserted successfully!")    
        return 1

    except mysql.connector.Error as err:
        print("Error inserting the sign-up credentials:", err)
        cnx.rollback()
        return -1
    
    except Exception as e:
        print(f"An error occurred: {e}")
        cnx.rollback()
        return -1


def search_login_credentials(email, password):
    try:
        cursor = cnx.cursor()

        # Modify the query to select the name and password
        query = "SELECT name, email, password FROM sign_up WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))
        
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            name, email, _ = row
            
            # Get the current date and time
            start_time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

            # Store the start time in the database
            cursor = cnx.cursor()
            update_query = "UPDATE sign_up SET start_time = NOW() WHERE email = %s"
            cursor.execute(update_query, (email,))
            cnx.commit()
            cursor.close()
            
            text_to_write = f"Data found for {name}:\nEmail: {email}"
            with open('report.txt', 'w') as file:
                file.write(text_to_write)
            
            cursor = cnx.cursor()
            query = "SELECT candidate_id FROM sign_up WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                candidate_id = result[0]
                image_path = f"exam/{candidate_id}.jpg"
                capture_image(image_path)
            

            cursor = cnx.cursor()
            with open(image_path, 'rb') as file:
                binary_data = file.read()

            # Update the image in the database
            query = "UPDATE sign_up SET candidate_image = %s WHERE candidate_id = %s"
            cursor.execute(query, (binary_data, candidate_id))
            
            cnx.commit()
            result = cursor.fetchone()
            cursor.close()
            
            print("Login successful. Start time recorded:", start_time)
            return {'username': name, 'message': 'Login successful'}
        else:
            print("No data found.")
            return None

    except mysql.connector.Error as err:
        print("Error during login process:", err)
        return None

    except Exception as e:
        print(f"An error occurred during login process: {e}")
        return None

def save_score(email, score, total_questions, violations):
    try:
        cursor = cnx.cursor()

        # Calculate percentage score
        percentage = (score / total_questions) * 100

        # Fetch the current time as the time_taken value
        time_taken = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

        # Update the database with the final score, time taken, and violation scale
        query = """
        UPDATE sign_up 
        SET total_score = %s, 
            percentage = %s, 
            time_taken = %s, 
            violation_scale = %s, 
            attempted = %s
        WHERE email = %s
        """
        cursor.execute(query, (score, percentage, time_taken, violations, total_questions, email))
        cnx.commit()
        cursor.close()

        print(f"Score for {email} saved successfully with a percentage of {percentage:.2f}%.")
        return 1

    except mysql.connector.Error as err:
        print("Error saving the score:", err)
        cnx.rollback()
        return -1
    
    except Exception as e:
        print(f"An error occurred while saving the score: {e}")
        cnx.rollback()
        return -1

# Example usage:
# save_score('newuser@gmail.com', 5, 6, 2)


if __name__ == "__main__":
    print("All Sign-Up Details:")
    get_all_details()
    # Example usage:
    # print(search_login_credentials('kumar1166@gmail.com', 'Krishna1'))
    # insert_signup('New User', 'Male', '2000-01-01', '1234567890', 'newuser@gmail.com', 'newpassword')
    # print("Updated Sign-Up Details:")
    # get_all_details()
