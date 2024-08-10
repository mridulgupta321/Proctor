import mysql.connector

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

def insert_signup(email, username, password):
    try:
        # Create a cursor object
        cursor = cnx.cursor()

        query = "INSERT INTO sign_up (email, username, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (email, username, password))
        cnx.commit()
        cursor.close()
        print("Sign-Up data credentials inserted successfully!")
        return 1

    except mysql.connector.Error as err:
        print("Error inserting the sign-up credentials:", err)
        # Rollback changes if necessary
        cnx.rollback()
        return -1
    
    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback changes if necessary
        cnx.rollback()
        return -1

def search_login_credentials(email, password):
    cursor = cnx.cursor()

    query = "SELECT email, password FROM sign_up WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))
    rows = cursor.fetchall()
    cursor.close()
    
    if rows:
        print("Data found")
        return True
    else:
        print("No data found.")
        return False

if __name__ == "__main__":
    print("All Sign-Up Details:")
    get_all_details()
    # Example usage:
    # print(search_login_credentials('kumar1166@gmail.com', 'Krishna1'))
    # insert_signup('newuser@gmail.com', 'newuser', 'newpassword')
    # print("Updated Sign-Up Details:")
    # get_all_details()
