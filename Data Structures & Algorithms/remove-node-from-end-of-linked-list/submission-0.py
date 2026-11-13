# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        l = dummy
        r = head.next
        i,j = head,head

        # second pointer move n away
        for count in range(n):
            j = j.next
        

        # reach the end so that the first pointer is at n from last
        while j:
            l,r,i,j = i,i.next.next,i.next,j.next
        
        # remove the required node
        l.next = r

        return dummy.next
