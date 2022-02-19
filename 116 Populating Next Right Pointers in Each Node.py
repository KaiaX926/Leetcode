"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    
        node = Node(-float('inf'))
        stack = [root]
        
        def find(stack):
            if stack:
                stack_next = []
                stack = stack[::-1]
                while stack:
                
                    root = stack.pop()
                    if root:
                        node.next = Node(root.val)
                        print(root.val)

                        stack_next.append(root.left)
                        stack_next.append(root.right)
                print('one end',stack_next)
                node.next = find(stack_next)
            return node
        
        node.next = find(stack)
        
        return node.next
        
       
# --------------------------------------------------------------

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def connectTwoNodes(node1, node2):
            if not node1 or not node2:
                return
            node1.next = node2
            
            connectTwoNodes(node1.left, node1.right)
            connectTwoNodes(node1.right, node2.left)
            connectTwoNodes(node2.left, node2.right)
            
        
        if not root:
            return None
        connectTwoNodes(root.left, root.right)
        return root
