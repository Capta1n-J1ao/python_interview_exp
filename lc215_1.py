import heapq
import random
from typing import List


# 其他视频都不好，还是参考原来的视频
# https://www.bilibili.com/video/BV15Z4y1p7KR?t=412
# lc295_1是一个基于quick sort对于数组的排序
class Solution:
    # 实现完整快排
    def quick_sort(self, nums: List[int], low, high):
        self.nums = nums
        numLen = len(nums)
        if low != high:
            curPos = self.partition(low, high)
            # print(low, high, curPos)
            if curPos > 0 and low < curPos - 1:
                self.quick_sort(nums, low, curPos - 1)
            if curPos < high and curPos + 1 < high:
                self.quick_sort(nums, curPos + 1, high)
        return self.nums

    def partition(self, low, high):
        def swap(lo, hi):
            # print(lo, hi)
            temp = self.nums[lo]
            self.nums[lo] = self.nums[hi]
            self.nums[hi] = temp

        print(low, high + 1)
        pivot = random.choice(range(low, high + 1))
        print(pivot)
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


print(Solution().quick_sort([3, 2, 1, 5, 6, 4], 0, 5))
