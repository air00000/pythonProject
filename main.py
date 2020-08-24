from tkinter import *

k = 4
canvas_width = 256 * k
canvas_height = 8 * k
brush_size = 1
eraser_size = 1
color = "black"
eraser = "white"
arr = [[0] * canvas_width for i in range(canvas_height)]

def save(event):
    binf = open("gir.txt", "wt")
    i = 0
    j = 0
    for i in range(canvas_height):
        for j in range(canvas_width):
            binf.write(str(arr[i][j]))
    binf.close()

def paint(event):
    global brush_size
    global color
    x1 = event.x
    y1 = event.y

    x2 = event.x
    y2 = event.y
    w.create_rectangle(x1, y1, x2, y2)
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

def erase(event):
    global eraser_size
    global eraser
    x1 = event.x
    y1 = event.y
    x2 = event.x
    y2 = event.y
    w.create_rectangle(x1, y1, x2, y2, fill = "white", outline = "white")
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 0

root = Tk()
root.title("Paint")

w = Canvas(root, width=canvas_width, height=canvas_height, bg="white")

w.bind("<B1-Motion>", paint)
w.bind("<Button-1>", paint)
w.bind("<B3-Motion>", erase)
w.bind("<space>", save)

w.pack()

root.mainloop()
