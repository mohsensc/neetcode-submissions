# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root: return TreeNode(val)
        
        node = root

        while True:
            value = node.val

            if value > val:
                if not node.left:
                    new = TreeNode(val)
                    node.left = new
                    break
                
                node = node.left

            elif value < val:
                if not node.right:
                    new = TreeNode(val)
                    node.right = new
                    break
                
                node = node.right 
        
        return root
