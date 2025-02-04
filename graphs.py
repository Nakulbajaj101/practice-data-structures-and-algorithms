class Graph:
    def __init__(self):
        self.num_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.num_of_nodes += 1

    def add_edge(self, node1, node2):
        if node1 in self.adjacent_list.keys():
            self.adjacent_list[node1].append(node2)
        if node2 in self.adjacent_list.keys():
            self.adjacent_list[node2].append(node1)

    def show_connections(self):
        if len(self.adjacent_list) > 0:
            for key in self.adjacent_list.keys():
                if len(self.adjacent_list[key]) > 0:
                    values = " ".join(str(i) for i in self.adjacent_list[key])
                    print(f"{key} --> {values}")


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

g.add_edge(1,2)
g.add_edge(2,3)
g.show_connections()
