# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        p = head
        while p.next:
            print(p.val, p.next.val)
            if p.val == p.next.val:
                if p.next.next is not None:
                    p.next = p.next.next
                else:
                    p.next = None
            else:
                p = p.next
        
        return head
