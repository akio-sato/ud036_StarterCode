"""Script to produce a movie trailer website.

Usage: Run the following command.

$ python entertainment_center.py
"""
import fresh_tomatoes
import media

# John Wick
movie_1 = media.Movie("John Wick",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

# John Wick: Chapter 2
movie_2 = media.Movie("John Wick: Chapter 2",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_SY1000_CR0,0,648,1000_AL_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=ChpLV9AMqm4")

# The Wizard of Oz
movie_3 = media.Movie("The Wizard of Oz",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNjUyMTc4MDExMV5BMl5BanBnXkFtZTgwNDg0NDIwMjE@._V1_SY1000_CR0,0,670,1000_AL_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=FfpF8UUVTeM")

# La La Land
movie_4 = media.Movie("La La Land",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_SY1000_SX675_AL_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=0pdqf4P9MB8")

# Valerian and the City of a Thousand Planets
movie_5 = media.Movie("Valerian and the City of a Thousand Planets",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMDAxNDUyNV5BMl5BanBnXkFtZTgwOTc3MzcxMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=BszXhUjJz00")

# Wonder Woman
movie_6 = media.Movie("Wonder Woman",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_SX675_AL_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=VSB4wGIdDwo")

# Create a list of Movie class
movies = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]

# Create an HTML file and open a web browser
fresh_tomatoes.open_movies_page(movies)
