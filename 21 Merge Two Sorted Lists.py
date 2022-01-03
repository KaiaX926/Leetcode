# The core idea is to compare the value of each pair in list1 and list2 and move the pointer forward in the list with the smaller value.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l = []
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    l.append(list1.val)
                    list1 = list1.next
                else:
                    l.append(list2.val)
                    list2 = list2.next
            else:
                if list1:
                    l.append(list1.val)
                    list1 = list1.next
                else:
                    l.append(list2.val)
                    list2 = list2.next
        
        if len(l) == 0:
            return None
        
        h = tail = ListNode(l[0])
        for x in l[1:]:
            tail.next = ListNode(x) # Create and add another node
            tail = tail.next # Move the tail pointer
      
        
        return h
        
