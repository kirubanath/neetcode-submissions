# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev_node = None
        while head and head.next:
            cur_node = head
            head = head.next
            cur_node.next = prev_node
            prev_node = cur_node
        
        if head:
            head.next = prev_node

        return head





        
