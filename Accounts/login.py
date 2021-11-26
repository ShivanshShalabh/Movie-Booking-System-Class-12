import __main__
from take_input import take_input
from clear_screen import clear_screen


def login():
    print("Login")
    email = take_input(
        input_statement="Enter Email-id: ", error_message="Invalid Input", input_type='email')
    password = take_input(
        input_statement="Enter Password: ")
    __main__.cursor.execute(
        f"SELECT * FROM Users WHERE email = '{email}' AND password = '{password}'")
    user = __main__.cursor.fetchall()
    if user:
        user = user[0]
        __main__.user = {'id': user[0], 'username': user[1], 'password': user[2], 'email': user[3], 'first_name': user[4],
                         'last_name': user[5], 'phone_number': user[6], 'user_type': user[7], 'dob': user[8], 'date_created': user[9]}

        __main__.role = 0 if __main__.user['user_type'] == 'User' else 1
        clear_screen()
        print(f"Welcome {__main__.user['first_name']}")
    else:
        print("Login Failed\nPlease check the email and password")
    cache = open('cache.txt', 'w')
    cache.write(str(__main__.user)+'\n')
    cache.write(str(__main__.role))
    cache.close()
    return True
