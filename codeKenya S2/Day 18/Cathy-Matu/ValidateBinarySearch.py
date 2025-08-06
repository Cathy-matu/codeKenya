class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            # Node value must be strictly between low and high
            if not (low < node.val < high):
                return False
            
            # Check left subtree and right subtree
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)




if __name__ == "__main__":
    sol = Solution()

   
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print("Example 1:", sol.isValidBST(root1))  

    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4, TreeNode(3), TreeNode(6))
    print("Example 2:", sol.isValidBST(root2)) 
