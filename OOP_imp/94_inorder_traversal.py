# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # # recursive solution
    # def postorderTraversal(self, root):

        # def traversal(node):
        #     if not node:
        #         return
        #
        #     traversal(node.left)
        #     traversal(node.right)
        #     order_list.append(node.val)
        #
        # order_list = []
        # traversal(root)
        #
        # return order_list

    # iterative solution for pre-order traversal
    def inorderTraversal(self, root):
        stack = [root]
        result = []

        while stack and root is not None:
            root = stack.pop()
            result.append(
                root.val
            )
            if root.left:
                stack.append(root.left)
                print(root.left.val)

            if root.right:
                stack.append(root.right)
                print(root.right.val)
        print(stack)
        return result[::-1]




        # while root is not None or stack:
        #
        #     while root is not None:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     result.append(root.val)
        #     if root.right:
        #         result.append(root.val)
        #     root = root.right

        return result




_obj = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(6)
# root.right.left.left = TreeNode(7)
# root.right.left.right = TreeNode(8)

_obj.inorderTraversal(root)
