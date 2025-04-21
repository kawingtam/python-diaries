"""April 21, 2025
Exercise 3: Connected Components
Problem:
Given a graph, use DFS to find all connected components in the graph. 
Each connected component is a subset of nodes 
where each node can reach every other node in that component.

Task:
Use DFS to find all connected components in the graph.
For this graph, the expected result is:
Component 1: ['A', 'B']
Component 2: ['C', 'D']
Component 3: ['E']"""

graph = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C'],
    'E': []
}

visited = set()
count = 0 

def dfs (graph,node,connected,component):

