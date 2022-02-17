from typing import List

# 按照lc46 -> lc60 -> lc212的顺序可以写一遍
# 针对python进行深拷贝的在刷题的时候有两种方法：
# 1. 使用slicing，也就是self.res.append(curList[:])
# 2. 在更新curList的时候使用curList + [元素]的形式，这样在Python的语法里面其实是新建一个list的


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.numLen = len(nums)
        self.res = []
        self.visited = [False for _ in range(self.numLen)]
        self.backTracking([])
        return self.res

    # slicing写法
    def backTracking(self, curList):
        if len(curList) == self.numLen:
            self.res.append(curList[:])
            return
        for i in range(self.numLen):
            if self.visited[i]:
                continue
            curList.append(self.nums[i])
            # print(curList)
            self.visited[i] = True
            self.backTracking(curList)
            curList.pop()
            self.visited[i] = False

    # curList + [元素]写法， 注意区别
    # def backTracking(self, curList):
    #     if len(curList) == self.numLen:
    #         # 对应append版本
    #         # self.res.append(curList[:])
    #         self.res.append(curList)
    #         return
    #     for i in range(self.numLen):
    #         if self.visited[i]:
    #             continue
    #         self.visited[i] = True
    #         self.backTracking(curList + [self.nums[i]])
    #         # 关键在这里
    #         # curList.pop()
    #         self.visited[i] = False


print(Solution().permute([1,2,3]))


