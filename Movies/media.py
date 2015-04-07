class Movie():
    """This class provieds a way to store movie related information."""

    def __init__(self, title, storyline, poster_image, trailer_url, rating):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url
        self.rating = rating
