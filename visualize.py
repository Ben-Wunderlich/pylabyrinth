from tkinter import *

master = Tk()


def display(graph, x, y):
    canvas_width = x*10
    canvas_height = y*10
    w = Canvas(master, 
            width=canvas_width,
            height=canvas_height)
    w.pack()

    y = int(canvas_height / 2)
    w.create_line(0, y, canvas_width, y, fill="#476042")


    mainloop()

    #print(graph.get_vertices())