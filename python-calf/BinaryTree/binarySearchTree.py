#!/usr/bin/env python
# -*- coding: utf-8 -*-

## 二叉搜索树 排序：左 < 根 < 右


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        1，2，3分别作为根结点
        i 作为根结点的时候，(1,...,i-1) 为左子树，(i+1,...,n) 为右子树
        :type n: int
        :rtype: List[TreeNode]
        """
        treeList = []
        def compare(root, i):
            """
            :param root:
            :param i:
            :return:
            """
            if i < root.val:
                # 如果 root.left is None, i 赋值给left; 否则让 i 跟 left 继续比较
                if root.left is None:
                    root.left = TreeNode(i)
                    i += 1
                    if i <= n:
                        compare(root.left, i)
                else:
                    # 让 i 跟 left 比较
                    compare(root.left, i)
            if i > root.val:
                if root.right is None:
                    root.right = TreeNode(i)
                    i += 1
                    if i <= n:
                       compare(root.right, i)
                else:
                    compare(root.right, i)
            return root

        root = TreeNode(1)
        res = compare(root, 2)
        treeList.append(res)
        return treeList



if __name__ == '__main__':
    sol = Solution()
    rootList = sol.generateTrees(8)

    import inorderTraversal
    travelObj = inorderTraversal.Solution()
    res = travelObj.inorderTraversal(rootList[0])

    print(res)

