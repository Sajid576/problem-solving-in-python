'''https://leetcode.com/problems/binary-tree-inorder-traversal/'''

import google_problems.my_test as my_test
from typing import *


null = None


def inorderTraversal(root) -> List[int]:
    res = []

    if root:
        if root.left:
            res += inorderTraversal(root.left)

        res.append(root.val)

        if root.right:
            res += inorderTraversal(root.right)

    return res


my_test.test(inorderTraversal([1, null, 2, 3]), [1, 3, 2])
my_test.test(inorderTraversal([]), [])
my_test.test(inorderTraversal([1]), [1])
my_test.test(inorderTraversal([1, 2]), [2, 1])
my_test.test(inorderTraversal([1, null, 2]), [1, 2])
