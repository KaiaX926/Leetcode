# The core idea is always to combine the first two listed nodes in the list while the first item of the list will be updated into the combined listed nodes and the third item in the beforehand list will become the second item in the new list.
# We still use the DFS method.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if len(lists) == 0:
            return None
        
        profix = lists[0]
        
        if len(lists) == 1:
            return profix
        
        x = lists[1]
        r = tail = ListNode()

        while profix and x:
            if profix.val > x.val:
                tail.next = x
                x = x.next
            else:
                tail.next = profix
                profix = profix.next   
            tail = tail.next
         
        if profix is not None:
            tail.next = profix
        if x is not None:
            tail.next = x
        
        r = r.next
        lists[0] = r
        
        del lists[1]
        profix = self.mergeKLists(lists)                
        return profix          
                    
                
