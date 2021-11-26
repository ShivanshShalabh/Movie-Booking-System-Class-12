def movie_detail_processor(movie):
    movie = {'id': movie[0],
             'name': movie[1],
             'decription': movie[2],
             'duration': movie[3],
             'languages': movie[3+1],
             'rating': {movie[4+1]},
             'release_date': movie[5+1],
             'roll_back_date': movie[6+1],
             'date_added': movie[7+1],
             'last_edited': movie[8+1]}
    return movie
