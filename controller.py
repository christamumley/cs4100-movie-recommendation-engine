import os
import sys
import threading

# chatbot implementatipon 
from chatbot.moviebot import get_label
# movie model implmentation 
from Models.movie_models import recommend_movies_based_on_input_plot




##########################################
#    NEEDS to be implemented
##########################################

def handle_msg(msg): 
    label = get_label(msg) 
    if(label == "plot"):
        return recommend_movies_based_on_input_plot(msg)
    else:
        return label 