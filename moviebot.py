from transformers import BertForSequenceClassification, BertTokenizerFast
from transformers import pipeline
import os 

MODEL_PATH = "chatbot"

############# ENSURE PARENT DIRECTORY #######
current_directory = os.getcwd().split('\\')[-1]
if (current_directory != 'cs4100-movie-recommendation-engine'):
    os.chdir('..')

############## LOAD MODEL ###################
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer= BertTokenizerFast.from_pretrained(MODEL_PATH)
chatbot = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# re-set dir
os.chdir(current_directory)

def get_label(user_text):
    '''
    Gets the action label of the given text
    '''
    user_text = user_text.lower().strip()
    label, score = chatbot(user_text)[0].values() 
    if(score < .7):
        return "unknown"
    else: 
        return label

