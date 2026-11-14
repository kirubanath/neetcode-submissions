# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        i = l1
        j = l2
        reminder = 0
        dummy = ListNode()
        k = dummy

        while i and j:
            s   = i.val + j.val + reminder
            val = s%10
            reminder = s//10 
            k.next = ListNode(val)

            i = i.next
            j = j.next
            k = k.next
        
        while i:
            s   = i.val + reminder 
            val = s%10
            reminder = s//10 
            k.next = ListNode(val)

            i = i.next
            k = k.next
        
        while j:
            s   = j.val + reminder 
            val = s%10
            reminder = s//10 
            k.next = ListNode(val)

            j = j.next
            k = k.next
        
        if reminder:
            k.next = ListNode(reminder)
        
        return dummy.next




