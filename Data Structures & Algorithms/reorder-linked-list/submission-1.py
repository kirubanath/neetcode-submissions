# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:   

        
        if not head or head.next:
            
            # get to center
            slow, fast = head,head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # break of the list
            second_head = slow.next
            slow.next   = None

            # reverse the second half
            prev = None
            cur = second_head
            while second_head:
                second_head = second_head.next
                cur.next = prev
                prev = cur
                cur = second_head
                
            
            second_head = prev

            # interleave the two lists
            i = head
            j = second_head

            while  j:
                node1 = i.next
                node2 = j.next

                i.next = j
                j.next = node1
                i = node1
                j = node2
        
        



