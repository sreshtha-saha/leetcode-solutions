class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        result = []

        def dfs(node, path):
            if not node.left and not node.right:
                result.append(path)
                return
            if node.left:
                dfs(node.left, path + "->" + str(node.left.val))
            if node.right:
                dfs(node.right, path + "->" + str(node.right.val))

        dfs(root, str(root.val))
        return result