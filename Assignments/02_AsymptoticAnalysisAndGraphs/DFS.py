# returns a dict with nodes and its neighbors
def generate_Graph():
    graph = dict()
    num_of_nodes = int(input())
    for i in range(num_of_nodes):
        nodes = input().strip().split(" ")
        graph[nodes[0]] = nodes[1:]
    
    return graph

# returns a list of nodes visited through dfs
def dfs(graph, visited, node):
    if node in visited:
        return
    
    visited.append(node)
    for i in graph[node]:
        dfs(graph, visited, i)

def main():
    num_of_graphs = int(input())
    dfs_transversal = []

    for i in range(num_of_graphs):
        visited = []
        graph = generate_Graph()

        for j in list(graph.keys()):
            dfs(graph, visited, j)
        dfs_transversal.append(visited)

    for trees in dfs_transversal:
        print(trees[0], end="")
        for i in range(1,len(trees)):
            print("", trees[i], end="")
        print()

if __name__ == "__main__":
    main()


