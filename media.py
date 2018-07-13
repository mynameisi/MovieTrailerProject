class Movie():
    def __init__(self, title, trailer_url, poster_url):
        """Form a Movie object

        Keyword arguments:
        title -- the title of the movie
        trailer_url -- the trailer url of the movie
        poster_url -- the url of a poster image of the movie
        """
        self.title = title
        self.trailer_youtube_url = trailer_url
        self.poster_image_url = poster_url
