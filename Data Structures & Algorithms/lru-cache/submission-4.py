"""
Doubly linked list to maintain the order!
head - list - tail (dummy head and tail is helpful)
"""
class Node:
    def __init__(self,key = None, val = None, left = None, right = None):
        self.key = key
        self.val = val
        self.left= left
        self.right = right 

class LRUCache:

    def __init__(self, capacity: int):

        # dictionary to store the keys and corresponding nodes:
        self.key_map = {}
        self.capacity = capacity

        # doubly linked list init
        self.head,self.tail = Node(0,0), Node(0,0)
        self.head.right = self.tail
        self.tail.left  = self.head
        

    def get(self, key: int) -> int:
        
        if key not in self.key_map:
            return -1
        
        # update access:
        self.update_access(key)

        # return the value:
        return self.key_map[key].val



    def put(self, key: int, value: int) -> None:

        if key in self.key_map:
            # update the existing node:
            self.key_map[key].val = value
        
        else:
            # create new node:
            self.key_map[key] = Node(key,value)
        
        # update access:
        self.update_access(key)

        # trim if needed:
        if len(self.key_map) > self.capacity:
            self.trim()


    def update_access(self,key):

        node = self.key_map[key]
        
        # if its an already existing node, remove it from the list
        if node.left:
            node.left.right = node.right
        
        if node.right:
            node.right.left = node.left
        
        # Add it at the end
        end_node = self.tail.left
        
        end_node.right = node
        node.left = end_node

        node.right = self.tail
        self.tail.left = node

    
    def trim(self):

        node = self.head.right
        next_node = node.right

        self.head.right = next_node
        next_node.left  = self.head

        del self.key_map[node.key] 
        
