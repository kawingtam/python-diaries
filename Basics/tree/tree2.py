"""2. Print All Node Values (No DFS or recursion)
Task: Given the tree 

        A
       / \
      B   C
     / \
    D   E
write a function to print all node values using a simple loop 
(you can use a list or queue for help).

Hint: Use a list like a queue. Add root, 
then loop over list while adding children.
"""


""""A" = ["B","C"]
"B" = ["D","E"]
"C" = []
"D" = []
"E" = []"""

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

queue = [node_a]
current = []

while queue:
    # take one node out of the front of the list
    current = queue.pop(0)

    # print its value
    print(current.value)
    

    # if it has a left child, add it to the list
    
    if current.left:
        queue.append(current.left)

    # if it has a right child, add it to the list
    if current.right:
        queue.append(current.right)