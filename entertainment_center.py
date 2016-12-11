import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","Story of Boy and Toy",
		"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ" )

#print(avatar.storyline)
#avatar.show_trailer()

bossbaby = media.Movie("The Boss Baby","A wildly imaginative 7-year-old (Miles Bakshi) clashes with his demanding newborn brother (Alec Baldwin).","https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg","https://www.youtube.com/watch?v=tquIfapGVqs");

#bossbaby.show_trailer()
midnight_in_paris = media.Movie("Midnight in Paris","Gil arrives with his fiancee and her family in Paris for a vacation, even as he tries to finish his debut novel. He is beguiled by the city, which takes him to a time past, away from his fiancee.","https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=BYRWfS2s2v4")

school_of_rocks = media.Movie("School of Rock","Dewey Finn, an amateur rock enthusiast, slyly takes up his friend's substitute teacher's job. Bearing no qualifications for it, he instead starts training the students to be a band.","https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=XCwy6lW5Ixc")

hunger_games = media.Movie("The Hunger Games","Katniss volunteers to replace her sister in a tournament, where the participants must kill their counterparts to qualify for the next round. Can she defeat professionals in order to survive the game?","https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg","https://www.youtube.com/watch?v=4S9a5V9ODuY")

matrix= media.Movie("The Matrix","Thomas, a computer programmer, is led to fight an underground war against powerful computers who now rule the world with a system called 'The Matrix'.","https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg","https://www.youtube.com/watch?v=m8e-FF8MsqU")


movies = [toy_story,avatar,bossbaby,midnight_in_paris,school_of_rocks,hunger_games,matrix]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
