from tkinter import *

canvas_width = 500
canvas_height = 150

def paint(event):
    python_green = "#476042"
    x1, y1  = (event.x - 1), (event.y - 1)
    x2, y2  = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1,x2,y2, fill=python_green)

root = Tk()
root.title("Paiting using ovals")
w = Canvas(root,
           width=canvas_width,
           height=canvas_height)

w.pack(expand=YES, fill=BOTH)
w.bind("<B1-Motion>", paint)

message = Label(root, text="Press and drag the mouse to draw")
message.pack()

root.mainloop()