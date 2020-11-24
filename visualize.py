from tkinter import *

master = Tk()

def addNodes(graph):
    pass
CIRCE_WIDTH = 4
OFFSET = 20
EXPAND=50
LINE_WIDTH = 30

def makeNode(w,x,y):
    x+=OFFSET
    y+=OFFSET
    w.create_oval(x,y,x+CIRCE_WIDTH,y+CIRCE_WIDTH, fill="#476042")

def makeConnection(w, p1, p2):
    p1 = (p1[0]*EXPAND+OFFSET+CIRCE_WIDTH/2, p1[1]*EXPAND+OFFSET+CIRCE_WIDTH/2)
    p2 = (p2[0]*EXPAND+OFFSET+CIRCE_WIDTH/2, p2[1]*EXPAND+OFFSET+CIRCE_WIDTH/2)
    w.create_line(p1[0], p1[1], p2[0], p2[1], width=LINE_WIDTH, fill="#23262b")

def display(graph, x, y):
    canvas_width = x*EXPAND+OFFSET*2
    canvas_height = y*EXPAND+OFFSET*2
    w = Canvas(master, 
            width=canvas_width+OFFSET*2,
            height=canvas_height+OFFSET*2)
    w.configure(bg='black')
    w.pack()

    allVertices = graph.get_vertices()
    #addedVertices= set()

    for vertex in allVertices:
        makeNode(w, vertex[0]*EXPAND, vertex[1]*EXPAND)
        for connected in graph.get_vertex(vertex).get_connections():
            makeConnection(w, vertex, connected.get_id())
        #addedVertices.add(vertex)

    #y = int(canvas_height / 2)


    mainloop()

    #print(graph.get_vertices())