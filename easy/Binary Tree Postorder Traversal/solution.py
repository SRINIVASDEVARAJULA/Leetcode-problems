# Time complexity: O(n)
# Approach: Post order traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    
    def traverse(self, head):
        if not head:
            return
        self.traverse(head.left)
        self.traverse(head.right)
        self.ans.append(head.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.ans