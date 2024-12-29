import PIL, shelve, pyttsx3, os
from tkinter import *
from PIL import ImageTk, Image
from functools import partial

# initialize the speaking engine
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty(rate, 100)

# initialize the main screen
root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.title("J.A.R.V.I.S.")
root.geometry("%dx%d" % (w, h))
root.configure(bg = "black")

# Changing the title bar look
root.overrideredirect(True)
title_bar = Frame(root, 
                  bg = "black")
title_bar.pack(fill = "x")
title_label = Label(title_bar, 
                    text = "J.A.R.V.I.S.", 
                    bg = "black", fg = "white",
                    font = ("Tahoma", 20))
title_label.pack()
closebutton = Button(title_bar,
                     text = "X",
                     bg = "snow", fg = "black",
                     cursor = "mouse",
                     relief = "flat",
                     width = 4,
                     command= root.quit)
closebutton.place(x = int(w/1.03), y = int(w/270))


# Open the image, resize it and display it
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "assets", "bg.jpg")
image = Image.open(image_path)
resized = image.resize((w, h), PIL.Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(resized)



canvas = Canvas(root, width = w, height = h) 
canvas.pack(side = "bottom") 
canvas.create_image(1, 1, anchor = NW, image = img)

def main():
    # global variables to destroy them later in the program
    global user_area
    global pwd_area
    global signin_bt
    global signup_bt

    canvas.create_text(w/1.95, h/5,                         # starting text
                       text = "Enter Username & Password", 
                       font = ("Tahoma", int(w/38)),
                       fill = "white",
                       tag = "first_win")
    user_area = Text(canvas,                                # username input field
                     height = 1,
                     width = int(w/70),
                    font = ("Tahoma", int(w/38)))
    user_area.place(x = int (w/3.2), y = int(h/3))
    pwd_area = Text(canvas,                                 # password input field
                    height = 1,
                    width = int(w/70),
                    font = ("Tahoma", int(w/38)))
    pwd_area.place(x = int (w/3.2), y = int(h/2))

    signin_bt = Button(canvas,                              # sign in button
                 text = "Sign In",                  
                 font = ("Tahoma", int(w/80)),
                 cursor = "mouse",
                 command = user_auth)
    signin_bt.place(x = int (w/3.2), y = int(h/1.5))
    signup_bt = Button(canvas,                              # sign up button
                 text = "New? Sign Up",
                 font = ("TahomaS", int(w/80)),
                 cursor = "mouse",
                 command = user_ask)
    signup_bt.place(x = int (w/1.7), y = int(h/1.5))
    
    root.mainloop()

# function called when the sign in button is clicked, checking if correct username and password are entered
def user_auth():
    global username                                         # global so it can be called in the next window
    username = user_area.get("1.0", "end-1c")               # getting the username as text from the input
    pwd = pwd_area.get("1.0", "end-1c")                     # getting the password as text from the input

    with shelve.open("users") as db:                        # opening the database of all users and passwords
        if username in db:
            if pwd == db[username]:
                second_win()                                # opening the main window if the username and password match
            else:                                           # error if password wrong
                new_win = Toplevel()
                new_win.geometry("%dx%d+%d+%d" % (w/2.5, h/11, w/3.2, h/2.5))
                lb = Label(new_win,
                       text = "Wrong Password. Try Again.",
                       font = ("Tahoma", int(w/50)))
                lb.place(x = int(w/70), y = int(h/100))
        else:                                               # error if username wrong
                new_win = Toplevel()
                new_win.geometry("%dx%d+%d+%d" % (w/2.5, h/11, w/3.2, h/2.5))
                lb = Label(new_win,
                       text = "Wrong Username. Try Again.",
                       font = ("Tahoma", int(w/50)))
                lb.place(x = int(w/70), y = int(h/100))

# function called if the sign up button is clicked, opening a window to add username and password
def user_ask():
    new_win = Toplevel(root)
    new_win.geometry("%dx%d+%d+%d" % (w/2.5, h/1.5, w/3.2, h/6))

    # making a modal window so all don't close
    new_win.transient(root)
    new_win.grab_set()
    new_win.focus_set()

    newuser_label = Label(new_win,                          # text labeling username area
                       text = "Username: ",
                       font = ("Tahoma", int(w/38)))
    newuser_label.place(x = int(w/80), y = int(h/6))
    newuser_area = Text(new_win,                            # area for entering username
                     height = 1,
                     width = int(w/180),
                    font = ("Tahoma", int(w/38)))
    newuser_area.place(x = int (w/4.8), y = int(h/6))
    newpwd_label = Label(new_win,                           # text labeling password area
                       text = "Password: ",
                       font = ("Tahoma", int(w/38)))
    newpwd_label.place(x = int(w/80), y = int(h/3))
    newpwd_area = Text(new_win,                             # area for entering password
                    height = 1,
                    width = int(w/180),
                    font = ("Tahoma", int(w/38)))
    newpwd_area.place(x = int (w/4.8), y = int(h/3))

    bt1 = Button(new_win,                                   # button to add user
                 text = "Enter",
                 font = ("Arial Greek", int(w/80)),
                 cursor = "mouse",
                 command = partial(user_add, newuser_area, newpwd_area))
    bt1.place(x = int (w/6), y = int(h/2))

# function to add user
def user_add(newuser_area, newpwd_area):
    username = newuser_area.get("1.0", "end-1c")            # getting username as text from input
    pwd = newpwd_area.get("1.0", "end-1c")                  # getting password as text from input

    with shelve.open("users") as db:                        # opening the database of all users
        if username not in db:
            db[username] = pwd                              # if user does not already exist, add the                                                         
            message("User added. Please sign in.")          # username as key and password as value
        else:
            message("That user already exists.")

# function to display a message after user is added (or not). this whole thing is a modal window
def message(msg):
    msg_win = Toplevel(root)
    msg_win.geometry("%dx%d+%d+%d" % (w/2.5, h/11, w/3.2, h/2.5))
    msg_win.transient(root)
    msg_win.grab_set()
    msg_win.focus_set()

    lb = Label(msg_win,
                text = msg,
                font = ("Tahoma", int(w/50)))
    lb.place(x = int(w/70), y = int(h/100))

# new window opened if the user is authorized
def second_win():
    # delete all the previous text, fields and buttons
    canvas.delete("first_win")
    user_area.destroy()
    pwd_area.destroy()
    signin_bt.destroy()
    signup_bt.destroy()

    canvas.create_text(w/1.95, h/5,                         # Welcome text
                       text = "Welcome " f"{username}", 
                       font = ("Tahoma", int(w/20)),
                       fill = "white")
    engine.say("Welcome " f"{username}")
    engine.runAndWait()

if __name__ == "__main__":
    main()