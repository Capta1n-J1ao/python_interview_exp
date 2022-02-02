import heapq
import random
from typing import List

# 其他视频都不好，还是参考原来的视频
# https://www.bilibili.com/video/BV15Z4y1p7KR?t=412
# lc295_1是一个基于quick sort对于数组的排序
class Solution:
    # 方法一，大根堆，很简单
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     minHeap = []
    #     numLen = len(nums)
    #     threshold = numLen - k + 1
    #     for num in nums:
    #         heapq.heappush(minHeap, -num)
    #         if len(minHeap) > threshold:
    #             heapq.heappop(minHeap)
    #     return -minHeap[0]

#     方法二：quick sort
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        numLen = len(nums)
        threshold = numLen - k
        left, right, curPos = 0, numLen - 1, -1
        while curPos != threshold:
            curPos = self.partition(left, right)
            print(curPos)
            if curPos < threshold:
                left = curPos + 1
            elif curPos > threshold:
                right = curPos - 1

        return self.nums[threshold]


    def partition(self, low, high):
        def swap(lo, hi):
            # print(lo, hi)
            temp = self.nums[lo]
            self.nums[lo] = self.nums[hi]
            self.nums[hi] = temp

        pivot = random.choice(range(low, high + 1))
        # print(pivot, high)
        swap(pivot, high)
        left, right = low, high - 1
        while left < right:
            # print(left, right)
            # 注意这里两个判断条件都必须是>=/<=，因为要判断严格大于nums[pivot]的index
            while self.nums[left] <= self.nums[high] and left < right:
                left += 1
            while self.nums[right] >= self.nums[high] and left < right:
                right -= 1
            swap(left, right)
        if self.nums[high] < self.nums[left]:
            swap(high, left)
            return left
        return high





print(Solution().findKthLargest([3,2,1,5,6,4],2))