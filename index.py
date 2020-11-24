'''
graph code courtesy of https://www.bogotobogo.com/python/python_graph_data_structures.php

'''

from graph import Graph
import visualize

def createGrid(width, height) -> int:#do more with this

    newGraph = Graph()
    for i in range(width-1):
        for j in range(height-1):
            newGraph.add_edge((i,j),(i, j+1))
            newGraph.add_edge((i,j),(i+1, j))
    return newGraph


def main():
    aslk= createGrid(5,5)
    visualize.display(aslk, 5,5)
    #print(len(aslk.get_vertices()))


if __name__ == "__main__":
    main()