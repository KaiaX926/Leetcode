# To construct the binary tree:
# If inorder is not empty create a root node by "consuming" preorder[0].
# Construct its left subtree starting from the next item in preorder and using the inorder prefix bounded by inorder.index(preorder[0]).
# Constrcut its right subtree using the remaining items in preorder and the inorder suffix starting at 1 + inorder.index(preorder[0]).

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(p_s, p_e, i_s, i_e):
           
            if p_s >= p_e:
                return None
            
            node = TreeNode(preorder[p_s])
            
            idx = idxs[preorder[p_s]] 
            node.left = build(p_s + 1, p_s + idx - i_s + 1, i_s, idx) 
            node.right = build(p_s + idx - i_s + 1, p_e, idx + 1, i_e) 
            
            return node
        
        idxs = {n: i for i, n in enumerate(inorder)}
        return build(0, len(preorder), 0, len(inorder))
