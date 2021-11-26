# Admin email: foo@foo.com and password: 123456
# Import libraries
import mysql.connector

# Import modules
from setup import run_setup
from menu import menu


if __name__ == '__main__':
    role = -1  # User role
    user = {}  # User details
    db_name = 'BOOK_MY_MOVIE'
    mydb = mysql.connector.connect(
        host="localhost",
        user="USER",
        passwd="Helloworld@123",
    )
    cursor = mydb.cursor()
    run_setup()  # Create database and tables
    while menu():  # Display menu
        pass
    print("Thank you for using our service!")
    print("Hope to see you again!")
