class Solution:
	def partition(self, head,x):
		small = ListNode()
		temp_small = small
		large = ListNode()
		temp_large = large
		while head:
			if head.val < x:
				temp_small.next = ListNode(head.val)
				temp_small = temp_small.next
			else:
				temp_large.next = ListNode(head.val)
				temp_large = temp_large.next
			head = head.next
		temp_small.next = large.next
		return small.next
