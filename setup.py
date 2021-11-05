import __main__


def run_setup():
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
        date_created varchar(255) NOT NULL,
        PRIMARY KEY (user_id)
    );''')
