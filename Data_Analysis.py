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

# Function to get members in a specified age range using SQL BETWEEN
def get_members_in_age_range(start_age, end_age):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"
            cursor.execute(query, (start_age, end_age))
            results = cursor.fetchall()
            
            members = []
            for row in results:
                members.append({
                    "id": row[0],
                    "name": row[1],
                    "age": row[2]
                })
            
            return members
        except Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

# Example usage
if __name__ == "__main__":
    members_in_age_range = get_members_in_age_range(25, 30)
    for member in members_in_age_range:
        print(member)
