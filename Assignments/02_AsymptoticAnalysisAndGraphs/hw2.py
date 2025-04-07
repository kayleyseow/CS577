class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adj = []

    def add_adj(self, adj):
        self.adj += adj

def dfs(graph, starting_node):
    if(starting_node.visited == True):
        return ""
    starting_node.visited = True
    path = "" + starting_node.name + " "
    for n in starting_node.adj:
        node = graph.get(n)
        path += dfs(graph, node)
    return path

numGraphs = int(input())

allGraphs = []

for i in range(numGraphs):
    # number of nodes per graph, from input
    numNodes = int(input())
    graphTemp = {}
    for j in range(numNodes):
        nodes = input().split(' ')
        for node in nodes:
            if node not in graphTemp:
                new_node = Node(node)
                graphTemp.update({node:new_node})
        graphTemp.get(nodes[0]).add_adj(nodes[1:])
    allGraphs.append(graphTemp)

for graph in allGraphs:
    path = ""
    for node in graph.keys():
        path += dfs(graph, graph.get(node))
    print(path[:-1])









