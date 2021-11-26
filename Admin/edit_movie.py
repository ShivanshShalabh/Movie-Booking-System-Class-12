from take_input import take_input
from Common.print_movie_detail import print_movie_details
import __main__
from clear_screen import clear_screen
from Admin.add_movie import add_movie


def edit_movie():
    movie_name = take_input(input_statement="Enter the name of the movie: ")
    __main__.cursor.execute(
        f"SELECT * FROM MovieDetails WHERE name = '{movie_name}'")
    movie_details = __main__.cursor.fetchall()
    print(movie_details)
    clear_screen()
    if not movie_details:
        print("No movie found with that name")
    else:
        print("Current movie details:")
        print_movie_details(movie_details[0])
        print("\n"+"-"*10+"\n")
        print("Enter the new details for the movie:")
        add_movie(movie_details[0][0])
    return True
