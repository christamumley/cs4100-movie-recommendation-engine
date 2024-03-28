# cs4100-movie-recommendation-engine

#Notes: 
    Some ideas for implementation: 
     -  For infering which genres certain movies fall under: Viterbi Algorithm, (basically we will be infering the most likely sequence of hidden states (genres) given observed sequences (movie descriptions)). After we know what genres the person's description is (assuming that in this implementation, the person types a description of a movie they'd want to watch), then we can go ahead and recommend movies that fall under that genre. This algorithm would be used when actually coming up with a recommendation, whereas the other algorithm (down below), is to train.


     - For training the hidden markov model itself: Baum-Welch algorithm. We would do so on a dataset of movie descriptions and genres, allowing the model to learn the transition and emission probabilities that best explain the observed data, this would allow the model to learn from data and improve its predictive accuracy over time.

     NOTE: we can include various types of hidden states such as: Genres, Age Rating, Languages, or Tropes etc.