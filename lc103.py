# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        # True = l to r, False = r to l
        flag = True
        queue = deque()
        queue.append(root)
        res = [[root.val]]
        while len(queue) > 0:
            qLen = len(queue)
            flag = not flag

            curRes = []
            for i in range(qLen):
                curNode = queue.pop()
                if curNode.left is not None:
                    queue.appendleft(curNode.left)
                    curRes.append(curNode.left.val)
                if curNode.right is not None:
                    queue.appendleft(curNode.right)
                    curRes.append(curNode.right.val)
            if not flag:
                curRes.reverse()
            if len(curRes) > 0:
                res.append(curRes)

        return res
