import __main__
from Common.print_movie_detail import print_movie_details
from take_input import take_input
from clear_screen import clear_screen
from Common.movie_detail_processor import movie_detail_processor


def view_movies():
    clear_screen()
    print("1. View all movies", "2. Get movie by name", "3. Get movie by release date", "4. Get movie by language",
          "5. Get movie by rating", "6. Get movie by roll back date", "7. Get movie by date added",  sep="\n")
    action_choice = take_input(
        input_statement="Your choice: ", error_message="Invalid Input", input_type='int', input_range=(1, 8))
    clear_screen()
    if action_choice == 1:  # View all Movies

        __main__.cursor.execute("SELECT * FROM MovieDetails")
        all_movies = __main__.cursor.fetchall()
        if not all_movies:
            print("No movies found")
        else:
            print("**All Movies**")
            for movie in all_movies:
                print("\n"+"-"*10+"\n")
                print_movie_details(movie)
            print("\n"+"-"*10+"\n")

    elif action_choice == 2:  # Get movie by name
        movie_name = take_input(
            input_statement="Enter the name of the movie: ")
        __main__.cursor.execute(
            f"SELECT * FROM MovieDetails WHERE name = '{movie_name}'")
        movie_details = __main__.cursor.fetchall()

        if not movie_details:
            print("No movie found with that name")
        else:
            print("\n"+"-"*10+"\n")
            print_movie_details(movie_details[0])
            print("\n"+"-"*10+"\n")
    elif action_choice == 3 or action_choice == 6:  # Get movie by release date or roll back date
        date = take_input(
            input_statement="Enter the release date of the movie: ", input_type='date')
        __main__.cursor.execute(
            f"SELECT * FROM MovieDetails WHERE {'release_date' if action_choice == 3 else 'roll_back_date'} = '{date}'")
        all_movies = __main__.cursor.fetchall()

        if not all_movies:
            print(
                f"No movie found with that {'release' if action_choice == 3 else 'roll back'} date")
        else:
            print(
                f"Movie with {'release' if action_choice == 3 else 'roll back'} date as {date}")
            for movie in all_movies:
                print("\n"+"-"*10+"\n")
                print_movie_details(movie)
            print("\n"+"-"*10+"\n")
    elif action_choice == 4:  # Get movie by language
        language = (take_input(
            input_statement="Enter the language of the movie: ")).lower()
        __main__.cursor.execute(
            f"SELECT * FROM MovieDetails")
        all_movies = __main__.cursor.fetchall()
        all_movies = list(all_movies)
        desired_movies = []
        for i in range(len(all_movies)):
            movie = movie_detail_processor(all_movies[i])
            if language in movie['languages'].lower():
                desired_movies.append(all_movies[i])

        if not desired_movies:
            print("No movie found with that language")
        else:
            for movie in desired_movies:
                print("\n"+"-"*10+"\n")
                print_movie_details(movie)
            print("\n"+"-"*10+"\n")
    elif action_choice == 5:  # Get movie by rating
        rating = take_input(
            input_statement="Enter the rating of the movie: ", input_type='float', input_range=(0, 6))
        __main__.cursor.execute(
            f"SELECT * FROM MovieDetails WHERE rating = {rating}")
        all_movies = __main__.cursor.fetchall()
        if not all_movies:
            print("No movie found with that rating")
        else:
            for movie in all_movies:
                print("\n"+"-"*10+"\n")
                print_movie_details(movie)
            print("\n"+"-"*10+"\n")
    elif action_choice == 7:  # Get movie by date added
        date = take_input(
            input_statement="Enter the date added of the movie: ", input_type='date')
        __main__.cursor.execute(
            f"SELECT * FROM MovieDetails WHERE date_added = '{date}'")
        all_movies = __main__.cursor.fetchall()
        if not all_movies:
            print(
                f"No movie found with that date added")
        else:
            for movie in all_movies:
                print("\n"+"-"*10+"\n")
                print_movie_details(movie)
            print("\n"+"-"*10+"\n")
    return True
