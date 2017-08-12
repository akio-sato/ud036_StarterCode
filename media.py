class Movie():
    """Store movie attributes.

    Instance variables:
    movie_title -- the title of the movie
    box_art -- poster image file URL
    trailer_link -- YouTube URL
    """

    def __init__(self,
                 movie_title,
                 box_art,
                 trailer_link):
        """Constructor for Movie object.

        Keyword arguments:
        movie_title -- the title of the movie
        box_art -- poster image file URL
        trailer_link -- YouTube URL
        """
        self.title = movie_title
        self.poster_image_url = box_art
        self.trailer_youtube_url = trailer_link
