import threading
## run gui
from GUI.chat_gui import run as run_gui
from GUI.chat_gui import get_root

root = get_root()

# kind of suspect to import from a thread but it makes the gui look nice 
def import_():
    # load model data
    root.event_generate("<<loading>>", when="tail")
    import chatbot.moviebot 
    chatbot.moviebot.load()
    root.event_generate("<<greet>>", when="tail")

import_thread = threading.Thread(target=import_)
import_thread.start()



def main():
    run_gui()
    # wait for the chatbot model to finish loading 
    import_thread.join() 


if __name__ == "__main__":
    main()