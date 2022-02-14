# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        stack,nodes = [],[]
        
        while head:
            nodes.append(head.val)
            head = head.next
        
        print(nodes)
            
        if len(nodes) == 0:
            return None
        
        long = len(nodes)
        def find(nodes):
            idx = len(nodes)//2
            
            if len(nodes) > 0:
                node = TreeNode(nodes[idx])
                node.left = find(nodes[:idx])
                if len(nodes) - idx - 1 > 0:
                    node.right = find(nodes[idx+1:])
            
                return node
            
            else:
                return None
        
        return find(nodes)
