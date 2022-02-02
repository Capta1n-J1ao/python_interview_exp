from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        numLen = len(nums)
        if numLen == 0:
            return [-1, -1]
        # if nums[0] == nums[numLen - 1]:
        #     return nums
        left, right = 0, numLen - 1
        while left < right:
            mid = int(left + (right - left) / 2)
            # print(mid)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid
        if nums[left] != target:
            return [-1, -1]
        rBoundary = left
        while rBoundary < numLen and nums[rBoundary] == nums[left]:
            rBoundary += 1
        return [left, rBoundary - 1]

# print(Solution().searchRange([5,7,7,8,8,10], 8))
# print(Solution().searchRange([5,7,7,8,8,10], 6))
print(Solution().searchRange([1], 0))
print(Solution().searchRange([1], 1))