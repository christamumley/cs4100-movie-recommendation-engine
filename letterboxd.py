import requests
from bs4 import BeautifulSoup

def get_watched(username):
    # get html 
    url = f'https://letterboxd.com/{username}/films/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # get movie names from image alt texts
    images = soup.find_all(class_='image')
    movies = [image.get('alt') for image in images]
    return movies 

def get_movie_genres(movies) :
    # get html for each movie
    genres = []
    themes = []
    for movie in movies:

        formatted_movie = movie.lower().replace(' ', '-')
        url = f'https://letterboxd.com/film/{formatted_movie}/genres/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # get genres
        genre_themes_parent = soup.find(id='tab-genres')
        div_elements = genre_themes_parent.find_all('div')
        # Get the second div element
        
        genre_tab = genre_themes_parent.find('div', class_= 'text-sluglist capitalize')
        genre_tags = genre_tab.find_all(class_='text-slug')
        genres = [tag.text.strip() for tag in genre_tags]

        if len(div_elements) > 1:
            theme_tab = genre_tab.find_next_sibling('div', class_= 'text-sluglist capitalize')
            theme_tags = theme_tab.find_all(class_='text-slug')
            themes = [tag.text.strip() for tag in theme_tags]


    return genres, themes

movies_test= get_watched('jay')
print(movies_test)

genres_test, themes_test = get_movie_genres(['ferrari-2023'])
print(genres_test, themes_test)