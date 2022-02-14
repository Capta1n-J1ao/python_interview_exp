# Definition for a binary tree node.
from collections import deque

# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/cpython3-1dfs_nlr-2bfs-by-qrhqcdd90g-j81c/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "null"
        queue = deque()
        queue.append(root)
        ser_string = []
        while queue:
            qLen = len(queue)
            for i in range(qLen):
                curNode = queue.popleft()
                if curNode is None:
                    ser_string.append("null")
                else:
                    ser_string.append(str(curNode.val))
                    queue.append(curNode.left)
                    queue.append(curNode.right)
        return " ".join(ser_string)







    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "null":
            return None
        data = data.split(" ")
        # print(type(data))
        root = TreeNode(int(data[0]))
        queue = deque()
        queue.append(root)
        index = 1
        while index < len(data):
            curNode = queue.popleft()
            if data[index] != "null":
                leftNode = TreeNode(int(data[index]))
                curNode.left = leftNode
                queue.append(leftNode)
            index += 1
            if data[index] != "null":
                rightNode = TreeNode(int(data[index]))
                curNode.right = rightNode
                queue.append(rightNode)
            index += 1
        return root



# Your Codec object will be instantiated and called as such:
root = TreeNode(100)
ser = Codec()
# print(ser.serialize(root))
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
