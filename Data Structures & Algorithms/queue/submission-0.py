class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)

        self.head.right = self.tail
        self.tail.left  = self.head

    def isEmpty(self) -> bool:
        return self.head.right == self.tail
        

    def append(self, value: int) -> None:
        
        node = Node(value)
        prev_node = self.tail.left

        prev_node.right = node
        node.left = prev_node

        node.right = self.tail
        self.tail.left = node
        

    def appendleft(self, value: int) -> None:

        node = Node(value)
        prev_node = self.head.right

        self.head.right = node
        node.left = self.head

        node.right = prev_node
        prev_node.left = node

        node = self.head
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        node = self.tail.left
        next_node = node.left

        next_node.right = self.tail
        self.tail.left = next_node
        
        return node.value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        
        node = self.head.right
        next_node = node.right

        next_node.left = self.head
        self.head.right = next_node

        return node.value
        
