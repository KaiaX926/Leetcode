# The core idea is to transfer the linked list into a list, put the last k item in the front of the list and transfer the list into a linked list.
# It's worth noting that if k is larger than the length of list, redefine k as k % len(list).

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        v = []
        while head:
            v.append(head.val)
            head = head.next
        
        if len(v) < 1:
            return head
        
        if k > len(v):
            k = k % len(v)
            
        first = v[:len(v) - k]
        last = v[len(v) - k:]
        v = last + first
        
        head = tail = ListNode(v[0])
        for i in range(1,len(v)):
            tail.next = ListNode(v[i])
            tail = tail.next
        
        return head
                
