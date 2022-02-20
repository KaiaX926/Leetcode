    
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = []
        queue.append(root)
        
        while queue:
            size = len(queue)
            prev = queue[0]
            
            for i in range(len(queue)):
                curr = queue.pop(0)
                prev.next = curr
                prev = curr
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                     
            curr.next = None
            
        return root
