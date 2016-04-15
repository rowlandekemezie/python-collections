from media import Movie
import fresh_tomatoes

#1 hungry games
hungry_games = Movie('Hungry games',
                     'This is the movie for the hungary folks',
                     'http://www.rantchic.com/wp-content/uploads/2014/06/The-Hunger-Games.jpg',
                     'https://www.youtube.com/watch?v=811Llm99M88&feature=youtu.be')

#2 rataouille
rataouille = Movie('rataouille',
                   'Another movie for the rataouille',
                   'http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg',
                   'https://www.youtube.com/watch?v=3YG4h5GbTqU&feature=youtu.be')
#3 school of rock
school_of_rock = Movie('school_of_rock',
                       'The school of the rocks is a cool movie to watch in this season',
                       'https://i.ytimg.com/vi_webp/cwuZAaqcMfY/mqdefault.webp',
                       'https://www.youtube.com/watch?v=cwuZAaqcMfY&feature=youtu.be')
#4 midnight in paris
midnight_in_paris = Movie('midnight in paris',
                          'An elavorate movie of events taking place in paris especially at night',
                          'https://i.ytimg.com/vi/FAfR8omt-CY/mqdefault.jpg',
                          'https://www.youtube.com/watch?v=zVuuooZqVaU&feature=youtu.be')

#5 toy story
toy_story = Movie('toy story',
                        'The story of toys  and the joy of seeing toys play',
                        'http://media.comicbook.com/uploads1/2015/03/group-disney-announces-toy-story-4-is-happening-126226.jpeg',
                        'https://www.youtube.com/watch?v=fOFgtfdRmw0')
#6 Avatar
avatar = Movie('Avatar',
                     'The marine avatar for all humans',
                     'http://www.lexpress.to/data/manchettes/00004560.lrg.jpg',
                     'https://www.youtube.com/watch?v=9LwajYQeEWI')
# call open page
movies = [hungry_games, rataouille, school_of_rock, midnight_in_paris, toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
