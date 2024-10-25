import PIL, requests, users
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
    canvas.create_text(w/1.95, h/5, 
                       text = "Enter Username & Password", 
                       font = ("Lucida Fax", int(w/38)),
                       fill = "white")
    user_area = Entry(canvas,
                    font = ("Lucida Fax", int(w/38)))
    user_area.place(x = int (w/3.5), y = int(h/3))
    username = user_area.get()
    pwd_area = Entry(canvas,
                    font = ("Lucida Fax", int(w/38)))
    pwd_area.place(x = int (w/3.5), y = int(h/2))
    pwd = pwd_area.get()
    bt1 = Button(canvas,
                 text = "Sign In",
                 font = ("Arial Greek", int(w/80)),
                 cursor = "mouse",
                 command = partial(user_auth, username, pwd))
    bt1.place(x = int (w/3.5), y = int(h/1.5))
    
    root.mainloop()

def user_auth(username, pwd):
    print(users.auth_users)
    if username and pwd in users.auth_users:
        print("ok")
    else:
        print("no")

if __name__ == "__main__":
    main()