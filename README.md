# cs4100-movie-recommendation-engine

#Notes: 
    Some ideas for implementation: 
     -  For infering which genres certain movies fall under: Viterbi Algorithm, (basically we will be infering the most likely sequence of hidden states (genres) given observed sequences (movie descriptions)). After we know what genres the person's description is (assuming that in this implementation, the person types a description of a movie they'd want to watch), then we can go ahead and recommend movies that fall under that genre. This algorithm would be used when actually coming up with a recommendation, whereas the other algorithm (down below), is to train.


     - For training the hidden markov model itself: Baum-Welch algorithm. We would do so on a dataset of movie descriptions and genres, allowing the model to learn the transition and emission probabilities that best explain the observed data, this would allow the model to learn from data and improve its predictive accuracy over time.

     NOTE: we can include various types of hidden states such as: Genres, Age Rating, Languages, or Tropes etc.

main.py:
Entry point of the application.
Handles user input and interaction.
Orchestrates the workflow of the recommendation system.

text_processor.py:
Contains classes or functions for preprocessing the user's input text.
Handles tokenization, stopwords removal, stemming, lemmatization, and other text cleaning tasks.
Provides methods for extracting key plot words and other features from the input text.

genre_classifier.py:
Implements a classifier for predicting movie genres based on text features extracted from the user's input.
Uses machine learning models or rule-based approaches to classify the input text into relevant genres.

keyword_extractor.py:
Implements algorithms for extracting keywords or phrases indicative of movie genres, plot points, and themes from the user's input.
Provides methods for identifying and ranking key plot words and other relevant features.


trope_analyzer.py:
Contains classes or functions for analyzing and extracting the tropes found in the user's input text.
Implement algorithms to scan movie descriptions for occurrences of keywords, phrases, or patterns associated with the tropes in your database.
Use techniques like regular expressions, keyword matching, or machine learning models trained on labeled data to identify tropes in the text.

Tropes Analyzer Module:

Create a module or class responsible for trope analysis.
This module should take the movie description as input and output a list of tropes present in the description along with their relevance scores or confidence levels.

sentiment_analyzer.py:
Contains classes or functions for analyzing the sentiment of the user's input text.
Implements sentiment analysis algorithms to determine the overall sentiment (positive, negative, neutral) of the input text.

movie_database.py:
Manages a database or dataset of movies, including information such as titles, genres, descriptions, ratings, etc.
Provides methods for querying and retrieving movie data based on genres, keywords, or other criteria.

recommendation_engine.py:
Implements the recommendation engine, which generates movie recommendations based on the extracted features from the user's input.
Combines information from genre classification, keyword extraction, sentiment analysis, and movie database queries to recommend relevant movies.

hmm.py:
Contains classes and functions for implementing Hidden Markov Models (HMMs).
Implements algorithms such as the Viterbi algorithm for inference and the Baum-Welch algorithm for training.
Provides methods for training an HMM on movie description data and using the trained model for genre prediction.

user_interface.py:
Contains classes or functions for presenting movie recommendations to the user.
Handles formatting and displaying recommendations in a user-friendly manner, such as through a graphical user interface (GUI) or command-line interface (CLI).

utils.py:
Contains utility functions or classes used across multiple modules, such as file I/O operations, logging, and miscellaneous helper functions.