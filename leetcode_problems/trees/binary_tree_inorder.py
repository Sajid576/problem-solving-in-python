'''https://leetcode.com/problems/binary-tree-inorder-traversal/'''

import myTest
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


myTest.test(inorderTraversal([1, null, 2, 3]), [1, 3, 2])
myTest.test(inorderTraversal([]), [])
myTest.test(inorderTraversal([1]), [1])
myTest.test(inorderTraversal([1, 2]), [2, 1])
myTest.test(inorderTraversal([1, null, 2]), [1, 2])
