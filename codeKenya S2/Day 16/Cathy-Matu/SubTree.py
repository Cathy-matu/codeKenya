class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

    def isSubtree(self, root, subRoot):
        if not root:
            return False
        
        # If trees match at current node
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise check left or right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
root = TreeNode(3)
root.left = TreeNode(4, TreeNode(1), TreeNode(2))
root.right = TreeNode(5)

subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

sol = Solution()
print(sol.isSubtree(root, subRoot))  
