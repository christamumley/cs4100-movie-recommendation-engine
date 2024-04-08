from Models.letterboxd import get_watched, get_movie_genres, count_items, corresponding_themes
import pandas as pd


def collect_letterboxd_data(user_name):
    movies = get_watched(user_name)
    genres, themes, my_dict = get_movie_genres(movies)
    top_genres = count_items(genres, 3)

    #key is the genre we want, values are the themes we want within that genre
    g_t_dict = corresponding_themes(top_genres, my_dict)

    genre_file_path = 'Datasets/letterboxd_data/genres.csv'
    themes_file_path = 'Datasets/letterboxd_data/themes.csv'
    movies_file_path = 'Datasets/letterboxd_data/lb_movies.csv'

    genre_data = pd.read_csv(genre_file_path)
    genre_data.to_csv('Datasets/letterboxd_data/genres.csv', index=False) 

    themes_data = pd.read_csv(themes_file_path)
    themes_data.to_csv('Datasets/letterboxd_data/themes.csv', index=False) 

    movies_data = pd.read_csv(movies_file_path)
    movies_data.to_csv('Datasets/letterboxd_data/lb_movies.csv', index=False) 

    for i in top_genres:
        filter_genre = genre_data[genre_data.iloc[:, 1] == i]
        filter_theme = themes_data[themes_data.iloc[:, 1].isin(g_t_dict[i])]
        key_column = filter_genre.columns[0]
        merged = pd.merge(filter_genre, filter_theme, on=key_column, how='inner')
        merged_movies = pd.merge(merged, movies_data, on=key_column, how='inner')
        filename = f"Datasets/letterboxd_data/merged_dataset_{user_name}{i}.csv"
        merged_movies.to_csv(filename, index=False)










