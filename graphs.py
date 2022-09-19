class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)
    #returns a list of edges in the format (value, node_from value, node_to value)
    def get_edge_list(self):
        if type(self.edges) is list:
            ret = []
            for x in self.edges:
                ret.append((x.value, x.node_from.value, x.node_to.value))
            return ret
        else:
            return ("Error: no list found")

    #returns a list containing lists of edges connected to the node corresponding to the current index, filtered to have each element show up only once
    def get_adjacency_list(self):
        x = len(self.nodes)
        ret = [None]*(x+1)
        edges = self.get_edge_list()
        for edge in edges:
            if ret[edge[1]] is None:
                ret[edge[1]] = [(edge[2], edge[0])]
            else:
                ret[edge[1]].append((edge[2], edge[0]))

        return ret
    #version of the adjacency list that doesn't use the get_edge_list function
    def get_adjacency_list_standalone(self):
        x = len(self.nodes)
        ret = [None]*(x+1)
        for y in self.nodes:
            temp = []
            for edge in y.edges:
                temp.append((edge.node_to.value, edge.value))
            ret[y.value] = temp
        return ret
    
    #returns a matrix containing either 0 or the edge value where the matrix indices corespond to the 2 nodes, filtered to have each element show up once
    def get_adjacency_matrix(self):
        x = len(self.nodes)
        ret = [None]*(x+1)
        for y in range(x+1):
            ret[y] = [0] * (x+1)

        edge = self.get_edge_list()
        for ed in edge:
            ret[ed[1]][ed[2]] = ed[0]
        return ret



    #Depth First search (DFS), Traverse a graph by prioritizing going deeper than visiting nodes. In other words, if the current node has connections to unvisited nodes, 
    #those will be visited before unmarked nodes from previous visited nodes, a stack is usually used to remember which nodes to travel to next
    def DFS(self, start, visited = None):
        if visited == None:
            visited = set()
        visited.add(start)
        print(start.value, end=" ")
        adlist = []
        for edge in start.edges:
            adlist.append(edge.node_to)
        for next in adlist:
            if not next in visited:
                self.DFS(next, visited)
        return visited

    #Breadth First Search (BFS), elements to visit get added to the queue, prioritizing elements longer in the queue to visit next
    def BFS(self, start):
        queue = []
        visited = []
        queue.append(start)
        while queue:
            visited.append(queue[0])
            for edge in queue[0].edges:
                if (not edge.node_to in visited) and (not edge.node_to in queue):
                    queue.append(edge.node_to)
            print(queue[0].value, end=" ")
            queue.pop(0)

graph = Graph()
graph.insert_node(1)
graph.insert_node(2)
graph.insert_node(3)
graph.insert_node(4)

graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

print (graph.get_edge_list())
print (graph.get_adjacency_list())
print (graph.get_adjacency_matrix())
print("DFS")
graph.DFS(graph.nodes[0])
print()
print("BFS")
graph.BFS(graph.nodes[0])

