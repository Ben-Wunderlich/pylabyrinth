'''
graph code courtesy of https://www.bogotobogo.com/python/python_graph_data_structures.php

'''

from graph import Graph
import visualize
from random import shuffle, randint

def createGrid(width, height) -> int:#do more with this

    newGraph = Graph()
    for i in range(width):
        for j in range(height):
            if j != height-1:
                newGraph.add_edge((i,j),(i, j+1))
            if i != width-1:
                newGraph.add_edge((i,j),(i+1, j))
    return newGraph

def destructiveDfs(graph, startVertex):
    visited = set()
    removed = Graph()
    vertex_obj = graph.get_vertex(startVertex)
    destructiveDfsUtil(graph, vertex_obj, visited, removed)
    return removed

def destructiveDfsUtil(graph, nextVertex, visited, removed):
    visited.add(nextVertex)
    allNeighbors = list(nextVertex.get_connections())
    shuffle(allNeighbors)

    for neighbor in allNeighbors:
        if neighbor not in visited:
            removed.add_edge(nextVertex.get_id(), neighbor.get_id())
            destructiveDfsUtil(graph, neighbor, visited, removed)

def markCount(vertex1, vertex2, marked):
    i=0
    if vertex1.get_id() in marked:
        i+=1
    if vertex2.get_id() in marked:
        i+=1

    '''if vertex1 not in vertex2.get_connections():
        return -1'''
    
    return i

def primMaze(graph, width, height):
    # refer to https://en.wikipedia.org/wiki/Maze_generation_algorithm

    traversed = Graph()

    #start = (width//2,height//2)
    start = (width//2,0)
    marked = set([start])
    startvert =graph.get_vertex(start)
    neighbors = graph.get_vertex(start).get_connections()
    while len(neighbors) > 0:
        #print("I run")
        picked = neighbors.pop()

        #allNeighbors = list(picked.get_connections())
        #shuffle(allNeighbors)

        for newNeighbor in picked.get_connections():
            if markCount(picked, newNeighbor, marked) == 1:
                traversed.add_edge(picked.get_id(), newNeighbor.get_id())
                neighbors.update(picked.get_connections())
                if startvert in neighbors:#XXX why does it need
                    print("kill is")
                    neighbors.remove(startvert)#bug fixing
                break
        #neighbors.update(picked.get_connections())
        marked.add(picked.get_id())
    
    return traversed



def aldousBroder(graph, width, height):
    #also do this sometime
    # refer to https://en.wikipedia.org/wiki/Maze_generation_algorithm
    currCell = (randint(0, width-1),randint(0, height-1))
    visited = set()
    visited.add(currCell)
    unvisited = set(graph.get_vertices())

    while len(unvisited) > 0:
        pass



def main():
    #40x40 is pretty good
    WIDTH = 50
    HEIGHT = 50

    aslk= createGrid(WIDTH,HEIGHT)
    #print(aslk.get_vertices())
    pathes = primMaze(aslk, WIDTH, HEIGHT)
    #pathes = destructiveDfs(aslk, (randint(0, WIDTH-1),randint(0, HEIGHT-1)))

    #pathes = aslk
    visualize.display(pathes, WIDTH, HEIGHT)


if __name__ == "__main__":
    main()