from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        numLen = len(nums)
        left, right = 0, numLen - 1
        while left < right:
            mid = int(left + (right - left + 1) / 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] <= target:
                left = mid
        return left + 1 if nums[left] < target else left

# correct answer = 2
# print(Solution().searchInsert([1,3,5,6], 5))
# correct answer = 1
print(Solution().searchInsert([1,3,5,6], 2))
# correct answer = 4
print(Solution().searchInsert([1,3,5,6], 7))
# correct answer = 0
print(Solution().searchInsert([1,3,5,6], 0))