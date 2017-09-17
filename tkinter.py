from Tkinter import *
import tkMessageBox
import Tkinter
from Pillow import ImageTk, Image

root = Tkinter.Tk()
root.title("Qweet")
root.geometry("500x300")

img = ImageTk.PhotoImage(Image.open("QweetsLogo.png"))


imglabel = Label(app_root, image=img).grid(row=1, column=1)

Lbl1 = Label(root, text="Input username here (ommit the @):")
Lbl1.pack(side=TOP,padx=5,pady=5)
Entry1 = Entry(root, bd =1)
Entry1.pack(side=TOP,padx=5,pady=5)
Lbl2 = Label(root, text="Input a tweet ID here:")
Lbl2.pack(side=TOP,padx=5,pady=5)
Entry2 = Entry(root, bd =1)
Entry2.pack(side=TOP,padx=5,pady=5)
Lbl3 = Label(root, text="Input a Keyword here:")
Lbl3.pack(side=TOP,padx=5,pady=5)
Entry3 = Entry(root, bd =1)
Entry3.pack(side=TOP,padx=5,pady=5)

def PrintCommand():
    reply = str(Entry1.get())
    replyID = str(Entry2.get())
    keyword = str(Entry3.get())
    print reply
    print replyID
    print keyword

bttn1 = Tkinter.Button(root, text ="Tweet!", command = PrintCommand)
bttn1.pack(side = TOP,padx=10,pady=20)

root.mainloop()
