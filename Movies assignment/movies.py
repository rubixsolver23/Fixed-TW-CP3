
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
        self.printable_movie_list = []
    
    def search_genre(self, genre):
        genre_list = []
        for movie in self.movie_list:
            if movie.genre.lower() == genre.lower():
                genre_list.append(movie)
        return MovieList(genre_list)
    
    def search_director(self, director):
        director_list = []
        for movie in self.movie_list:
            if movie.director.lower() == director.lower():
                director_list.append(movie)
        return MovieList(director_list)
        
    def search_cast(self, actor):
        actor_list = []
        for movie in self.movie_list:
            if actor in movie.actors:
                actor_list.append(movie)
        return MovieList(actor_list)

    def sort_alphabetical(self):
        titles_list = [movie.title for movie in self.movie_list]
        titles_list.sort()
        new_list = []
        for title in titles_list:
            for movie in self.movie_list:
                if movie.title == title:
                    new_list.append(movie)
                    break
                
        self.movie_list = new_list
    
    def sort_chronological(self):
        year_list = [movie.year for movie in self.movie_list]
        year_list.sort()
        new_list = []
        for year in year_list:
            for movie in self.movie_list:
                if movie.year == year:
                    new_list.append(movie)
                    self.movie_list.remove(movie)
                    break
                
        self.movie_list = new_list
    
    def __str__(self):
        self.printable_movie_list = []
        for movie in self.movie_list:
            self.printable_movie_list.append(str(movie))
        return "\n".join(self.printable_movie_list)



movies = MovieList([
    Movie(
        "The Shawshank Redemption", 1994, "Drama", "R", "Frank Darabont",
        ["Tim Robbins", "Morgan Freeman"]
    ),
    Movie(
        "Pulp Fiction", 1994, "Crime", "R", "Quentin Tarantino", 
        ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]
    ),
    Movie(
        "The Godfather", 1942, "Crime", "R", "Francis Ford Coppola",
        ["Marlon Brando, Al Pacino, James Caan"]
    ),
    Movie(
        "Inception", 2010, "Sci-Fi", "PG-13", "Christopher Nolan", 
        ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    ),
    Movie(
        "The Matrix", 1999, "Sci-Fi", "R", "Lana Wachowski", 
        ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]
    ),
    Movie(
        "Forrest Gump", 1994, "Drama", "PG-13", "Robert Zemeckis",
        ["Tom Hanks", "Robin Wright", "Gari Sinise"]
    ),
    Movie(
        "The Dark Night", 2008, "Action", "PG-13", "Chirstopher Nolan",
        ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    ),
    Movie(
        "Schindler's List", 1993, "Drama", "R", "Steven Spielberg",
        ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"]
    ),
    Movie(
        "Fight Club", 1999, "Drama", "R", "David Fincher", 
        ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"]
    ),
    Movie(
        "Goodfellas", 1990, "Crime", "R", "Martin Scorsese",
        ["Robert De Niro", "Ray Liotta", "Joe Pesci"]
    ),
    Movie(
        "The Silence of the Lambs", 1991, "Thriller", "R", "Jonathan Demme",
        ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"]
    ),
    Movie(
        "Titanic", 1997, "Romance", "PG-13", "James Cameron",
        ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"]
    ),
    Movie(
        "The Lord of the Rings: The Fellowship of the Ring", 2001, "Fantasy", "PG-13", "Peter Jackson",
        ["Elijah Wood", "Ian McKellen", "Orlando Bloom"]
    ),
    Movie(
        "Gladiator", 2000, "Action", "R", "Ridley Scott",
        ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"]
    ),
    Movie(
        "The Green Mile", 1999, "Drama", "R", "Frank Darabont",
        ["Tom Hanks", "Michael Clarke Duncan", "David Morse"]
    ),
    Movie(
        "Saving Private Ryan", 1998, "War", "R", "Steven Spielberg",
        ["Tom Hanks", "Matt Damon", "Tom Sizemore"]
    ),
    Movie(
        "Jurassic Park", 1993, "Adventure", "PG-13", "Steven Spielberg",
        ["Sam Neill", "Laura Dern", "Jeff Goldblum"]
    ),
    Movie(
        "The Departed", 2006, "Crime", "R", "Martin Scorsese",
        ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"]
    ),
    Movie(
        "The Lion King", 1994, "Animation", "G", "Roger Allers",
        ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"]
    ),
    Movie(
        "Eternal Sunshine of the Spotless Mind", 2004, "Romance", "R", "Michel Gondry",
        ["Jim Carrey", "Kate Winslet", "Kirsten Dunst"]
    )
])

def main():
    while True:
        print(
"""
To print the list of movies, type                  P
To sort the movies in alphabetical order, type     1
To sort the movies in chronological order, type    2
To search the movies for a certain genre, type     A
To search the movies for a certain director, type  B
To search the movies for a certain actor, type     C
To exit, type                                      X
"""
        )
        action = input("What would you like to do?: ")
        if action == "P":
            print(movies)
        elif action == "1":
            movies.sort_alphabetical()
        elif action == "2":
            movies.sort_chronological()
        elif action == "A":
            print(movies.search_genre(input("What genre do you want to serach for?: ")))
        elif action == "B":
            print(movies.search_director(input("What director do you want to search for?: ")))
        elif action == "C":
            print(movies.search_cast(input("What actor do you want to search for? (please capitalize): ")))
        elif action == "X":
            print("Goodbye!")
            break
        else:
            print("This is an invalid input.")

main()