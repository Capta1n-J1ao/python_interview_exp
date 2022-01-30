# Definition for singly-linked list.
import heapq
from typing import List

# 这道题目的难点是在于不新建node行程排序，下面这个链接比较符合我的思路
# https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/duo-tu-yan-shi-23-he-bing-kge-pai-xu-lian-biao-by-/
# 但是在实际编写的时候提交会有错误，原因如下：
# https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/python-c-you-xian-dui-lie-zui-xiao-dui-onlogk-by-m/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 由于上面所说的原因，这个代码无法执行，但是思路思路一致，只是引用了enumerate
        # if lists is None or len(lists) == 0:
        #     return None
        # minHeap = []
        # for list in lists:
        #     curNode = list
        #     heapq.heappush(minHeap, (curNode.val, curNode))
        #
        # head = ListNode(-1)
        # tempNode = head
        # while not len(minHeap) == 0:
        #     cur = heapq.heappop(minHeap)
        #     if cur[1].next is not None:
        #         heapq.heappush(minHeap, (cur[1].val, cur[1]))
        #     tempNode.next = cur[1]
        #     tempNode = tempNode.next
        # return head.next

        if lists is None or len(lists) == 0:
            return None
        minHeap = []
        for index, list in enumerate(lists):
            if list is not None:
                heapq.heappush(minHeap, (list.val, index))

        head = ListNode(-1)
        tempNode = head
        while not len(minHeap) == 0:
            curVal, index = heapq.heappop(minHeap)
            tempNode.next = lists[index]
            tempNode = tempNode.next
            lists[index] = lists[index].next
            if lists[index] is not None:
                heapq.heappush(minHeap, (lists[index].val, index))

        return head.next

