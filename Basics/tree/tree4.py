"""4. Find the Height of a Tree
Task: Write a function to find the height (maximum depth) of the tree.

Given the tree 

        A
       / \
      B   C
     / \
    D   E

Example:
A tree with just root → height = 1
A → B → D → height = 3"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Tree
node_a = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")

node_a.left = node_b
node_a.right = node_c

node_b.left = node_d
node_b.right = node_e

queue = [node_a]
current = []
level = 0

#Breadth-First Search BFS
# for each level
while queue:
    level = 0 
    level_size = len(current)+1

    # check child on the level
    while 
        # take one node out of the front of the list
        current = queue.pop(0)

        # if it has a left child
        if current.left:
            queue.append(current.left)        

        # if it has a right child
        if current.right:
            queue.append(current.right)

print(level)