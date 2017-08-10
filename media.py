class Movie():
    """This class provides a way to store movie related information
    
    Keyword arguments:
    movie_title -- the title of the movie
    box_art -- poster image file URL
    trailer_link -- YouTube URL
    """
    def __init__(self,
                 movie_title,
                 box_art,
                 trailer_link):
        self.title = movie_title
        self.poster_image_url = box_art
        self.trailer_youtube_url = trailer_link
