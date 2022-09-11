"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):

        tree_nodes = []

        def get_children(node):
            tree_nodes.append(node.val)

            for child in node.children:
                if child is not None:
                    get_children(child)

        if root.val is None:
            return []

        get_children(root)
        return tree_nodes
