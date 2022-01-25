# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curNode = head
        while curNode:
            copyNode = Node(curNode.val, None, None)
            copyNode.next = curNode.next
            curNode.next = copyNode
            curNode = copyNode.next
        # reset curNode
        curNode = head
        while curNode:
            # print(curNode.val)
            if curNode.random:
                curNode.next.random = curNode.random.next
            curNode = curNode.next.next
        # reset curNode
        curNode = head.next
        copyHead = head.next
        while curNode:
            # print(curNode.val)
            if curNode.next:
                curNode.next = curNode.next.next
            curNode = curNode.next
        return copyHead




