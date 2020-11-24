'''
graph code courtesy of https://www.bogotobogo.com/python/python_graph_data_structures.php

'''

from graph import Graph
import visualize
from copy import deepcopy

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
    toRemove = set()
    vertex_obj = graph.get_vertex(startVertex)
    destructiveDfsUtil(graph, vertex_obj, visited, toRemove)
    return toRemove

def destructiveDfsUtil(graph, nextVertex, visited, toRemove):
    visited.add(nextVertex)
    for neighbor in nextVertex.get_connections():
        if neighbor not in visited:
            #print(neighbor)
            #nextVertex.remove_connection(neighbor)
            toRemove.add((nextVertex.get_id(), neighbor.get_id()))
            destructiveDfsUtil(graph, neighbor, visited, toRemove)

def nowDestroy(graph, toDestroy):
    for ptPair in toDestroy:
        graph.remove_edge(ptPair[0], ptPair[1])

def main():
    aslk= createGrid(5,5)
    #visualize.display(aslk, 5,5)
    #print(aslk.get_vertices())
    res = destructiveDfs(aslk, (0,0))
    nowDestroy(aslk, res)

    #print(res)
    visualize.display(aslk)


if __name__ == "__main__":
    main()