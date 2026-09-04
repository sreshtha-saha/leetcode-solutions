class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node.left:
                if not node.left.left and not node.left.right:
                    total += node.left.val
                else:
                    stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
        
        return total