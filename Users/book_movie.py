from Common.print_movie_detail import print_movie_details
from string import ascii_uppercase
from Common.print_seating import print_seating
from take_input import take_input
from clear_screen import clear_screen
import __main__


def book_movie():
    clear_screen()
    print("Book Movie")
    show_id_and_movie_id = {}
    show_id_set = set()
    __main__.cursor.execute(
        "SELECT * FROM BookingDetails")
    bookings = __main__.cursor.fetchall()
    if not bookings:
        print("No show available")
        return True
    for booking in bookings:
        movie_id = booking[1]

        __main__.cursor.execute(
            f"SELECT * FROM MovieDetails WHERE movie_id = {movie_id}")

        movie_details = __main__.cursor.fetchone()
        show_id = movie_details[0]
        print("Show ID:", show_id)
        show_id_set.add(show_id)
        print_movie_details(movie_details)
        print(f"\n{'-'*20}\n")
        show_id_and_movie_id[show_id] = movie_id
    user_show_id = int(input("Enter the show id to book: "))
    while user_show_id not in show_id_set:
        user_show_id = int(input("Invalid Input\nEnter the show id to book: "))
    __main__.cursor.execute(
        f"SELECT * FROM MovieDetails WHERE movie_id = {show_id_and_movie_id[user_show_id]}")
    movie_details = __main__.cursor.fetchone()
    print()
    print_movie_details(movie_details)
    user_confirmation = take_input(
        input_statement="Are you sure you want to book this show?(y/n): ")
    if user_confirmation.lower() == "y":
        __main__.cursor.execute(
            f"SELECT * FROM SeatingInfo WHERE show_id = {user_show_id}")
        seats = __main__.cursor.fetchone()
        if not seats:
            print("Something went wrong, please contact admin and share the show ID.")
        else:
            seat_details = seats[2]
            seat_details = seat_details.split("!")
            available_time = {}
            for i in range(len(seat_details)):
                seat_details[i] = seat_details[i].split("*")
                date = seat_details[i][0]
                time = seat_details[i][1]

                if date not in available_time:
                    available_time[date] = []
                available_time[date].append(time)

            print("\nAvailable Timings:")
            for i in available_time.keys():
                time = ', '.join(available_time[i])
                time = time.replace('1', 'Morning')
                time = time.replace('2', 'Afternoon')
                time = time.replace('3', 'Evening')
                time = time.replace('4', 'Night')
                print(f"{'.'.join(i.split('-')[::-1])} - {time}")
            user_date = take_input(
                "Enter the date of booking: ", input_type='date')
            if user_date not in available_time:
                user_date = take_input(
                    "Invalid Input\nEnter the date of booking: ", input_type='date')
            user_time = str(take_input(
                "Enter the time of the show:\n1 for Morning\n2 for Evening\n3 for Afternoon\n4 for Night\nYour choice: ", input_type='int', input_range=(1, 5)))
            while user_time not in available_time[user_date]:
                user_time = str(take_input(
                    "Invalid Input\nEnter the time of the show:\n1 for Morning\n2 for Evening\n3 for Afternoon\n4 for Night\nYour choice: ", input_type='int', input_range=(1, 5)))
            user_show_index = -1
            seating = ""
            for i in range(len(seat_details)):
                if seat_details[i][0] == user_date and seat_details[i][1] == user_time:
                    seating = seat_details[i][2]
                    user_show_index = i
            seats_req = take_input(
                "Enter the number of seats required: ", input_type='int', input_range=(1, seating.count('0')))
            seating_lst = seating.split('|')
            for i in range(len(seating_lst)):
                seating_lst[i] = seating_lst[i].split('-')
            width = 0
            height = len(seating_lst)
            for i in seating_lst[0]:
                width += len(i)
            print("Seating Chart:", "0: Available\n1: Booked", sep="\n")
            print_seating(seating)
            seats_req_copy = seats_req
            print("Enter the seat number in the format <column><row> like A1 and B7.")
            user_seats_lst = []
            while seats_req:
                seat = take_input(
                    f"Enter the seat number {seats_req_copy-seats_req+1}: ", input_type='str', input_range=(2, 4))
                seat = [seat[0].upper(), eval(seat[1:])]
                if seat[0] not in ascii_uppercase[:width] or seat[1] not in range(1, height+1):
                    print("Invalid Input")
                    continue
                temp_width = ascii_uppercase.index(seat[0])
                for k in range(len(seating_lst[seat[1]-1])):

                    if len(seating_lst[seat[1]-1][k]) > temp_width:
                        if seating_lst[seat[1]-1][k][temp_width] == '1':
                            print("Seat already taken")
                            continue
                        seating_lst[seat[1]-1][k] = seating_lst[seat[1] -
                                                                1][k][:temp_width]+'X'+seating_lst[seat[1]-1][k][temp_width+1:]
                        user_seats_lst.append(f"{seat[0]}{seat[1]}")
                        seats_req -= 1
                        break

                    else:
                        temp_width -= len(seating_lst[seat[1]-1][k])

            for i in range(len(seating_lst)):
                seating_lst[i] = '-'.join(seating_lst[i])
            seating_lst = '|'.join(seating_lst)

            print_seating(seating_lst)
            print("The seats chosen by you are marked with 'X'")
            confirmation = take_input(
                "Are you sure you want to book this seat?(y/n): ", input_type='str')
            if confirmation.lower() != 'y':
                return True
            seating_lst = seating_lst.replace('X', '1')

            seat_details[user_show_index][2] = seating_lst
            for ii in range(len(seat_details)):
                seat_details[ii] = '*'.join(seat_details[ii])
            seat_details = '!'.join(seat_details)
            __main__.cursor.execute(
                f"UPDATE SeatingInfo SET all_seating_details = '{seat_details}' WHERE show_id = {user_show_id}")
            __main__.mydb.commit()
            __main__.cursor.execute(
                f"INSERT INTO Tickets(show_id, user_id, timing, show_date, seat_number) VALUES({user_show_id}, '{__main__.user['id']}', '{user_time}', '{user_date}', '{', '.join(user_seats_lst)}')")
            __main__.mydb.commit()
            print("Booking Successful")
            return True
