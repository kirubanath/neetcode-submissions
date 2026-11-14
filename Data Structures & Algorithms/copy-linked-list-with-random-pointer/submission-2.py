"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hashmap = {None : None}
        
        # First pass : Create and link to original

        node = head

        while node:
            new_node = Node(node.val)
            hashmap[node] = new_node
            node = node.next

        
        # Second pass : Links
        node = head

        while node:
            new_node = hashmap[node]

            # next:
            new_node.next = hashmap[node.next]

            # random:
            new_node.random = hashmap[node.random]
            
            node = node.next
        
        return hashmap[head] 


        

            
        