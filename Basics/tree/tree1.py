"""April 22, 2025
Entry-Level Tree Questions (Before DFS)
1. Build a Simple Binary Tree

# Define a TreeNode class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
✅ Task: Create a binary tree like this:

        A
       / \
      B   C
     / \
    D   E
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# calling the method
node_a = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")

node_a.left = node_b
node_a.right = node_c

node_b.left = node_d
node_b.right = node_e

