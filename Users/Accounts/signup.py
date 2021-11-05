from take_input import take_input
import __main__


def signup_user():
    print("Sign Up")
    fname = take_input(
        input_statement="Enter First Name: ", error_message="Invalid Input")
    lname = take_input(
        input_statement="Enter Last Name: ", error_message="Invalid Input")
    phone = take_input(
        input_statement="Enter Phone Number: ", error_message="Invalid Input")
    dob = take_input(
        input_statement="Enter Date of Birth: ", error_message="Invalid Input")
    email = take_input(
        input_statement="Enter Email-id: ", error_message="Invalid Input")
    while True:
        password = take_input(
            input_statement="Enter Password: ", error_message="Invalid Input", input_type='str', input_range=(6, 30))
        confirm_password = input("Confirm Password: ")
        if password == confirm_password:
            break
        else:
            print("Password did not match. Please try again.")
    print("Sign Up Successful")
