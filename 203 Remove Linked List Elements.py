# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
            
        start = head
        
        while head:
            temp = head.next
            while temp and temp.val == val:
                temp = temp.next
            head.next = temp
            head = head.next
            
        return start
