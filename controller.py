import os
import sys
import threading
import numpy as np

# chatbot implementatipon
from chatbot.moviebot import get_label, get_default_responses

# movie model implmentation
from Models.movie_models import (
    recommend_movies_based_on_input_plot,
    recommend_movies_based_on_genre,
    recommend_movies_based_on_similarity,
)

def handle_msg(msg):
    label = get_label(msg)
    if label == "plot":
        return recommend_movies_based_on_input_plot(msg).to_string(index=False)
    elif label == "genre":
        return recommend_movies_based_on_genre(msg).to_string(index=False)
    elif label == "similar":
        return recommend_movies_based_on_similarity(msg).to_string(index=False)
    else:
        responses = get_default_responses() 
        if(label in responses.keys()):
            return np.random.choice(responses[label])
        else: 
            return "Sorry, I'm not sure I understand what you're looking for. Could you reword that?"
