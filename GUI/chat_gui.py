import tkinter
from tkinter import *
from PIL import ImageTk, Image
import customtkinter

# GUI for movie recommendation engine
# Chat bot

# basic version with tkinter created using
# https://medium.com/@vishwanathmuthuraman_92476/building-a-chatbot-with-python-and-tkinter-library-for-the-gui-390a747dadf6


# Function: given a user's inputted plot description and preferred genre, respond a certain way
def chat_response(genre_input):
    # Normalize the user's input
    # plot_input = plot_input.lower()
    genre_input = genre_input.lower()

    ## TO-DO: pass user input to model and get resulting output to return
    # response = f"Recommended Movie: {recommend_movie(plot_input, genre_input)}
    response = "Based on your preferences, I would recommend: "

    return response

### creating the GUI
root = customtkinter.CTk()
root.title("Movie Recommendation Chatbot")

# Logo
logo = Image.open("images\\logo.jpeg").resize((300, 100))
photo = ImageTk.PhotoImage(logo)
Button(
    root,
    image=photo,
).grid(row=0, columnspan=2, pady=(10, 0))

# Scrollbar
scrollbar = Scrollbar(root, orient="vertical")

# Chat text area
text_area = tkinter.Text(
    root,
    bg="white",
    fg="black",
    width=82,
    height=20,
    wrap="word",
    relief=FLAT,
    font=("Helvetica" + "bold"),
    yscrollcommand=scrollbar.set,
)
text_area.grid(row=1, columnspan=3)
text_area.yview_scroll

scrollbar.config(command=text_area.yview)
scrollbar.grid(row=1, column=3, sticky="ns")

# User input field:
genre_field = customtkinter.CTkEntry(root, corner_radius=3, width=325, exportselection=0)
genre_field.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky="news")
genre_field.bind("<Return>", (lambda event: send_message()))

# Enter button
# MUST attribute license 
# "https://www.flaticon.com/free-icons/paper-plane by smashicons"
send = customtkinter.CTkImage(light_image=Image.open("images\\plane.png"),
                              size=(32, 32))
button = customtkinter.CTkButton(master=root,
                                 fg_color=("#4995ff", "#4995ff"),  
                                 image=send,
                                 text="",
                                 corner_radius=10,
                                 width=50,
                                 height=50,
                                 command=lambda: send_message()).grid(row=3, column=2, pady=(10, 10), padx=(0,10))

# Letterboxd button
pic_lib = customtkinter.CTkImage(light_image=Image.open("images\\lb.png"), 
                            size=(114, 50))
lb_button = customtkinter.CTkButton(
    root,
    text="",
    image=pic_lib,
    compound=BOTTOM,
    command=lambda: letterbox_connect(),
    width= 114, 
    height=50,
    corner_radius= 0,
    fg_color= 'black',
    hover_color = '#6e6e6e'
).grid(row=3, column=0, pady=(10, 10), padx=(10,0))

# text config for chat labels
text_area.tag_configure(
    "boldtextuser",
    background="#4995ff",
    font=("Helvetica" + "bold"),
    foreground="white",
)
text_area.tag_configure(
    "boldtextbot",
    background="#d30000",
    font=("Helvetica" + "bold"),
    foreground="white",
)

# text config for chat content
text_area.tag_configure("hang", lmargin1=106, lmargin2=106, rmargin=20)
text_area.config(spacing1=5)
text_area.config(spacing2=5)
text_area.config(spacing3=5)

# Displaying greeting text
text_area.insert(tkinter.END, f"\n   ")
text_area.insert(tkinter.END, f"  FLIX Rec:  ", "boldtextbot")
text_area.insert(
    tkinter.END,
    f"\t Hi! Welcome to the FLIX Rec Movie Recommendation Engine.\n"
    + f"Please enter a short plot description of a movie you would like to see, "
    + f"along with preferred genre, "
    + f"or click the button below to connect your Letterboxd for a personalized recommendation!",
    "hang",
)

# Displaying button
text_area.window_create(END, window=lb_button, padx=200, pady=20)
text_area.config(state=DISABLED)

# Function: send message
def send_message():
    # Get user input
    # plot_input = plot_field.get()
    genre_input = genre_field.get()

    # Clear input fields
    # plot_field.delete(0, tkinter.END)
    genre_field.delete(0, tkinter.END)

    # Create response
    response = chat_response(genre_input)

    # Display response
    ## TO-DO: format this how we want
    text_area.config(state=NORMAL)
    text_area.insert(tkinter.END, f"\n   ")
    text_area.insert(tkinter.END, f"      User:     ", "boldtextuser")
    text_area.insert(
        tkinter.END,
        f"\t Plot description: \nPreferred genre: \n\n",
        "hang",
    )
    text_area.insert(tkinter.END, f"   ")
    text_area.insert(tkinter.END, f"  FLIX Rec:  ", "boldtextbot")
    text_area.insert(tkinter.END, f"\t {response}\n", "hang")
    text_area.insert(
        tkinter.END, f"\nFeel free to ask for another recommendation!\n\n", "hang"
    )
    text_area.config(state=DISABLED)
    text_area.see(tkinter.END)


# Function: TO-DO connect Letterboxd
def letterbox_connect():
    return

# open at the center of the screen 
root.eval('tk::PlaceWindow . center')
root.configure(fg_color='#303030')

root.mainloop()
