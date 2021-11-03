from movie import Movie
import csv


class MovieCatalog:

    def __init__(self):
        self.rows = open("movies.csv", "r")
        self.movies_list = [i for i in csv.reader(self.rows)]

    def get_movie(self, title: str) -> Movie:
        for movie in self.movies_list:
            if title == movie[1]:
                return Movie(title, int(movie[2]), movie[3].split("|"))
