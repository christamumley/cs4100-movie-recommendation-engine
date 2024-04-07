# cs4100-movie-recommendation-engine
### Setup 
#### Without retraining the chatbot model: 
1. Go to the shared folder
2. download the zipped "chatbot_data" file. Unzip into cs4100-movie-recommendation-engine/chatbot/data 
3. download the zipped "movie_model_data" file. Unzip into cs4100-movie-recommendation-engine/Models/saved_weights 
#### With training the chatbot model: 
open terminal > cd to \chatbot > run `TrainChatbot.py` 

Note: re-training may not work if you don't have pytorch cuda enabled. 

This trains question intents from `intents.json`. If you want to add tags/fine-tune the intents, change that file. 

### Running the program: 
open a terminal window in the root folder (/cs4100-movie-recommendation-engine) 

Run: `python main.py`
