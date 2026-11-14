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
        # prep:
        # Node to index
        node_index = {}
        
        node = head
        index = 0

        while node:
            node_index[node] = index
            node = node.next
            index+=1
        
        # random link index
        random_links = []
        node = head

        while node:
            if node.random:
                link_index = node_index[node.random]
            else:
                link_index = -1
            
            random_links.append(link_index)
            node = node.next
        
        # deep copy:
        dummy = Node(0)
        i = head
        j = dummy
        index_to_node = []

        while i:
            j.next = Node(i.val)
            i = i.next
            j = j.next
            index_to_node.append(j)
        
        for k in range(len(random_links)):

            new_node = index_to_node[k]
            new_node_link_index = random_links[k]

            if new_node_link_index != -1:
                new_node.random = index_to_node[new_node_link_index]
        
        return dummy.next

        
        

    






            

        


