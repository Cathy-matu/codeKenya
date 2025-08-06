class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # In-order traversal using a stack
        stack = []
        while True:
            # Go as left as possible
            while root:
                stack.append(root)
                root = root.left
            
            # Pop the smallest element
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val  # k-th smallest found
            
            # Visit right subtree
            root = root.right



if __name__ == "__main__":
   
    root1 = TreeNode(3)
    root1.left = TreeNode(1, None, TreeNode(2))
    root1.right = TreeNode(4)
    
    sol = Solution()
    print("Example 1:", sol.kthSmallest(root1, 1))  

    
    root2 = TreeNode(5)
    root2.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
    root2.right = TreeNode(6)
    
    print("Example 2:", sol.kthSmallest(root2, 3))  
