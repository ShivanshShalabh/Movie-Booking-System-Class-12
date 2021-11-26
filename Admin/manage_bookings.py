from Common.movie_detail_processor import movie_detail_processor
from time import sleep
from clear_screen import clear_screen
from datetime import datetime
import datetime as datetime_parent
import __main__
from take_input import take_input
from Common.print_movie_detail import print_movie_details
from Common.print_seating import print_seating


def manage_bookings():
    empty_threater = ("000-000000-00|"*12)[:-1]
    clear_screen()
    print("Manage Bookings")
    print("1. Schedule shows", "2. Cancel a movie releaase",
          "3. View scheduled shows", "4. View booking for a specific show", "5. View booking of a movie", "6. Back", sep="\n")
    action_choice = take_input(
        "Enter your choice: ", input_type='int', input_range=(1, 7))
    if action_choice == 1:
        # Release a movie
        movie_id = take_input(
            "Enter the movie id: ", input_type='int')
        __main__.cursor.execute(
            f"SELECT * FROM MovieDetails WHERE movie_id = '{movie_id}'")
        movie_details = __main__.cursor.fetchone()
        release_date = take_input(
            "Enter the release date of the show: ", input_type='date')
        roll_back_date = take_input(
            "Enter the roll back date of the show: ", input_type='date')
        print("What are the show timings")
        timings = take_input(
            "1 for Morning (11 AM)\n2 for Afternoon (2 PM)\n3 for Evening (6 PM)\n4 for night (9 PM)\nSeperate multiple choice with a comma\nYour choice: ", input_type='str')
        timings_list = timings.replace(" ", "").split(",")
        release_date_list = release_date.split("-")
        # convert each element of release_date_list to int using map
        release_date_list = list(map(int, release_date_list))
        roll_back_list = roll_back_date.split("-")
        roll_back_list = list(map(int, roll_back_list))
        now = datetime(
            release_date_list[0], release_date_list[1], release_date_list[2])
        then = datetime(
            roll_back_list[0], roll_back_list[1], roll_back_list[2])
        duration = (then - now).days
        date_list = [
            now + datetime_parent.timedelta(days=x) for x in range(duration)]
        for i in range(len(date_list)):
            date_list[i] = str(date_list[i].date())

        all_threater_seats = []
        for i in date_list:
            for k in timings_list:
                all_threater_seats.append(
                    f"{i}*{k}*{empty_threater}")
        today = str(datetime.now().date())
        if not movie_details:
            print("Movie not found")
        else:
            __main__.cursor.execute(
                f"INSERT INTO BookingDetails(movie_id, show_timings, release_date,roll_back_date,date_added) VALUES ('{movie_id}','{timings}','{release_date}', '{roll_back_date}','{today}')")
            __main__.mydb.commit()
            sleep(1)
            __main__.cursor.execute(
                f"SELECT * FROM BookingDetails WHERE movie_id = '{movie_id}'")
            show_details = __main__.cursor.fetchall()
            show_details = show_details[-1]
            show_id = show_details[0]
            __main__.cursor.execute(
                f"INSERT INTO SeatingInfo(show_id, all_seating_details) VALUES ('{show_id}','{'!'.join(all_threater_seats)}')")
            __main__.mydb.commit()
            print(f"Show scheduled successfully with id {show_id}")
    elif action_choice == 2:
        # Cancel a show
        show_id = take_input(
            "Enter the show id: ", input_type='int')
        __main__.cursor.execute(
            f"SELECT * FROM BookingDetails WHERE show_id = '{show_id}'")
        show_details = __main__.cursor.fetchone()
        if show_details is None:
            print("Show not found")
        else:
            cancel_choice = take_input(
                "Are you sure you want to cancel this show, this will also delete all the seatings info? (y/n): ", input_type='str')
            if cancel_choice == 'y':
                __main__.cursor.execute(
                    f"DELETE FROM BookingDetails WHERE show_id = '{show_id}'")
                __main__.mydb.commit()
                __main__.cursor.execute(
                    f"DELETE FROM SeatingInfo WHERE show_id = '{show_id}'")
                __main__.mydb.commit()
    elif action_choice == 3:
        # View bookings
        __main__.cursor.execute(
            "SELECT * FROM BookingDetails")
        bookings = __main__.cursor.fetchall()

        if not bookings:
            print("No bookings found")
        else:
            clear_screen()
            print("Show Details")
            for booking in bookings:

                movie_id = booking[1]
                __main__.cursor.execute(
                    f"SELECT * FROM MovieDetails WHERE movie_id = '{movie_id}'")
                movie_details = __main__.cursor.fetchone()
                movie_details = movie_detail_processor(movie_details)
                print()
                print("Show id: ", booking[0])
                print(f"Movie Name: {movie_details['name']}")
                print(f"Release Date: {booking[3]}")
                print(f"Roll Back Date: {booking[4]}")
                print(f"Show Timings: {booking[2]}")
                print(f"Date Added: {booking[5]}")
                print()
                print(f"\n{'-'*20}")
    elif action_choice == 4:
        show_id = take_input(
            "Enter the show id: ", input_type='int')
        __main__.cursor.execute(
            f"SELECT * FROM BookingDetails WHERE show_id = '{show_id}'")
        show_details = __main__.cursor.fetchone()
        print(show_details)
        if not show_details:
            print("Show not found")
        else:
            __main__.cursor.execute(
                f"SELECT * FROM SeatingInfo WHERE show_id = '{show_id}'")
            show_seats = __main__.cursor.fetchone()
            show_seats = show_seats[2].split("!")
            for i in show_seats:
                i = i.split("*")
                print(f"Date: {i[0]}")
                print(f"Timings: {i[1]}")
                print(f"Seats: ")
                print_seating(i[2])
                print(f"\n{'-'*20}\n")
            # print(show_seats)
    elif action_choice == 5:
        show_id = take_input(
            "Enter the show id: ", input_type='int')
        date = take_input(
            "Enter the date: ", input_type='str')
        date = (date.split("/")[::-1])
        date = list(map(int, date))
        date = datetime(date[0], date[1], date[2])

        date = date.date()
        date = str(date)
        timings = take_input(
            "Enter the timings: ", input_type='int', input_range=[1, 5])
        __main__.cursor.execute(
            f"SELECT * FROM BookingDetails WHERE show_id = '{show_id}'")
        show_details = __main__.cursor.fetchone()
        # print(show_details)
        if not show_details:
            print("Show not found")
        else:
            __main__.cursor.execute(
                f"SELECT * FROM SeatingInfo WHERE show_id = '{show_id}'")
            show_seats = __main__.cursor.fetchone()
            show_seats = show_seats[2].split("!")
            movie_there = False
            for i in show_seats:
                i = i.split("*")
                if i[0] != date or eval(i[1]) != timings:
                    movie_there = True
                    continue
                print(f"Date: {i[0]}")
                print(f"Timings: {i[1]}")
                print(f"Seats: ")
                print_seating(i[2])
                print(f"\n{'-'*20}\n")
            if not movie_there:
                print("Show not found")
            # print(show_seats)
    return True
