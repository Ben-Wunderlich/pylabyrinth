'''
graph code courtesy of https://www.bogotobogo.com/python/python_graph_data_structures.php

'''

from graph import Graph
import visualize
from random import shuffle

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
            #print(neighbor)
            #nextVertex.remove_connection(neighbor)
            removed.add_edge(nextVertex.get_id(), neighbor.get_id())
            destructiveDfsUtil(graph, neighbor, visited, removed)

def nowDestroy(graph, toDestroy):
    for ptPair in toDestroy:
        graph.remove_edge(ptPair[0], ptPair[1])

def main():
    WIDTH = 30
    HEIGHT = 15

    aslk= createGrid(WIDTH,HEIGHT)
    #visualize.display(aslk, 5,5)
    #print(aslk.get_vertices())
    res = destructiveDfs(aslk, (0,0))
    #nowDestroy(aslk, res)

    #print(res)
    visualize.display(res, WIDTH, HEIGHT)


if __name__ == "__main__":
    main()