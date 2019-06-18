"""
- Write a function given the dataset and id of an individual
- return their earliest known ancestor (DFS)
- if there is a tie return the one with the lowest numeric id
- If the input individual has no parents return -1
"""
from util import Stack, Queue  # These may come in handy


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def dfs(self, starting_vertex):
        return_paths = []
        visited = set()
        s = Stack()

        root_node = [starting_vertex]
        s.push(root_node)

        while s.size() > 0:
            path = s.pop()
            node = path[-1]

            if node not in visited:
                visited.add(node)
                if len(self.visited[node]) == 0:
                    return_paths.append(path)

                for next_vertex in self.vertices[node]:
                    if next_vertex in self.vertices[node]:
                        if next_vertex not in visited:
                            new_path = path.copy()
                            new_path.append(next_vertex)

                            s.push(new_path)

        max_path_len = float('-inf')
        parent_vertex = float('inf')

        for path in return_paths:
            if len(path) > max_path_len:
                max_path_len = len(path)
                parent_vertex = path[-1]

            if len(path) == max_path_len:
                parent_vertex = min(parent_vertex, path[-1])

        if parent_vertex == starting_vertex:
            parent_vertex = -1

        return parent_vertex


def earliest_ancestor(dataset, item):
    print(item, dataset)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_vertex(10)
    graph.add_vertex(11)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 6)
    graph.add_edge(5, 6)
    graph.add_edge(5, 7)
    graph.add_edge(4, 5)
    graph.add_edge(4, 8)
    graph.add_edge(8, 9)
    graph.add_edge(11, 8)
    graph.add_edge(10, 1)
