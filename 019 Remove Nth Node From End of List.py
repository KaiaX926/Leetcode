# The core idea is to enter the value of each node into a list in order, remove the number at the certain place, and input the numbers in the list into a new listed node tree.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = []
        start = head
        
        while start:
            l.append(start.val)
            start = start.next
            
        del l[-n]

        if len(l) == 0:
            return None
        
        tail = h = ListNode(l[0])
        for x in l[1:]:
            tail.next = ListNode(x) # Create and add another node
            tail = tail.next # Move the tail pointer
        
        return h
        
        
            
