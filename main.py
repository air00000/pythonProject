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

    bin_file = open("gir.txt", "w")
    for i in range(canvas_height):
        for j in range(canvas_width):
            bin_file.write(str(arr[i][j]))
        bin_file.write('\n')
    bin_file.close()


def paint(event):
    global brush_size
    global color
    x1 = event.x
    y1 = event.y

    x2 = event.x
    y2 = event.y
    w.create_rectangle(x1, y1, x2, y2)

    try:
        arr[y1][x1] = 1
    except IndexError:
        pass


def erase(event):
    global eraser_size
    global eraser
    x1 = event.x
    y1 = event.y
    x2 = event.x
    y2 = event.y
    w.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 0


root = Tk()
root.title("Paint")

w = Canvas(root, width=canvas_width, height=canvas_height, bg="white")

w.bind("<B1-Motion>", paint)
w.bind("<Button-1>", paint)
w.bind("<B3-Motion>", erase)
save_button = Button(text='Save')

save_button.bind("<Button-1>", save)

w.pack()
save_button.pack()
root.mainloop()
