import __main__


def print_movie_details(movie):
    if __main__.role == 1:
        print(f'Id : {movie[0]}')
    print(f'Name : {movie[1]}')
    print(f'Decription : {movie[2]}')
    print(f'Duration : {movie[3]}')
    print(f'Languages : {movie[1+3]}')
    print(f'Rating : {movie[1+4]}')
    print(f'Release Date : {movie[1+5]}')
    if __main__.role == 1:
        print(f'Roll Back Date : {movie[1+6]}')
        print(f'Date Added : {movie[1+7]}')
        print(f'Last Edited : {movie[1+8]}')
