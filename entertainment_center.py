# Import media (where class Movie is defined) and fresh_tomatoes (the program
# that will generate the final html page).
import media
import fresh_tomatoes

# Create instances for each movie in the final html page. 
barbarella = media.Movie(
	"Barbarella (1968)",
	"The sexiest astronavigatrix on a journey to find an evil scientist",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMzcwMjU4OV5BMl5BanBnXkFtZTgwNzYzMjU2MTE@._V1_SY1000_CR0,0,683,1000_AL_.jpg",  #NOQA
	"https://www.youtube.com/watch?v=0Xo6FaypcpY"
	)

death_race_2000 = media.Movie(
	"Death Race 2000 (1975)",
	"A deadly road race reality show",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BNTQ3OTA3ODc4NV5BMl5BanBnXkFtZTYwMjM3NDg4._V1._CR4,1,275,438_.jpg",  #NOQA
	"https://www.youtube.com/watch?v=atSyNC0aP3Y"
	)

attack_of_the_killer_tomatoes = media.Movie(
	"Attack of the Killer Tomatoes (1978)",
	"Scientists try to save the world from vicious mutated tomatoes",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BZWMxOTEzMjktYjE3NC00NmZjLThlNzYtMDE3MDlmNWVmZTZkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,627,1000_AL_.jpg",  #NOQA
	"https://www.youtube.com/watch?v=fy0fTFpqT48"
	)

flash_gordon = media.Movie(
	"Flash Gordon (1980)",
	"A football player travels to a distant planet to save the Earth",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMjE1OTU3ODAwMl5BMl5BanBnXkFtZTcwMzQ2NjczNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  #NOQA
	"https://www.youtube.com/watch?v=PfjZoM_wrV0"
	)

time_bandits = media.Movie(
    "Time Bandits (1982)",
    "A kid joins a band of time-traveling dwarf thieves",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MDYwMzM0NF5BMl5BanBnXkFtZTcwODI3MTQ5OQ@@._V1_.jpg",  #NOQA
    "https://www.youtube.com/watch?v=JwnjENpIyq0"
    )

kung_fury = media.Movie(
    "Kung Fury (2015)",
    "Miami's most powerful cop travels in time to beat the Kung Führer",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQwMjU2ODU5NF5BMl5BanBnXkFtZTgwNTU1NjM4NTE@._V1_SY999_CR0,0,702,999_AL_.jpg",  #NOQA
    "https://www.youtube.com/watch?v=nO_DIwuGBnA"
    )

# Create an array with all the instances of Movie.
movies = [
    barbarella, death_race_2000, attack_of_the_killer_tomatoes,
    flash_gordon, time_bandits, kung_fury
    ]

# Call function to create an html page using fresh_tomatoes.
fresh_tomatoes.open_movies_page(movies)
