# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = [root.val]
        queue = []

        def bfs(node, depth):
            if not node:
                return

            if depth == len(result) - 1:
                if node.right:
                    result.append(node.right.val)
                elif node.left:
                    result.append(node.left.val)

            bfs(node.right, depth + 1)
            bfs(node.left, depth + 1)

        bfs(root, 0)
        return result
