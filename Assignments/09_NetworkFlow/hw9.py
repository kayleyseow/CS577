# Gets the number of instances from the input
numInstances = int(input())

maxPaths = []

def bfs(graph, start, find, parent):
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True
    while queue:
        u = queue.pop(0)
        for index in range(len(graph[u])):
            if visited[index] is False and graph[u][index] > 0:
                queue.append(index)
                visited[index] = True
                parent[index] = u
    return True if visited[t] else False

# Runs the ford Fulkerson algorithm
def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow
    
# Iterate through how many instances we have
for i in range(numInstances):
    # number of items per instance, from input
    tempNodes, tempEdges = input().strip().split()
    nodes, edges = int(tempNodes), int(tempEdges)
    graph = [[0 for x in range(nodes)] for x in range(nodes)]
        for e in range(edges):
            tempStart, tempEnd, tempWeight = input().strip().split()
            start, end, weight = int(start), int(end), int(weight)
            graph[start - 1][end - 1] += weight
        maxPaths.add(ford_fulkerson(graph, 0, num_nodes - 1))

# Print the result
for mPaths in maxPaths:
    print(mPaths)
