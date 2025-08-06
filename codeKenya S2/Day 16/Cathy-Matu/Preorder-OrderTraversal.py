from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # Mapping each value to its index in inorder for O(1) lookups
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  # Pointer to track root in preorder

        def helper(left, right):
            
            if left > right:
                return None
            
            # Pick current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            # Split inorder into left and right subtrees
            mid = inorder_index[root_val]
            
            # Build left and right subtrees recursively
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root

        return helper(0, len(inorder) - 1)

# Helper function to print tree in level order
def print_level_order(root):
    if not root:
        print([])
        return
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    
    print(result)


preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]

sol = Solution()
root = sol.buildTree(preorder, inorder)

print_level_order(root)  
