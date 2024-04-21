
# FlixREC: A Movie Recommendation Chatbot
### Created by: Thanoshi Balasuriya, Christa Mumley, Smita Rosemary, and Gauri Sarin
### Northeastern University | CS4100: Artificial Intelligence
---

## Setup 
### Without retraining the chatbot model: 
1. Go to [this Google Drive folder](https://drive.google.com/drive/folders/114bY8i-pJH59j-rHaaZ6ZdVGhBz0KXaY?usp=sharing)
2. Download the zipped "data" file. Unzip into cs4100-movie-recommendation-engine/chatbot/data 
3. Download the zipped "movie_model_data" file. Unzip into cs4100-movie-recommendation-engine/Models/saved_weights 

### With training the chatbot model: 
Open terminal > cd to \chatbot > run `TrainChatbot.py` 

Note: re-training may not work if you don't have pytorch cuda enabled. 

This trains question intents from `intents.json`. If you want to add tags/fine-tune the intents, change that file. 

## Running the program: 
Open a terminal window in the root folder (/cs4100-movie-recommendation-engine) 

Run: `python main.py`

---

### File Organization:
`Chatbot` - files related to training the Chatbot, using BERT

`Datasets` - .csv files of data

`GUI` - files related to the graphical UI

`Models` - files related to the actual recommendation models. `Models/Jupyter Notebooks` is a folder of the original notebooks used to create the models

`controller.py` - handles the input and directs program to right action/recommendation model

`main.py` - runs the Chatbot from the terminal

---

#### General Notes 
* Loading the program may take a little while
* Some file paths are currently in MacOS format: for Windows, in `GUI/chat_gui.py`, replace `/` with `\\` in the file paths
* Jupyter Notebooks (seen in `Models/Jupyter Notebooks`) are where we brainstormed/fleshed out our ideas - the file paths within are not currently accurate (you will run into errors attempting to run the notebooks)