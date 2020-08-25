class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set() # sets are faster and they are hashtables 

    def add_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].add(v2) 
        else:
            raise IndexError("Vertex not found")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    
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



def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
    explored = set()
    stack = Stack()
    stack.push([starting_node])
    longest_path = [[starting_node]]
    earliest_one = -1
    while stack.size() > 0:
        path = stack.pop()
        current = path[-1]
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path)) and current < earliest_one: #If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID
            longest_path = path
            earliest_one = longest_path[-1]
        if current not in explored:
                explored.add(current)
                parents = graph.get_neighbors(current)
                for parent in parents:
                    new_path = path.copy()
                    new_path.append(parent)
                    stack.push(new_path)
    return earliest_one


test_ancestors = [(1,3),(2,3),(3,6),(4,5),(4,8),(5,6),(5,7),(8,9),(11,8),(10,1)]

print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 5))