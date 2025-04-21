"""April 11, 2025

Depth-First Search

Given a graph (as an adjacency list)
implement DFS to traverse the graph starting from a specified node
Print all the nodes in the order they are visited

Task:
Implement DFS for this graph.
Start DFS from node 'A'.
Print the order of traversal."""


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

visited = set()

def dfs_iterative (graph,start_node):
    stack = [start_node]
    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

dfs_iterative(graph,'A')
