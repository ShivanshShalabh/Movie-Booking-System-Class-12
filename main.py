# Import libraries
import mysql.connector

# Import modules
from setup import run_setup
from menu import menu

if __name__ == '__main__':
    role = -1
    db_name = 'BOOK_MY_MOVIE'
    mydb = mysql.connector.connect(
        host="localhost",
        user="USER",
        passwd="1234"
        # # database="mydatabase"
    )
    menu()
    cursor = mydb.cursor()
    run_setup()