import __main__
from take_input import take_input


def menu():
    if __main__.role == -1:
        print("1. Sign Up as a New User", "2. Login as a User",
              "3. Login as an Admin", "4. Quit")
        auth_action = take_input(
            input_statement="Your choice: ", error_message="Invalid Input", is_int=True, input_range=(1, 4))
        if auth_action == 1:
            # Take input First Name, Last Name, Phone Number, Date of Birth, Email-id, password
            # Create a new user
            pass

        elif auth_action == 2:
            # Login as a user
            print("Login")
        elif auth_action == 3:
            # Login as an admin
            print("Login")
        elif auth_action == 4:
            # Quit
            print("Quitting")
            exit(0)
