import webbrowser

# define movie class
class Movie():
    """docstring for Movie that allows the creation of different instances"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.movie_title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        """docstring for the instance method to show trailers of different movies"""
        webbrowser.open(self.trailer_youtube_url)
