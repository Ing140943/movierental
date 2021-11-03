class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).

    def __init__(self, title, year, genre=None):
        # Initialize a new movie.
        if genre is None:
            genre = []
        self.__year = int(year)
        self.__title = title
        self.__genres = genre

    def get_year(self):
        return self.__year

    def get_title(self):
        return self.__title

    def get_genre(self, genre: str):
        return genre in self.__genres

    def __str__(self):
        return self.__title
