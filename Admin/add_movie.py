from take_input import take_input
from clear_screen import clear_screen
import __main__
from datetime import datetime


def add_movie(editing=False):
    if not editing:
        clear_screen()
    print("Add Movie")
    name = take_input(input_statement="Enter the name of the movie: ")
    description = take_input(
        input_statement="Enter the description of the movie: ")
    duration = take_input(
        input_statement="Enter the duration of the movie: ")
    rating = take_input(input_statement="Enter the rating of the movie: ",
                        input_type='float', input_range=(0, 6))
    language = take_input(input_statement="Enter the language of the movie: ")
    release_date = take_input(
        input_statement="Enter the release date of the movie: ", input_type='date')
    roll_back_date = take_input(
        input_statement="Enter the roll back date of the movie: ", input_type='date')
    today = str(datetime.now().date())
    if not editing:
        __main__.cursor.execute(
            f"INSERT INTO MovieDetails(name ,decription, duration ,languages ,rating ,release_date ,roll_back_date ,date_added ,last_edited) VALUES('{name}', '{description}','{duration}','{language}', {rating}, '{release_date}','{roll_back_date}', '{today}','{today}')")

    else:
        __main__.cursor.execute(
            f"UPDATE MovieDetails SET name = '{name}', decription = '{description}',duration = '{duration}', languages = '{language}', rating = {rating}, release_date = '{release_date}', roll_back_date = '{roll_back_date}', last_edited = '{today}' WHERE movie_id = {editing}")

    __main__.mydb.commit()
    clear_screen()
    if not editing:
        # get auto incremented value of added movie
        __main__.cursor.execute(
            "SELECT movie_id FROM MovieDetails ORDER BY movie_id DESC LIMIT 1")
        movie_id = __main__.cursor.fetchone()[0]
        print(f"Movie added successfully with id {movie_id}")

    else:
        print(f"Movie information updated successfully")
    return True
