class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        
        # use three pointers to remove duplicates
        p1, p2, prev = head, head.next, None
        while p2:
            if p1.val != p2.val:
                prev = p1
                p1 = p2
                p2 = p2.next
            else:
                # set the third pointer at the right position
                while p2 and p1.val == p2.val:
                    p2 = p2.next
                
                # if previous is None , adjust the head of the list at the right position
                if not prev:
                    head = p2
                    p1 = head
                    if p2:
                        p2 = p2.next
                else:
                    prev.next = p2
                    p1 = prev
                
        return head
