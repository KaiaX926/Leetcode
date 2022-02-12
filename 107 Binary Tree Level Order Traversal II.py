class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def parser(root,lt,num=0):
            if not root:
                return lt
            num+=1
            if len(lt)<num:
                lt.append([])
            lt[num-1].append(root.val)
            parser(root.left,lt,num)
            parser(root.right,lt,num)
            return lt
        lt=list()
        return parser(root,lt)[::-1]
