"""April 11, 2025
Given a graph (as an adjacency list)
implement DFS to traverse the graph starting from a specified node
Print all the nodes in the order they are visited

Task:
Implement DFS for this graph.
Start DFS from node 'A'.
Print the order of traversal."""

visited=set()

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
for node in graph:
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            continue

print(visited)
        