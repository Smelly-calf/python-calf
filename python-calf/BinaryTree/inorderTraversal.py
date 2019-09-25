#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node. 左->根->右
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        # 递归 # 迭代
        """
        btree = []
        def recurse(node):
            if node:
                btree.append(node.val)
                recurse(node.left)
                recurse(node.right)
        recurse(root)


        return btree



if __name__ == '__main__':
    arr = [1, None, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    obj = Solution()
    res = obj.inorderTraversal(root)
    print(res)