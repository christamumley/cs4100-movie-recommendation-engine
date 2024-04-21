from collections import Counter
import requests
from bs4 import BeautifulSoup


def get_watched(username):
    # get html 
    try:
        url = f'https://letterboxd.com/{username}/likes/films/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        return e
    

    images = soup.find_all(class_='image')
    movies = [image.get('alt') for image in images]

    for i in range(10):
        try:
            url = f'https://letterboxd.com/{username}/likes/films/page/{i+2}/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            break
        images = soup.find_all(class_='image')
        current_movies = [image.get('alt') for image in images]
        movies.extend(current_movies)
    return movies 

def get_movie_genres(movies) :
    # get html for each movie
    genres_total = []
    themes_total = []
    my_dict = {}
    for movie in movies:

        formatted_movie = movie.lower().replace(' ', '-')
        url = f'https://letterboxd.com/film/{formatted_movie}/genres/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # get genres
        genre_themes_parent = soup.find(id='tab-genres')
        try:
            div_elements = genre_themes_parent.find_all('div')
        except AttributeError:
            continue

        # Get the second div element
        
        genre_tab = genre_themes_parent.find('div', class_= 'text-sluglist capitalize')
        genre_tags = genre_tab.find_all(class_='text-slug') 
        genres = [tag.text.strip() for tag in genre_tags]
        genres_total.extend(genres) 

        if len(div_elements) > 1:
            theme_tab = genre_tab.find_next_sibling('div', class_= 'text-sluglist capitalize')
            theme_tags = theme_tab.find_all(class_='text-slug')
            themes = [tag.text.strip() for tag in theme_tags]
            str = 'Show All…'
            while str in themes:
                themes.remove(str)
            themes_total.extend(themes)
            my_dict[movie] = [genres, themes]
        else:
            my_dict[movie] = [genres]

    return genres_total, themes_total, my_dict

def count_items(items_list, n):
    counter = Counter()
    counter.update(items_list)
    c = counter.most_common(n)
    strings = [s[0] for s in c]
    return strings

def corresponding_themes(genres, my_dict):
    genre_themes = {}  # Dictionary to store themes for each genre
    for genre in genres:
        themes = []
        for movie, genre_nthemes in my_dict.items():
            if(len(genre_nthemes) == 2):
                genre_list, themes_list = genre_nthemes
                if genre in genre_list:                        
                    themes.extend(themes_list)
        top_themes = count_items(themes, 6)
        genre_themes[genre] = top_themes
    return genre_themes


'''
['We Live in Time', 'Irish Wish', 'Crossing', 'Madame Web', 'Dune: Part Two', 'My Wonderful Stranger', 'Love Lies Bleeding', 'Doctor Who: The Church on Ruby Road', 'Doctor Who: The Giggle', 'Doctor Who: Wild Blue Yonder', 'Wonka', 'Doctor Who: The Star Beast', 'Merchant Ivory', 'The Iron Claw', 'The Hunger Games: The Ballad of Songbirds & Snakes', 'Thanksgiving', "Five Nights at Freddy's", 'Chicken Run: Dawn of the Nugget', 'The Exorcist: Believer', 'Saw X', 'No One Will Save You', 'A Haunting in Venice', 'American Fiction', 'Hit Man', 'Priscilla', 'The Killer', 'Maestro', 'NYAD', 'Hoard', 'Poor Things', 'The Royal Hotel', 'The Wonderful Story of Henry Sugar', 'All of Us Strangers', 'Saltburn', 'The Holdovers', 'Ferrari', 'The Bikeriders', 'El Conde', 'Doctor Jekyll', 'Retribution', 'Gran Turismo', 'Teenage Mutant Ninja Turtles: Mutant Mayhem', 'The Boy and the Heron', 'Oppenheimer', 'Barbie', 'Insidious: The Red Door', 'Paradise', 'Mission: Impossible – Dead Reckoning Part One', 'Black Mirror: Demon 79', 'Black Mirror: Mazey Day', 'Black Mirror: Beyond the Sea', 'Black Mirror: Loch Henry', 'Black Mirror: Joan Is Awful', 'They Cloned Tyrone', 'The Flash', 'Meg 2: The Trench', 'Spider-Man: Across the Spider-Verse', 'La Chimera', 'In Our Day', 'Cobweb', 'The Taste of Things', 'Asteroid City', 'Kidnapped', 'Kubi', 'Fallen Leaves', 'The Boogeyman', 'Club Zero', 'Anatomy of a Fall', 'Killers of the Flower Moon', 'May December', 'The Zone of Interest', 'How to Have Sex']
[['Drama', 'Romance'], ['Romance', 'Fantasy', 'Comedy'], ['Fantasy', 'Action'], ['Drama'], ['Thriller', 'Crime', 'Action'], ['Comedy', 'Fantasy', 'Family'], ['Documentary'], ['Action', 'Adventure'], ['Drama'], ['Thriller', 'Horror'], ['Science Fiction', 'Thriller', 'Horror'], ['Crime', 'Mystery', 'Thriller'], ['Comedy', 'Drama'], ['Action'], ['Romance', 'Drama'], ['Crime', 'Drama', 'Action', 'Thriller'], ['Animation'], ['Drama', 'History'], ['Drama'], ['Thriller'], ['Drama', 'Thriller'], ['Fantasy', 'Comedy', 'Adventure'], ['Romance', 'Drama', 'Fantasy'], ['Comedy', 'Drama', 'Thriller'], ['Comedy', 'Drama'], ['Drama'], ['Crime', 'Drama'], ['Horror', 'Fantasy', 'Comedy'], ['Horror'], ['Horror', 'Thriller', 'Mystery'], ['Adventure', 'Action', 'Drama'], ['Animation', 'Adventure', 'Fantasy'], ['Drama'], ['Comedy', 'Adventure'], ['Adventure', 'Romance'], ['Comedy', 'Science Fiction', 'Mystery'], ['Science Fiction', 'Action', 'Adventure'], ['Comedy', 'Adventure', 'Drama', 'Fantasy'], ['Drama'], ['Music', 'Comedy', 'Romance'], ['Romance', 'Drama'], ['Comedy', 'Drama'], ['Adventure', 'Family', 'Action', 'Drama'], ['Action', 'Drama', 'History'], ['Drama'], ['Mystery', 'Horror', 'Thriller'], ['Comedy', 'Thriller', 'Drama'], ['Mystery', 'Crime', 'Thriller'], ['History', 'Crime', 'Drama'], ['Drama', 'Comedy'], ['Drama', 'History', 'War'], ['Drama']] 
[['Relationship comedy', 'Laugh-out-loud relationship entanglements', 'Charming romances and delightful chemistry', 'Quirky and endearing relationships', 'Captivating relationships and charming romance', 'Touching and sentimental family stories', 'Show All…'], ['Epic heroes', 'Superheroes in action-packed battles with villains', 'Show All…'], ['Song and dance', 'Humanity and the world around us', 'Crude humor and satire', 'Dazzling vocal performances and musicals', 'Holiday joy and heartwarming Christmas', 'Fairy-tale fantasy and enchanted magic', 'Catchy songs and hilarious musical comedy', "Kids' animated fun and adventure", 'Show All…'], ['Horror, the undead and monster classics', 'Graphic violence and brutal revenge', 'Gory,  gruesome,  and slasher horror', 'Twisted dark psychological thriller', 'Show All…'], ['Monsters, aliens, sci-fi and the apocalypse', 'Horror, the undead and monster classics', 'Sci-fi horror,  creatures,  and aliens', 'Terrifying,  haunted,  and supernatural horror', 'Twisted dark psychological thriller', 'Thought-provoking sci-fi action and future technology', 'Action-packed space and alien sagas', 'Show All…'], ['Thrillers and murder mysteries', 'Intriguing and suspenseful murder mysteries', 'Suspenseful crime thrillers', 'Terrifying,  haunted,  and supernatural horror', 'Noir and dark crime dramas', 'Twisted dark psychological thriller', 'Show All…'], ['Crude humor and satire', 'Humanity and the world around us', 'Moving relationship stories', 'Relationship comedy', 'Quirky and endearing relationships', 'Amusing jokes and witty satire', 'Funny jokes and crude humor', 'Gags,  jokes,  and slapstick humor', 'Teen school antics and laughter', 'Show All…'], ['Moving relationship stories', 'Passion and romance', 'Emotional teen coming-of-age stories', 'Enduring stories of family and marital drama', 'Emotional life of renowned artists', 'Powerful stories of heartbreak and suffering', 'Show All…'], ['Crime, drugs and gangsters', 'High speed and special ops', 'Moving relationship stories', 'Epic heroes', 'Violent action,  guns,  and crime', 'Intense combat and martial arts', 'Gritty crime and ruthless gangsters', 'Explosive and action-packed heroes vs. villains', 'Adrenaline-fueled action and fast cars', 'Show All…'], ['Humanity and the world around us', 'Inspiring sports underdog stories', 'Show All…'], ['Horror, the undead and monster classics', 'Terrifying,  haunted,  and supernatural horror', 'Show All…'], ['Humanity and the world around us', 'Emotional and captivating fantasy storytelling', 'Show All…'], ['Moving relationship stories', 'Humanity and the world around us', 'Powerful stories of heartbreak and suffering', 'Emotional LGBTQ relationships', 'Touching and sentimental family stories', 'Emotional and touching family dramas', 'Emotional teen coming-of-age stories', 'Show All…'], ['Intense violence and sexual transgression', 'Twisted dark psychological thriller', 'Challenging or sexual themes & twists', 'Erotic relationships and desire', 'Dreamlike,  quirky,  and surreal storytelling', 'Graphic violence and brutal revenge', 'Show All…'], ['Moving relationship stories', 'Underdogs and coming of age', 'Student coming-of-age challenges', 'Emotional and touching family dramas', 'Touching and sentimental family stories', 'Quirky and endearing relationships', 'Powerful stories of heartbreak and suffering', 'Show All…'], ['Crude humor and satire', 'Bloody vampire horror', 'Creepy,  chilling,  and terrifying horror', 'Gothic and eerie haunting horror', 'Show All…'], ['Thrillers and murder mysteries', 'Intriguing and suspenseful murder mysteries', 'Suspenseful crime thrillers', 'Terrifying,  haunted,  and supernatural horror', 'Gothic and eerie haunting horror', 'Gory,  gruesome,  and slasher horror', 'Show All…'], ['Moving relationship stories', 'Adrenaline-fueled action and fast cars', 'Inspiring sports underdog stories', 'Underdog fighting and boxing stories', 'Show All…'], ['Humanity and the world around us', 'Surreal and thought-provoking visions of life and death', 'Emotional and captivating fantasy storytelling', 'Dreamlike,  quirky,  and surreal storytelling', 'Fairy-tale fantasy and enchanted magic', 'Captivating relationships and charming romance', 'Show All…'], ['Humanity and the world around us', 'Crude humor and satire', 'Moving relationship stories', 'Emotional and captivating fantasy storytelling', 'Surreal and thought-provoking visions of life and death', 'Quirky and endearing relationships', 'Amusing jokes and witty satire', 'Laugh-out-loud relationship entanglements', 'Show All…'], ['Crude humor and satire', 'Humanity and the world around us', 'Dreamlike,  quirky,  and surreal storytelling', 'Gags,  jokes,  and slapstick humor', 'Amusing jokes and witty satire', 'Funny jokes and crude humor', 'Show All…'], ['Epic heroes', 'Superheroes in action-packed battles with villains', 'Emotional and captivating fantasy storytelling', 'Action comedy and silly heroics', 'Adrenaline-fueled action and fast cars', 'Show All…'], ['Moving relationship stories', 'Captivating relationships and charming romance', 'Charming romances and delightful chemistry', 'Passion and romance', 'Touching and sentimental family stories', 'Show All…'], ['Humanity and the world around us', 'Surreal and thought-provoking visions of life and death', 'Dreamlike,  quirky,  and surreal storytelling', 'Show All…'], ['Horror, the undead and monster classics', 'Intense violence and sexual transgression', 'Terrifying,  haunted,  and supernatural horror', 'Creepy,  chilling,  and terrifying horror', 'Twisted dark psychological thriller', 'Gothic and eerie haunting horror', 'Gory,  gruesome,  and slasher horror', 'Show All…'], ['Moving relationship stories', 'Thrillers and murder mysteries', 'Humanity and the world around us', 'Suspenseful crime thrillers', 'Enduring stories of family and marital drama', 'Gripping,  intense violent crime', 'Heartbreaking and moving family drama', 'Intriguing and suspenseful murder mysteries', 'Show All…'], ['Thrillers and murder mysteries', 'Crime, drugs and gangsters', 'Gripping,  intense violent crime', 'Suspenseful crime thrillers', 'Racism and the powerful fight for justice', 'Intense political and terrorist thrillers', 'Violent crime and drugs', 'Show All…'], ['Moving relationship stories', 'Intense violence and sexual transgression', 'Humanity and the world around us', 'Erotic relationships and desire', 'Challenging or sexual themes & twists', 'Enduring stories of family and marital drama', 'Powerful stories of heartbreak and suffering', 'Emotional teen coming-of-age stories', 'Show All…'], ['Humanity and the world around us', 'Nazis and World War II', 'Surreal and thought-provoking visions of life and death', 'Graphic violence and brutal revenge', 'Gripping,  intense violent crime', 'Terrifying,  haunted,  and supernatural horror', 'Show All…'], ['Humanity and the world around us', 'Emotional teen coming-of-age stories', 'Emotional LGBTQ relationships', 'Powerful poetic and passionate drama', 'Show All…']]

Example output form above print statements

***New update, also returns a dictionary that maps each movie to a list of genres and list of themes.
'''
