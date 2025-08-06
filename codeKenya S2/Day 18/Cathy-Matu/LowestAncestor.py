class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # Both p and q are smaller than root
            if p.val < root.val and q.val < root.val:
                root = root.left
            # Both p and q are greater than root
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                # Split point found
                return root
if __name__ == "__main__":
    # Construct BST
    root = TreeNode(6)
    root.left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    root.right = TreeNode(8, TreeNode(7), TreeNode(9))

    sol = Solution()

    # 1.0
    p, q = root.left, root.right  
    print("Example 1:", sol.lowestCommonAncestor(root, p, q).val)  

    #2.0
    p, q = root.left, root.left.right 
    print("Example 2:", sol.lowestCommonAncestor(root, p, q).val)  
