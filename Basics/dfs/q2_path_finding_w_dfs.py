Exercise 1: Basic DFS Traversal
Problem:

Given a graph (as an adjacency list), implement DFS to traverse the graph starting from a specified node. Print all the nodes in the order they are visited.

Graph Example:

python
Copy code
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
Task:

Implement DFS for this graph.

Start DFS from node 'A'.

Print the order of traversal.

🧩 Exercise 2: Path Finding with DFS
Problem:

Given a graph, implement DFS to check if there is a path from node A to node B.

Graph Example:

python
Copy code
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}
Task:

Implement DFS to check if there is a path from 'A' to 'E'.

If the path exists, return True; otherwise, return False.

🧩 Exercise 3: Connected Components
Problem:

Given a graph, use DFS to find all connected components in the graph. Each connected component is a subset of nodes where each node can reach every other node in that component.

Graph Example:

python
Copy code
graph = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C'],
    'E': []
}
Task:

Use DFS to find all connected components in the graph.

For this graph, the expected result is:

Component 1: ['A', 'B']

Component 2: ['C', 'D']

Component 3: ['E']

🧩 Exercise 4: DFS on a Tree
Problem:

Given a binary tree, implement DFS to find the sum of all the node values in the tree.

Binary Tree Example:

markdown
Copy code
       10
      /  \
     5   20
    / \   / \
   3   7 15 25
Task:

Use DFS to traverse the tree and compute the sum of all node values.

The expected sum of this tree is: 10 + 5 + 3 + 7 + 20 + 15 + 25 = 85.

🧩 Exercise 5: Detect Cycles in a Graph
Problem:

Given a graph, use DFS to detect if there is a cycle in the graph.

Graph Example (with a cycle):

python
Copy code
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']  # This creates a cycle: A -> B -> C -> A
}
Task:

Implement DFS to detect if there is a cycle in the graph.

If a cycle exists, return True; otherwise, return False.

🧩 Exercise 6: Find All Paths Between Two Nodes
Problem:

Given a graph, use DFS to find all paths between two nodes, start and end.

Graph Example:

python
Copy code
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
Task:

Find all paths between node 'A' and node 'D'.

For this graph, the expected result is:

['A', 'B', 'D']

['A', 'C', 'D']

🧩 Exercise 7: Topological Sort (DFS)
Problem:

Given a Directed Acyclic Graph (DAG), implement DFS to perform a topological sort.

Graph Example:

python
Copy code
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': []
}
Task:

Implement DFS to return a topologically sorted list of nodes for the graph.

For this graph, the expected output is:
['A', 'B', 'C', 'D']

🧩 Exercise 8: Find the Shortest Path in an Unweighted Graph
Problem:

Given an unweighted graph, use DFS to find the shortest path between two nodes.

Graph Example:

python
Copy code
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
Task:

Find the shortest path between A and D using DFS.

Expected result: ['A', 'B', 'D'] or ['A', 'C', 'D']

Tips for Solving:
DFS Recursion: Use a recursive approach for the DFS traversal.

Visited Set: Keep track of visited nodes to avoid revisiting and infinite loops.

Backtracking: When you reach a dead-end, backtrack and explore the next neighbor.

Edge Cases: Handle empty graphs, disconnected components, or graphs with no path.

