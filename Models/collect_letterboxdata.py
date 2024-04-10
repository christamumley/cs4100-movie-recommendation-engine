from Models.letterboxd import get_watched, get_movie_genres, count_items, corresponding_themes
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk



def collect_letterboxd_data(user_name):
    try:
        movies = get_watched(user_name)
    except Exception as e:
        return e
    
    genres, themes, my_dict = get_movie_genres(movies)
    top_genres = count_items(genres, 3)

    #key is the genre we want, values are the themes we want within that genre
    g_t_dict = corresponding_themes(top_genres, my_dict)
    return top_genres, g_t_dict


    
    










