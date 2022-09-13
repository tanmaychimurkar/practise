# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# incomplete solution, will revisit later
class Solution:
    def levelOrder(self, root):

        if root is None:
            return

        queue = [root]
        main_result = []

        while queue:
            next_values = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                next_values.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            main_result.append(next_values)

        return main_result


_obj = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(6)
# root.right.left.left = TreeNode(7)
# root.right.left.right = TreeNode(8)


_obj.levelOrder(root)
