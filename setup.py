import __main__
from datetime import datetime


def run_setup():
    # Creating database, tables and a super user
    __main__.cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {__main__.db_name};")
    __main__.cursor.execute(f"USE {__main__.db_name};")
    __main__.cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
        user_id int AUTO_INCREMENT,
        username varchar(255) NOT NULL ,
        password varchar(255) NOT NULL ,
        email varchar(255) NOT NULL ,
        first_name varchar(255) NOT NULL ,
        last_name varchar(255) NOT NULL ,
        phone_number varchar(255) NOT NULL ,
        user_type varchar(255) NOT NULL ,
        dob varchar(255) NOT NULL ,
        date_created varchar(255) NOT NULL,
        PRIMARY KEY (user_id)
    );''')
    # create a master user
    __main__.cursor.execute(
        f"SELECT * FROM Users WHERE email = 'foo@foo.com'")
    user = __main__.cursor.fetchall()
    if not user:
        __main__.cursor.execute(
            f"INSERT IGNORE INTO Users (username, password, email, first_name, last_name, phone_number, user_type, dob, date_created) VALUES ('Admin','123456', 'foo@foo.com', 'foo', 'foo', '1234567890', 'Admin', '1111-1-1', '{str(datetime.today().date())}');")

    __main__.cursor.execute(f'''CREATE TABLE IF NOT EXISTS MovieDetails (
        movie_id int AUTO_INCREMENT, 
        name varchar(255) NOT NULL , 
        decription varchar(255) NOT NULL , 
        duration varchar(255) NOT NULL , 
        languages varchar(255) NOT NULL , 
        rating float NOT NULL , 
        release_date varchar(255) NOT NULL ,
        roll_back_date varchar(255) NOT NULL , 
        date_added varchar(255) NOT NULL, 
        last_edited varchar(255) NOT NULL, 
        PRIMARY KEY (movie_id)
    );''')
    __main__.cursor.execute(f'''CREATE TABLE IF NOT EXISTS BookingDetails(
        show_id int AUTO_INCREMENT, 
        movie_id int NOT NULL , 
        show_timings varchar(255) NOT NULL, 
        release_date varchar(255) NOT NULL , 
        roll_back_date varchar(255) NOT NULL , 
        date_added varchar(255) NOT NULL, 
        PRIMARY KEY (show_id) 
    );''')
    __main__.cursor.execute('''CREATE TABLE IF NOT EXISTS SeatingInfo(
        booking_id int AUTO_INCREMENT,
        show_id int NOT NULL ,
        all_seating_details varchar(10000) NOT NULL ,                
        PRIMARY KEY (booking_id)
    );''')
    __main__.cursor.execute('''CREATE TABLE IF NOT EXISTS Tickets(
        ticket_id int AUTO_INCREMENT,
        show_id int NOT NULL ,
        user_id varchar(255) NOT NULL ,                
        timing varchar(255) NOT NULL ,
        show_date varchar(255) NOT NULL,
        seat_number varchar(255) NOT NULL ,
        PRIMARY KEY (ticket_id)
    );''')
