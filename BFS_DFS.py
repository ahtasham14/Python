from heapq import heapify
from binarytree import tree, setup, convert, inspect, pprint

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6,7],
    4: [8, 9],
    5: [10, 11],
    11: [12, 13]
}

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# Convert the list into a tree and return its root
my_tree = convert(my_list)

# Convert the list into a heap and return its root
heapify(my_list)
my_tree = convert(my_list)

# Convert the tree back to a list
my_list = convert(my_tree)

# Pretty-printing also works on lists
pprint(my_tree)



class MyNode(object):

    def __init__(self, data, left, right):
        self.data = data
        self.l_child = left
        self.r_child = right

def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()
    	 
    print (start , end)	
    while queue:
        # Gets the first path in the queue. As it is BFS so we implement Queue as a Data Structure. 
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            # Mark the vertex as visited
            print (vertex)
            visited.add(vertex)
            
def dfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()
    	 
    print (start , end)	
    while queue:
        # Gets the first path in the queue. This is DFS, It was implemented by Stack as per standard. But we implemented it as Queue.
        #The new thing is that we pop it by rear end by putting (-1)
        path = queue.pop(-1)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            # Mark the vertex as visited
            print (vertex)
            visited.add(vertex)
print '--------------BFS----------------'   
print (bfs(graph, 1, 11))
print '--------------DFS----------------'    
print (dfs(graph, 1, 11))
