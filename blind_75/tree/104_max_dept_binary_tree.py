from typing import List, Optional
from my_test import test


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root =None

    def insert(self, val):
        newNode = TreeNode(val)
        if(self.root):
            current = self.root
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.root = newNode

def maxDepth(root: Optional[TreeNode]) -> int:
    # Termination conditions
    if not root:
        return 0

    left_tree_depth = maxDepth(root.left)
    right_tree_depth = maxDepth(root.right)

    return max(left_tree_depth, right_tree_depth) + 1


test(maxDepth([3, 9, 20, None, None, 15, 7]), 3)
test(maxDepth([1, None, 2]), 2)
