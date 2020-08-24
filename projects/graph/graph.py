"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # pass  # TODO
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO
        if v1 in self.vertices:
            self.vertices[v1].add(v2) 
        else:
            self.vertices[v1] = [v2]

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size() > 0:
            current_node = queue.dequeue()
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # pass  # TODO
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for edge in self.vertices[starting_vertex]:
            if edge not in visited:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # pass  # TODO
        explored = set() # keep track of explored nodes
        queue = Queue()
        queue.enqueue([starting_vertex]) # keep track of all the paths to be checked
         # keeps looping until all possible paths have been checked
        while queue.size() > 0: 
            path = queue.dequeue() # pop the first path from the queue
            last_vert = path[-1] # get the last node from the path
            if last_vert == destination_vertex:
                return path
            if last_vert not in explored:
                neighbors = self.get_neighbors(last_vert)
                # go through all neighbor nodes, construct a new path and
                # push it into the queue
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)
                    # return path if neighbor is goal
                    if neighbor == destination_vertex:
                        return new_path
                # mark node as explored
                explored.add(last_vert)
           
        return "Connecting path doesn't exist"

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO
        stack = Stack()
        stack.push(starting_vertex) # keep track of all the paths to be checked
        explored = set() # keep track of explored nodes
        while stack.size() > 0:
            current_node = stack.pop()
            explored.add(current_node)
            for edge in self.get_neighbors(current_node):
                if edge not in explored:
                    stack.push(edge)
                if edge is destination_vertex:
                    explored.add(edge)
                    return list(explored)
            


    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
​
        This should be done using recursion.
        """
        ## mark our node as visited
        visited.add(starting_vertex)
        ## check if it's our target node, if so return
        if starting_vertex == destination_vertex:
            return path
        if len(path) == 0:
            path.append(starting_vertex)
        ## iterate over neighbors
        neighbors = self.get_neighbors(starting_vertex)
        ### check if visited
        for neighbor in neighbors:
            if neighbor not in visited: 
        #### if not, recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)
        ##### if this recursion returns a path,
                if result is not None:
            ###### return from here
                    return result


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
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
