import fresh_tomatoes, media

movie_1 = media.Movie("John Wick",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

movie_2 = media.Movie("John Wick: Chapter 2",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_SY1000_CR0,0,648,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=ChpLV9AMqm4")

movie_3 = media.Movie("The Wizard of Oz",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNjUyMTc4MDExMV5BMl5BanBnXkFtZTgwNDg0NDIwMjE@._V1_SY1000_CR0,0,670,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=FfpF8UUVTeM")

movie_4 = media.Movie("La La Land",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_SY1000_SX675_AL_.jpg",
                      "https://www.youtube.com/watch?v=0pdqf4P9MB8")

movie_5 = media.Movie("Valerian and the City of a Thousand Planets",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMDAxNDUyNV5BMl5BanBnXkFtZTgwOTc3MzcxMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=BszXhUjJz00")

movie_6 = media.Movie("Wonder Woman",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_SX675_AL_.jpg",
                      "https://www.youtube.com/watch?v=VSB4wGIdDwo")

movies = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]

fresh_tomatoes.open_movies_page(movies)
