# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def merge(self, lists):
        # Empty List
        if not lists:
            return None
        
        # Only one listnode -> No need to merge
        if len(lists) == 1:
            return lists[0]
                

        i,j = lists[0], lists[1]
        dummy = ListNode()
        k = dummy
        while i and j:
            if i.val < j.val:
                k.next = i
                i = i.next
            else:
                k.next = j
                j = j.next
            
            k = k.next
        
        while i:
            k.next = i
            i = i.next
            k = k.next
        
        while j:
            k.next = j
            j = j.next
            k = k.next
        

        return dummy.next




    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) < 3:
            return self.merge(lists)
        
        # break the lists into two halves and sort them both
        mid = len(lists)//2
        left_half = self.mergeKLists(lists[:mid])
        right_half = self.mergeKLists(lists[mid:])

        # merge them both and return 
        return self.merge([left_half, right_half])




        