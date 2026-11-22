# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        checkpoint = dummy
        dummy.next = head
        can_reverse= True
        
        while can_reverse:
            
            # check every k nodes and reverse it till we can't
            checkpoint, can_reverse = self.reverse(checkpoint, k)
        
        return dummy.next
    
    def reverse(self, checkpoint, k):

        # check if we can reverse in the first place:
        node_k = checkpoint
        
        for _ in range(k):

            node_k = node_k.next
            
            # There are not enough nodes to reverse
            if not node_k:
                return checkpoint, False
        
        # Now we can reverse
        new_checkpoint = checkpoint.next
        new_next_node  = node_k.next

        # reverse:
        prev = checkpoint
        node = checkpoint.next

        for _ in range(k):
            tmp = node.next
            node.next = prev
            prev, node = node, tmp
        
        new_checkpoint.next = new_next_node
        checkpoint.next = node_k

        return new_checkpoint, True








