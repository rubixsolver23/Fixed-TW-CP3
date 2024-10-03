
class Movie:
    def __init__(self, title, year, genre, rating, director, actors):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating
        self.director = director
        self.actors = actors

    def __str__(self):
        return(f"{self.title}, ({self.year}), {self.director}, {self.rating}, {self.genre}, {self.actors}")

class MovieList:
    def __init__(self, movie_list):
        self.movie_list = movie_list
    
    def search_director(self, director):
        director_list = []
        for movie in self.movie_list:
            if movie.director.lower() == director:
                director_list.append(movie)
        
    def search_cast(self, actor):
        actor_list = []
        for movie in self.movie_list:
            if actor.capitalize() in movie.actors:
                actor_list.append(movie)
    
    def sort_alphabetical(self):
        titles_list = [movie.title for movie in self.movie_list]
        titles_list.sort()
        new_list = []
        for title in titles_list:
            pass



movies = MovieList([
    Movie(
        "The Shawshank Redemption", 1994, "Drama", "R", "Frank Darabont",
        ["Tim Robbins", "Morgan Freeman"]
    ),
    Movie(
        "Pulp Fiction", 1994, "Crime", "R", "Quentin Tarantino", 
        ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]
    ),
])

movies.sort_alphabetical()