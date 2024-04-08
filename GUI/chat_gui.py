import tkinter 
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter

import os
import sys
import threading
# import chatbot
sys.path.append(os.path.abspath('..'))
from Models.collect_letterboxdata import collect_letterboxd_data
from controller import handle_msg

# basic version with tkinter created using
# https://medium.com/@vishwanathmuthuraman_92476/building-a-chatbot-with-python-and-tkinter-library-for-the-gui-390a747dadf6

# Function: TO-DO connect Letterboxd
def letterbox_connect():
    popup_window = tkinter.Toplevel(root)
    popup_window.title("Connect Letterboxd")

    icon = Image.open("GUI\\images\\foldericon.jpg").resize((150, 140))
    folder_icon = ImageTk.PhotoImage(icon)
    label_icon = tkinter.Label(popup_window, image=folder_icon)
    label_icon.image = folder_icon  # Keep a reference to the image
    label_icon.pack()

    label_username = tkinter.Label(popup_window, text="Enter your username:")
    label_username.pack()

    # Add an entry widget for the user to input their username
    entry_username = tkinter.Entry(popup_window)
    entry_username.pack()

        # Function to handle when the user clicks the "Submit" button
    def submit_username():
        username = entry_username.get()
        if username:
            popup_window.destroy()
            text_area.config(state=NORMAL)
            text_area.insert(tkinter.END, f"\n   ")
            text_area.insert(tkinter.END, f"  FLIX Rec:  ", "boldtextbot")
            text_area.insert(
                tkinter.END,
                f"\t Collecting data for Username: '{username}'...",
                "hang",)
            text_area.config(state=DISABLED)
            collect_letterboxd_data(username)
        else:
            messagebox.showerror("Error", "Please enter a username.")

    # Add a button to submit the username
    button_submit = tkinter.Button(popup_window, text="Submit", command=submit_username)
    button_submit.pack()



################################################## GUI DEFINITION #############################
root = customtkinter.CTk()
root.title("Movie Recommendation Chatbot")

# Logo
logo = Image.open("GUI\\images\\logo.jpeg").resize((300, 100))
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
user_field = customtkinter.CTkEntry(root, corner_radius=3, width=325, exportselection=0)
user_field.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky="news")
user_field.bind("<Return>", (lambda event: send_message()))

# Enter button
# MUST attribute license 
# "https://www.flaticon.com/free-icons/paper-plane by smashicons"
send = customtkinter.CTkImage(light_image=Image.open("GUI\\images\\plane.png"),
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
pic_lib = customtkinter.CTkImage(light_image=Image.open("GUI\\images\\lb.png"), 
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

# Displaying greeting/loading text
#loading_message()

# Displaying button
text_area.window_create(END, window=lb_button, padx=200, pady=20)
text_area.config(state=DISABLED)

# open at the center of the screen 
root.eval('tk::PlaceWindow . center')
root.configure(fg_color='#303030')

###################################### TKINTER FUNCTIONS #########################################
def get_root():
    return root 

# Function: given a user's inputted plot description and preferred genre, respond a certain way
def chat_response(user_input):
    # Normalize the user's input
    user_input = user_input.lower()
    response = handle_msg(user_input)

    return response

def loading_message(_):
    text_area.config(state=NORMAL)
    text_area.insert(tkinter.END, f"\n   ")
    text_area.insert(tkinter.END, f"  FLIX Rec:  ", "boldtextbot")
    text_area.insert(
        tkinter.END,
        f"\t One second, data is still loading...",
        "hang",
    )
    text_area.config(state=DISABLED)


def greeting_message(_):

    text_area.config(state=NORMAL)
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
    text_area.config(state=DISABLED)


# Function: send message
def send_message():
    # Get user input
    user_input = user_field.get()

    # Clear input fields
    user_field.delete(0, tkinter.END)

    # Create response
    response = chat_response(user_input)

    # Display response
    ## TO-DO: format this how we want
    text_area.config(state=NORMAL)
    text_area.insert(tkinter.END, f"\n   ")
    text_area.insert(tkinter.END, f"      User:     ", "boldtextuser")
    text_area.insert(
        tkinter.END,
        f"\t {user_input}\n",
        "hang",
    )
    text_area.insert(tkinter.END, f"   ")
    text_area.insert(tkinter.END, f"  FLIX Rec:  ", "boldtextbot")
    text_area.insert(tkinter.END, f"\t {response}\n", "hang")
    # text_area.insert(
    #     tkinter.END, f"\nFeel free to ask for another recommendation!\n\n", "hang"
    # )
    text_area.config(state=DISABLED)
    text_area.see(tkinter.END)

def doFoo(*args):
    print("Hello, world")

############################# EVENTS TO BE CALLED FROM MAIN ####################

root.bind("<<loading>>", loading_message)
root.bind("<<greet>>", greeting_message)

############################## run func #########################################
def run(): 
    root.mainloop()
