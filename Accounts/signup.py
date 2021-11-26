from take_input import take_input
from datetime import datetime
import __main__
from clear_screen import clear_screen


def signup_user(isAdmin=False):
    print("Sign Up")
    fname = take_input(
        input_statement="Enter First Name: ", error_message="Invalid Input")
    lname = take_input(
        input_statement="Enter Last Name: ", error_message="Invalid Input")
    phone = take_input(
        input_statement="Enter Phone Number: ", error_message="Invalid Input", input_range=(10, 11))
    dob = take_input(
        input_statement="Enter Date of Birth: ", error_message="Invalid Input", input_type='date')
    email = take_input(
        input_statement="Enter Email-id: ", error_message="Invalid Input", input_type='email')
    while True:
        password = take_input(
            input_statement="Enter Password: ", error_message="Invalid Input", input_range=(6, 30))
        confirm_password = input("Confirm Password: ")
        if password == confirm_password:
            break
        else:
            print("Password did not match. Please try again.")
    __main__.cursor.execute(
        f"INSERT INTO Users(username, password, email, first_name, last_name, phone_number, user_type, dob, date_created) VALUES ('{fname +' '+ lname}','{password}','{email}','{fname}','{lname}','{phone}','{'User' if not isAdmin else 'Admin'}','{dob}','{str(datetime.now().date())}')")
    __main__.mydb.commit()
    clear_screen()
    print("Sign Up Successful")
    print(f"Welcome {fname}")
    return True
