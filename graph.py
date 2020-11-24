class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = set()

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor):
        self.adjacent.add(neighbor)

    def get_connections(self):
        return self.adjacent  

    def remove_connection(self, other):
        if other in self.adjacent:
            self.adjacent.remove(other)

    def get_id(self):
        return self.id


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def remove_edge(self, frm, to):
        frm_obj = self.vert_dict[frm]
        to_obj = self.vert_dict[to]
        frm_obj.remove_connection(to_obj)
        to_obj.remove_connection(frm_obj)

    def add_edge(self, frm, to):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to])
        self.vert_dict[to].add_neighbor(self.vert_dict[frm])

    def get_vertices(self):
        return self.vert_dict.keys()
    
def main():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_edge(1,2)

    al = g.get_vertices()
    for node in al:
        print(g.get_vertex(node))

if __name__ == "__main__":
    main()