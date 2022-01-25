from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            toFind = target - nums[i]
            if toFind in dic:
                return [dic[toFind], i]
            else:
                dic[nums[i]] = i