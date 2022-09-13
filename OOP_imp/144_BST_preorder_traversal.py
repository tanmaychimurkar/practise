# Definition for a binary tree node.
import self as self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    order = []

    # def preorderTraversal(self, root):
    #
    #     def traversal(node):
    #         if not node:
    #             return
    #
    #         self.order.append(node.val)
    #         traversal(node.left)
    #         traversal(node.right)
    #
    #     traversal(root)
    #
    #     return self.order

    # iterative solution for pre-order traversal
    def preorderTraversal(self, root):
        stack = [root]
        result = []

        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return result


_obj = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)

_obj.preorderTraversal(root)
