# Use mathematical calculation method to split numbers and add them to linked list one by one.
# First, derive the sum of two lists by adding the products of each number and the corresponding power of 10 in two lists.
# Second, use mod calculation to derive the remainder of the sum divided by the different power of 10 according to the position and add the number to the listed list.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x1,x2 = 0,0
        i,j = 0,0
        print(l1.next)
        
        while l1:
            x1 += l1.val*(10**i)
            l1 = l1.next
            i+=1
        
        while l2:
            x2 += l2.val*(10**j)
            l2 = l2.next
            j+=1
        
        y = x1+x2
        r = 0
        head = curr = ListNode(0)
        
        j = 1
        z = y
        
        if z == 0:
            curr.next = ListNode(0)
            return head.next
        else:
            while z > 0 :
                a = z % (10**j)
                b = a / (10**(j-1))
                z -= a
                curr.next = ListNode(b)
                #print(r)
                curr = curr.next
                print(head,curr)
                j += 1
        
            return head.next
