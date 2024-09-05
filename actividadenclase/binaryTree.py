import time
class Node:
    def __init__(self, key):
        self.key = key  
        self.left = None 
        self.right = None  

class BinaryTree:
    def __init__(self):
        self.root = None  

    def traverseTree(self, node):
        if node is not None:
            self.traverseTree(node.left)  
            print(f" {node.key}", end="") 
            self.traverseTree(node.right)  


# main
# start time
startTime = time.perf_counter()

tree = BinaryTree()

# Create nodes of the tree
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)

print("Binary Tree:", end=" ")
tree.traverseTree(tree.root)

# end time
endTime = time.perf_counter()
executionTime = (endTime - startTime) * 1000  # Convert to milliseconds

print("\nExecution Time: {:.4f} ms".format(executionTime)) 





