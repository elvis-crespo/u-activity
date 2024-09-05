import time
class LinkedList:
    class Node:
        def __init__(self, d):
            self.value = d 
            self.next = None  

    def __init__(self):
        self.head = None  # Initialize the head of the linked list


# start time
startTime = time.perf_counter()

# Create an object of LinkedList
linkedList = LinkedList()

# Assign values to each linked list node
linkedList.head = LinkedList.Node(1)
second = LinkedList.Node(2)
third = LinkedList.Node(3)

linkedList.head.next = second
second.next = third

print("LinkedList:", end=" ")
current = linkedList.head
while current is not None:
    print(current.value, end=" ")
    current = current.next

# end time
endTime = time.perf_counter()
executionTime = (endTime - startTime) * 1000  # Convert to milliseconds

print("\nExecution Time: {:.4f} ms".format(executionTime))     
