from tkinter import *

master = Tk()

#CIRCE_WIDTH = 4
expand=offset=line_width= half_width=-1

def makeNode(w,x,y):
    x+=offset
    y+=offset
    #w.create_oval(x,y,x+CIRCE_WIDTH,y+CIRCE_WIDTH, fill="#476042")

def makeConnection(w, p1, p2):
    p1 = (p1[0]*expand+offset, p1[1]*expand+offset)
    p2 = (p2[0]*expand+offset, p2[1]*expand+offset)
    #w.create_line(p1[0]+half_width, p1[1]+half_width, p2[0], p2[1], width=line_width, fill="#B5DDFF")
    #it looks really cool if you use above line

    if(p1[0] == p2[0]):
        w.create_line(p1[0], p1[1]-half_width, p2[0], p2[1]+half_width, width=line_width, fill="#B5DDFF")
    else:
        w.create_line(p1[0]-half_width, p1[1], p2[0]+half_width, p2[1], width=line_width, fill="#B5DDFF")


def updateExpand(newExpand):
    global expand, offset, line_width, half_width
    expand = newExpand
    offset = newExpand
    line_width = int(expand*0.6)
    half_width = line_width//2


def display(graph, x, y, newExpand):
    updateExpand(newExpand)
    canvas_width = x*expand
    canvas_height = y*expand
    w = Canvas(master, 
            width=canvas_width+offset*2,
            height=canvas_height+offset*2)
    w.configure(bg='#7414FA')
    w.pack()

    allVertices = graph.get_vertices()

    for vertex in allVertices:
        makeNode(w, vertex[0]*expand, vertex[1]*expand)
        for connected in graph.get_vertex(vertex).get_connections():
            makeConnection(w, vertex, connected.get_id())
        #addedVertices.add(vertex)

    #y = int(canvas_height / 2)


    mainloop()

    #print(graph.get_vertices())