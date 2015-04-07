import media
import fresh_tomatoes

# Create instances of Movie class
# Each instance of movie contains info specific said movie.
toy_story = media.Movie(
        "Toy Story",
        "Story of a boy and his toys that come to life.",
        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://youtu.be/KYz2wyBy3kc",
        "G"
    )
avatar = media.Movie(
        "Avatar",
        "Blue people jump around wildly.",
        "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
        "https://youtu.be/cRdxXPV9GNQ",
        "PG-13"
    )
school_of_rock = media.Movie(
        "School of Rock",
        "Some goofy dude teaches kids how to live the rock life.",
        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
        "https://youtu.be/3PsUJFEBC74",
        "PG-13"
    )
midnight_in_paris = media.Movie(
        "Midnight in Paris",
        "Going back in time to meet authors.",
        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
        "https://youtu.be/BYRWfS2s2v4",
        "PG-13"
    )
hunger_games = media.Movie(
        "Hunger Games",
        "Woman fights off others in magical dome",
        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
        "https://youtu.be/4S9a5V9ODuY",
        "PG-13"
    )

# Create movies list that contains each movie instantiated above.
movies = [toy_story, avatar, school_of_rock, midnight_in_paris, hunger_games]

# Use fresh_tomatoes 'open_movies_page' function to create and open page.
fresh_tomatoes.open_movies_page(movies)
