# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        
        i = list1
        j = list2

        head,tip = None, None
        while i and j:
            node = None
            if i.val <= j.val:
                node = i
                i = i.next
            else:
                node = j
                j = j.next
            
            if not head:
                head = node
                tip  = node
            else:
                tip.next = node
                tip = tip.next

        
        if i:
            if head:
                tip.next = i
            else:
                head = i
        elif j:
            if head:
                tip.next = j
            else:
                head = j
        
        return head
            


                


        