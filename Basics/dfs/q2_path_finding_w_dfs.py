"""April 21, 2025
Exercise 2: Path Finding with DFS
Problem:
Given a graph, implement DFS to check if there is a path from node A to node B.

Task:
Implement DFS to check if there is a path from 'A' to 'E'.
If the path exists, return True; otherwise, return False.
"""
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []

}


visited = set()

def dfs (graph,node,target,visited):
    if node == target:
        return True

    visited.add(node)


    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True


    return False

print(dfs(graph,'A','E',visited))