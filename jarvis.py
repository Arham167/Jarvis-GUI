import PIL, requests, users, shelves
from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO
from functools import partial

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
                    font = ("Lucida Fax", 20))
title_label.pack()
closebutton = Button(title_bar,
                     text = "X",
                     bg = "snow", fg = "black",
                     cursor = "mouse",
                     relief = "flat",
                     width = 4,
                     command= root.quit)
closebutton.place(x = int(w/1.03), y = int(w/270))
minbutton = Button(title_bar,
                     text = "-",
                     bg = "snow", fg = "black",
                     cursor = "mouse",
                     relief = "flat",
                     width = 4,
                     command= root.withdraw)
minbutton.place(x = int(w/5), y = int(w/270))


# Open the image, resize it and display it
image_url = "https://i.pinimg.com/originals/90/e1/c2/90e1c21fa935d4f507dbb6cd1ebc8ef5.jpg"
data = requests.get(image_url)
image = Image.open(BytesIO(data.content))
resized = image.resize((w, h), PIL.Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(resized)

canvas = Canvas(root, width = w, height = h) 
canvas.pack(side = "bottom") 
canvas.create_image(1, 1, anchor = NW, image = img)

def main():
    global user_area
    global pwd_area
    canvas.create_text(w/1.95, h/5, 
                       text = "Enter Username & Password", 
                       font = ("Lucida Fax", int(w/38)),
                       fill = "white")
    user_area = Text(canvas,
                     height = 1,
                     width = int(w/70),
                    font = ("Lucida Fax", int(w/38)))
    user_area.place(x = int (w/3.5), y = int(h/3))
    pwd_area = Text(canvas,
                    height = 1,
                    width = int(w/70),
                    font = ("Lucida Fax", int(w/38)))
    pwd_area.place(x = int (w/3.5), y = int(h/2))
    bt1 = Button(canvas,
                 text = "Sign In",
                 font = ("Arial Greek", int(w/80)),
                 cursor = "mouse",
                 command = user_auth)
    bt1.place(x = int (w/3), y = int(h/1.5))
    bt2 = Button(canvas,
                 text = "New? Sign Up",
                 font = ("Arial Greek", int(w/80)),
                 cursor = "mouse",
                 command = user_ask)
    bt2.place(x = int (w/1.7), y = int(h/1.5))
    
    root.mainloop()

def user_auth():
    username = user_area.get("1.0", "end-1c")
    print(username)
    pwd = pwd_area.get("1.0", "end-1c")
    print(pwd)

    if username in users.auth_users:
        print("ok")
        if pwd == users.auth_users.get(username):
            print("ok")
        else:
            print("wrong pwd")
    else:
        print("wrong username")

def user_ask():
    new_win = Toplevel()
    new_win.geometry("%dx%d+%d+%d" % (w/2.5, h/1.5, w/3.2, h/6))
    global newuser_area
    global newpwd_area

    newuser_label = Label(new_win,
                       text = "Username: ",
                       font = ("Lucida Fax", int(w/38)))
    newuser_label.place(x = int(w/80), y = int(h/6))
    newuser_area = Text(new_win,
                     height = 1,
                     width = int(w/180),
                    font = ("Lucida Fax", int(w/38)))
    newuser_area.place(x = int (w/4.8), y = int(h/6))
    newpwd_label = Label(new_win,
                       text = "Password: ",
                       font = ("Lucida Fax", int(w/38)))
    newpwd_label.place(x = int(w/80), y = int(h/3))
    newpwd_area = Text(new_win,
                    height = 1,
                    width = int(w/180),
                    font = ("Lucida Fax", int(w/38)))
    newpwd_area.place(x = int (w/4.8), y = int(h/3))

    bt1 = Button(new_win,
                 text = "Enter",
                 font = ("Arial Greek", int(w/80)),
                 cursor = "mouse",
                 command = user_add)
    bt1.place(x = int (w/6), y = int(h/2))

def user_add():
    username = newuser_area.get("1.0", "end-1c")
    pwd = newpwd_area.get("1.0", "end-1c")
    print(users.auth_users)

    if username or pwd not in users.auth_users:
        key = username
        value = pwd
        users.auth_users.update({key: value})

    print(users.auth_users)

if __name__ == "__main__":
    main()