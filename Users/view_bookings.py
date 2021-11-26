from clear_screen import clear_screen
import __main__


def view_booking():
    clear_screen()
    __main__.cursor.execute(
        f"SELECT * FROM Tickets WHERE user_id = '{__main__.user['id']}'")
    bookings = __main__.cursor.fetchall()
    if not bookings:
        print("No bookings found")
    else:
        print("Past Bookings")
        print()
        for booking in bookings:
            show_id = booking[1]
            __main__.cursor.execute(
                f"SELECT * FROM BookingDetails WHERE show_id = {show_id}")
            show = __main__.cursor.fetchone()
            movie_id = show[1]
            __main__.cursor.execute(
                f"SELECT * FROM MovieDetails WHERE movie_id = {movie_id}")
            movie = __main__.cursor.fetchone()
            print(f"Movie: {movie[1]}")
            print(f"Date: {booking[4]}")
            print(f"Time: {booking[3]}")
            print(f"Duration: {movie[3]}")
            print(f"Seat: {booking[5]}")
            print(f"\n{'-'*20}\n")

    return True
