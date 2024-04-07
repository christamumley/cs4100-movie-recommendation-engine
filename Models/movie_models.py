import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def load():
    global tfidf_vectorizer
    global tfidf_matrix_summaries
    global movies_data_cleaned
    tfidf_vectorizer = pickle.load(open("Models\\saved_weights\\tfidf_vectorizer.pkl", 'rb'))
    tfidf_matrix_summaries = pickle.load(open("Models\\saved_weights\\tfidf_matrix_summaries.pkl", 'rb'))
    movies_data_cleaned = pd.read_csv("Models\\saved_weights\\movies_data_cleaned.csv")

def get_plot_keywords(plot):
    # vectorize the given plot 
    plot_tfidf = tfidf_vectorizer.transform([plot])
    feature_names = tfidf_vectorizer.get_feature_names_out()

    # retrieve the keyword importance for each word 
    scores = dict({(feature_names[i], plot_tfidf[0, i]) for i in plot_tfidf.indices})
    keywords = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [k[0] for k in keywords] 

def recommend_movies_based_on_input_plot(input_plot):
    plot_keywords = get_plot_keywords(input_plot)
    print(plot_keywords)
    input_vec = tfidf_vectorizer.transform([input_plot])
    cosine_sim = cosine_similarity(input_vec, tfidf_matrix_summaries)
    sim_scores = list(enumerate(cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movies_data_cleaned['title'].iloc[movie_indices]
