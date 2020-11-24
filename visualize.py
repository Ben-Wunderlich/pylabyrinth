from tkinter import *

master = Tk()

CIRCE_WIDTH = 4
EXPAND=22
OFFSET = EXPAND
LINE_WIDTH = int(EXPAND*0.6)

def makeNode(w,x,y):
    x+=OFFSET
    y+=OFFSET
    w.create_oval(x,y,x+CIRCE_WIDTH,y+CIRCE_WIDTH, fill="#476042")

def makeConnection(w, p1, p2):
    p1 = (p1[0]*EXPAND+OFFSET+CIRCE_WIDTH/2, p1[1]*EXPAND+OFFSET+CIRCE_WIDTH/2)
    p2 = (p2[0]*EXPAND+OFFSET+CIRCE_WIDTH/2, p2[1]*EXPAND+OFFSET+CIRCE_WIDTH/2)
    w.create_line(p1[0], p1[1], p2[0], p2[1], width=LINE_WIDTH, fill="#B5DDFF")

def display(graph, x, y):
    canvas_width = x*EXPAND
    canvas_height = y*EXPAND
    w = Canvas(master, 
            width=canvas_width+OFFSET*2,
            height=canvas_height+OFFSET*2)
    w.configure(bg='#7414FA')
    w.pack()

    allVertices = graph.get_vertices()

    for vertex in allVertices:
        makeNode(w, vertex[0]*EXPAND, vertex[1]*EXPAND)
        for connected in graph.get_vertex(vertex).get_connections():
            makeConnection(w, vertex, connected.get_id())
        #addedVertices.add(vertex)

    #y = int(canvas_height / 2)


    mainloop()

    #print(graph.get_vertices())