import tkinter

# GUI for movie recommendation engine
# Chat bot

# basic version with tkinter created using
# https://medium.com/@vishwanathmuthuraman_92476/building-a-chatbot-with-python-and-tkinter-library-for-the-gui-390a747dadf6


# Function: given a user's inputted plot description and preferred genre, respond a certain way
def chat_response(plot_input, genre_input):
    # Normalize the user's input
    plot_input = plot_input.lower()
    genre_input = genre_input.lower()

    ## TO-DO: pass user input to model and get resulting output to return
    # response = f"Recommended Movie: {recommend_movie(plot_input, genre_input)}
    response = "Recommended Movie: "

    return response


### creating the GUI

root = tkinter.Tk()
root.title("Movie Recommendation Chatbot")

# Text area
text_area = tkinter.Text(root, bg="white", fg="black", width=50, height=20, wrap="word")

text_area.grid(row=0, columnspan=2)

# User input field: Plot
plot_label = tkinter.Label(root, text="Plot description: ")
plot_label.grid(row=2, column=0)
plot_field = tkinter.Entry(root, width=50, exportselection=0)
plot_field.grid(row=2, column=1)


# User input field: Genre
genre_label = tkinter.Label(root, text="Preferred genre: ")
genre_label.grid(row=3, column=0)
genre_field = tkinter.Entry(root, width=50, exportselection=0)
genre_field.grid(row=3, column=1)

# Send button
send_button = tkinter.Button(root, text="Send", command=lambda: send_message()).grid(
    row=4
)

# Displaying greeting text
## TO-DO: format this how we want
text_area.insert(
    tkinter.END,
    f"Chatbot: Hi! Welcome to the Movie Recommendation Engine. Please enter a short plot description of a movie you would like to see or connect your Letterboxd for a personalized recommendation!\n\n",
)


# Function: send message
def send_message():
    # Get user input
    plot_input = plot_field.get()
    genre_input = genre_field.get()

    # Clear input fields
    plot_field.delete(0, tkinter.END)
    genre_field.delete(0, tkinter.END)

    # Create response
    response = chat_response(plot_input, genre_input)

    # Display response
    ## TO-DO: format this how we want
    text_area.insert(tkinter.END, f"User: {plot_input}\n\n")
    text_area.insert(tkinter.END, f"Chatbot: {response}\n\n")


root.mainloop()
