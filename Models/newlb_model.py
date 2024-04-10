import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity


from collect_letterboxdata import collect_letterboxd_data

genre_file_path = 'Datasets/letterboxd_data/genres.csv'
themes_file_path = 'Datasets/letterboxd_data/themes.csv'
movies_file_path = 'Datasets/letterboxd_data/lb_movies.csv'

genre_data = pd.read_csv(genre_file_path)
genre_data.to_csv('Datasets/letterboxd_data/genres.csv', index=False) 

themes_data = pd.read_csv(themes_file_path)
themes_data.to_csv('Datasets/letterboxd_data/themes.csv', index=False) 

movies_data = pd.read_csv(movies_file_path)
movies_data.to_csv('Datasets/letterboxd_data/lb_movies.csv', index=False) 
        
key_column = movies_data.columns[0]
merged = pd.merge(genre_data, themes_data, on=key_column, how='inner')
merged_movies = pd.merge(merged, movies_data, on=key_column, how='inner')

grouped_movies = merged_movies.groupby(['id', 'name', 'description']).agg({
    'genre': lambda x: list(set(x)),
    'theme': lambda x: list(set(x))
}).reset_index()

filename = f"Datasets/letterboxd_data/merged_lb_dataset.csv"
grouped_movies.to_csv(filename, index=False)

merged_file_path = 'Datasets/letterboxd_data/merged_lb_dataset.csv'
merged_movies_data = pd.read_csv(merged_file_path)
merged_movies_data['genre'] = merged_movies_data['genre'].apply(eval)
merged_movies_data['theme'] = merged_movies_data['theme'].apply(eval)

merged_movies_data['genres_str'] = merged_movies_data['genre'].apply(lambda x: ', '.join(x))
merged_movies_data['themes_str'] = merged_movies_data['theme'].apply(lambda x: ', '.join(x))

# Concatenate 'genres_str' and 'themes_str' into 'keywords' column
merged_movies_data['keywords'] = merged_movies_data['genres_str'] + ', ' + merged_movies_data['themes_str']

# Drop the intermediate columns if needed
merged_movies_data.drop(['genres_str', 'themes_str'], axis=1, inplace=True)

def lemmatize_(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    return ' '.join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])

merged_movies_data['keywords'] = merged_movies_data['keywords'].str.lower()
merged_movies_data['keywords'] = merged_movies_data['keywords'].str.replace(",", "")
merged_movies_data['keywords'] = merged_movies_data['keywords'].apply(lemmatize_)

tfidf_vectorizer_keywords  = TfidfVectorizer()
tfidf_matrix_keywords  = tfidf_vectorizer_keywords.fit_transform(merged_movies_data['keywords'])

# Drop the intermediate columns if needed
#merged_movies_data.drop(['keywords'], axis=1, inplace=True)

merged_file_path = 'Datasets/letterboxd_data/merged_lb_dataset.csv'
merged_movies_data.to_csv(filename, index=False)


def similar_movies(user_input, movie_data, tfidf_vectorizer=tfidf_vectorizer_keywords, tfidf_matrix = tfidf_matrix_keywords):
    # Calculate cosine similarity between the predicted plot and all movie plots

    input_vector = tfidf_vectorizer.transform([user_input])
    cosine_sim = cosine_similarity(input_vector, tfidf_matrix)

    # Find the index of the movie with the highest similarity score
    most_similar_index = cosine_sim.argmax()
    # Get details of the most similar movie
    most_similar_movie = movie_data['name'].iloc[most_similar_index]
    movies_file_path = 'Datasets/letterboxd_data/lb_movies.csv'
    lb_data = pd.read_csv(movies_file_path)
    most_similar_movie = lb_data.loc[lb_data['name'] == most_similar_movie]
    title = most_similar_movie.iloc[0]['name']
    description = most_similar_movie.iloc[0]['description']
    return title, description

def preprocess_user_input(genre, themes):
    genre_list = [genre]

    # Concatenate genre and themes lists
    keywords_list = genre_list + themes

    # Convert the list of keywords to a single string 
    keywords_str = ' '.join(keywords_list)
    keywords_str = keywords_str.lower()
    keywords_str = keywords_str.replace(",", "")
    keywords_str = lemmatize_(keywords_str)



    return keywords_str   

def rec_letterbox(user_name):
    movies_file_path = 'Datasets/letterboxd_data/merged_lb_dataset.csv'
    movies_data = pd.read_csv(movies_file_path)

    # 3. Recommendation Algorithm
    # After the user provides their preferred genres and themes
    genres, dict = collect_letterboxd_data(user_name)

    recommended_movies = {}

    # Predict movie plot based on user's preferred genres and themes
    for genre in genres:
        user_themes = dict[genre]
        user_keywords = preprocess_user_input(genre, user_themes)
        
        # Train TF-IDF vectorizer and matrix specific to the current genre
        #tfidf_vectorizer = TfidfVectorizer()
        #tfidf_matrix = tfidf_vectorizer.fit_transform(movies_data['Keywords_str'])

        recommended_movie, description = similar_movies(user_keywords, movies_data)
        recommended_movies[genre] = recommended_movie , description

    return recommended_movies


