# Gets the number of instances from the input
numInstances = int(input())

maxMatch = []

def dfs(curr, graph, past, match):
    for i in range(len(graph[0])):
        if (graph[curr][i] and past[i] == False):
            past[i] = True
            if (match[i] == -1 or dfs(match[i], graph, past, match)):
                match[i] = curr
                return True 
    return False


# Bipartite Matching
def bMatching(graph):
    pairs = [-1]*len(graph[0])
    result = 0

    for i in range(len(graph)):
        past = [False] * len(graph[0])
        if (dfs(i, graph, past, pairs)):
            result = result + 1
    return result
    
# Iterate through how many instances we have
for i in range(numInstances):
    graph = input().strip().split()
    size1 = int(graph[0])
    size2 = int(graph[1])
    edges = int(graph[2])

    matrix = [[0 for x in range(size2)] for y in range(size1)]

    for adj in range(edges):
        nodes = input().strip().split()
        node1 = int(nodes[0]) - 1
        node2 = int(nodes[1]) - 1
        matrix[node1][node2] = 1

    totalMatches = bMatching(matrix)
 
    if (size1 > totalMatches or size1 < size2):
        maxMatch.append((str(totalMatches) + " N"))
    else :
        maxMatch.append((str(totalMatches) + " Y"))     

# Print the result
for m in maxMatch:
    print(m)
