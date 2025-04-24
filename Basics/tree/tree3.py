"""3. Count Total Nodes in a Tree
Task: Write a function that counts how many nodes are in a binary tree.
Given the tree 

        A
       / \
      B   C
     / \
    D   E
Start with:
def count_nodes(root):
    # your code here
Try doing this without recursion first (using a queue or stack), 
then try it with recursion when you're ready.
"""
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
count = 0

while queue:
    # take one node out of the front of the list
    current = queue.pop(0)

    count +=1 # count the current node
    
    # if it has a left child
    if current.left:
        queue.append(current.left)
        

    # if it has a right child
    if current.right:
        queue.append(current.right)

print(count)