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

        if head is None:
            return None

        ## Three passes with pointer manipulation:

        # First pass : Random pointer of the original list

        l1 = head

        while l1:

            # create the new node:
            l2 = Node(l1.val)

            # random pointer of original as link to this
            l2.next = l1.random
            l1.random = l2

            l1 = l1.next
        
        # Now we have all the new nodes. Lets fix their random pointers

        newHead = head.random
        l1 = head

        while l1:
            l2 = l1.random
            l2.random = l2.next.random if l2.next else None
            l1 = l1.next
        
        # Now fix the random link of original and next link of new

        l1 = head

        while l1:
            l2 = l1.random
            l1.random = l2.next
            l2.next = l1.next.random if l1.next else None
            l1 = l1.next
        
        return newHead





        