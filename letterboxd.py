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