import __main__
from Users.view_bookings import view_booking
from take_input import take_input
from Accounts.signup import signup_user
from Accounts.login import login
from Admin.add_movie import add_movie
from Admin.view_movies import view_movies
from clear_screen import clear_screen
from Admin.edit_movie import edit_movie
from Admin.manage_bookings import manage_bookings
from Users.book_movie import book_movie


def menu():
    print(f"{'*'*10}\tMenu\t{'*'*10}")
    if __main__.role == -1:
        print("1. Sign Up as a New User", "2. Login", "3. Quit", sep="\n")
        auth_action = take_input(
            input_statement="Your choice: ", error_message="Invalid Input", input_type='int', input_range=(1, 4))

        if auth_action == 1:
            return signup_user()

        elif auth_action == 2:
            return login()

        elif auth_action == 3:
            clear_screen()
            return False

    elif __main__.role == 0:
        print("1. Book a ticket ", "2. View past bookings",
              "3. Logout", "4. Quit", sep="\n")
        action_choice = take_input(
            input_statement="Your choice: ", error_message="Invalid Input", input_type='int', input_range=(1, 5))

        if action_choice == 1:
            return book_movie()

        elif action_choice == 2:
            return view_booking()

        elif action_choice == 3:
            clear_screen()

            __main__.role = -1
            return True

        elif action_choice == 4:
            clear_screen()
            return False

    elif __main__.role == 1:
        print("1. Add a new movie", "2. View movie details", "3. Edit a movie",
              "4. Manage bookings", "5. Create an admin account", "6. Logout", "7. Quit", sep="\n")
        action_choice = take_input(input_statement="Your choice: ",
                                   error_message="Invalid Input", input_type='int', input_range=(1, 8))

        if action_choice == 1:
            return add_movie()

        elif action_choice == 2:
            return view_movies()

        elif action_choice == 3:
            return edit_movie()

        elif action_choice == 4:
            return manage_bookings()

        elif action_choice == 5:
            return signup_user(isAdmin=True)

        elif action_choice == 6:
            clear_screen()
            __main__.role = -1
            return True

        elif action_choice == 7:
            clear_screen()
            return False
