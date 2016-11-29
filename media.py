# Create class Movie and define its __init__ function. Class Movie takes 
# four arguments correlated to title, storyline, poster image and youtube
# trailer.
class Movie():
    def __init__(self, movie_title, movie_storyline, 
    	         poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
