import mysql.connector
from mysql.connector import Error

# Function to establish a database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='your_host',
            user='your_username',
            password='your_password',
            database='your_database'
        )
        if connection.is_connected():
            print("Connection successful")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Task 1: Add a Member
def add_member(id, name, age):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(query, (id, name, age))
            connection.commit()
            print("Member added successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, session_time, activity):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (None, member_id, date, session_time, activity))
            connection.commit()
            print("Workout session added successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Task 3: Updating Member Information
def update_member_age(member_id, new_age):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Check if member exists
            cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
            if cursor.fetchone() is None:
                print("Member not found")
                return

            query = "UPDATE Members SET age = %s WHERE id = %s"
            cursor.execute(query, (new_age, member_id))
            connection.commit()
            print("Member age updated successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Check if session exists
            cursor.execute("SELECT * FROM WorkoutSessions WHERE session_id = %s", (session_id,))
            if cursor.fetchone() is None:
                print("Workout session not found")
                return

            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, (session_id,))
            connection.commit()
            print("Workout session deleted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Example usage
if __name__ == "__main__":
    # Add members
    add_member(1, 'Jane Doe', 28)
    add_member(2, 'John Smith', 35)

    # Add workout sessions
    add_workout_session(1, '2023-06-28', 'Morning', 'Yoga')
    add_workout_session(2, '2023-06-28', 'Afternoon', 'Cardio')

    # Update member age
    update_member_age(1, 29)

    # Delete workout session
    delete_workout_session(2)
