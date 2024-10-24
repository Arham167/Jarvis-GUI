import PIL, requests
from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO

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
    
    root.mainloop()

if __name__ == "__main__":
    main()