# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# incomplete solution, will revisit later
class Solution:
    def levelOrder(self, root):

        level_order = [[root.val]]

        # def get_children(node):
        children = []
        child_root = []

        if root.left is not None:
            child_root.extend([root.left.val])
            # return
        if root.right is not None:
            child_root.extend([root.right.val])

        level_order.append([root.val])
        level_order.append(child_root)
        # child_node.append([child_node])


tree = TreeNode(1, 3, 5)
tree.left = TreeNode(3, 6, 7)
tree.right = TreeNode(5, 9, 10)
tree

_obj = Solution()
-_obj.levelOrder(tree)
