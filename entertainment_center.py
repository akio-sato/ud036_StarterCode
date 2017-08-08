#!/usr/bin/env python2.7

import fresh_tomatoes, media

movie_1 = media.Movie("John Wick",
                      "An ex-hitman comes out of retirement to track down the gangsters that took everything from him.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

movie_2 = media.Movie("John Wick: Chapter 2",
                      "After returning to the criminal underworld to repay a debt, John Wick discovers that a large bounty has been put on his life.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_SY1000_CR0,0,648,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=ChpLV9AMqm4")

movie_3 = media.Movie("The Wizard of Oz",
                      "Dorothy Gale is swept away from a farm in Kansas to a magical land of Oz in a tornado and embarks on a quest with her new friends to see the Wizard who can help her return home in Kansas and help her friends as well.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNjUyMTc4MDExMV5BMl5BanBnXkFtZTgwNDg0NDIwMjE@._V1_SY1000_CR0,0,670,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=FfpF8UUVTeM")

movie_4 = media.Movie("La La Land",
                      "Two proper L.A. dreamers, a suavely charming soft-spoken jazz pianist and a brilliant vivacious playwright, while waiting for their big break, attempt to reconcile aspirations and relationship in a magical old-school romance.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_SY1000_SX675_AL_.jpg",
                      "https://www.youtube.com/watch?v=0pdqf4P9MB8")

movie_5 = media.Movie("Valerian and the City of a Thousand Planets",
                      "A dark force threatens Alpha, a vast metropolis and home to species from a thousand planets. Special operatives Valerian and Laureline must race to identify the marauding menace and safeguard not just Alpha, but the future of the universe.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMDAxNDUyNV5BMl5BanBnXkFtZTgwOTc3MzcxMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=BszXhUjJz00")

movie_6 = media.Movie("Wonder Woman",
                      "Before she was Wonder Woman, she was Diana, princess of the Amazons, trained warrior. When a pilot crashes and tells of conflict in the outside world, she leaves home to fight a war, discovering her full powers and true destiny.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_SX675_AL_.jpg",
                      "https://www.youtube.com/watch?v=VSB4wGIdDwo")

movies = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]
fresh_tomatoes.open_movies_page(movies)
