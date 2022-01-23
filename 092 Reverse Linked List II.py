# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right) :
        if (head is None or head.next is None or left-right==0):
            return head
        
        count = 0
        # Node to head of ListNode to be able to assign startPrev
        
        temp = ListNode(0)
        temp.next = head
        head = temp
        
        # Define start and end Node
        start = None
        end = None
        
        # Define latest place of start and end Node places where stayed
        startPrev = None
        endNext = None
        
        # Find start and end Node
        temp = head
        prev = None
        while (temp is not None):
            
            if (count==left):
                startPrev = prev
                start = temp
            if (count == right):
                end = temp
                endNext = temp.next
                break
            prev = temp
            temp = temp.next
            count+=1
            
        prev = None
        count =0 
        
        
        # Reverse
        while (count<=right-left):

            startNext = start.next
            start.next = endNext
            endNext = start
            
            start = startNext
            count+=1
            
        startPrev.next = end
            
        # Return head.next because we attached a Node(0) to define startPrev value which is not None.
        
        return head.next
