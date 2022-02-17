
# 按照lc46 -> lc60 -> lc212的顺序可以写一遍
# 非常重要的知识点：str 在 Python 中将非列表转换为字符串
# https://www.delftstack.com/zh/howto/python/how-to-convert-a-list-to-string/
# 因为是接着lc46做的，所以方法一套用了backtracking的方法，超时了，应该要做一下处理
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.n = n
        self.k = k
        self.res = []
        self.visited = [False for _ in range(self.n + 1)]
        self.factorial = [1 for _ in range(self.n + 1)]
        for i in range(2, n + 1):
            self.factorial[i] = i * self.factorial[i - 1]
        self.backTracking(self.res, k, 0)
        # print(self.res)
        return "".join(map(str, self.res))


    def backTracking(self, curList:list, curIndex, curLayer):
        if len(curList) == self.n:
            # self.res.append(curList[:])
            return
        # 注意 最后的-1
        leafCut = self.n - curLayer - 1
        # print(leafCut)
        for i in range(1, self.n + 1):
            if self.visited[i]:
                continue
            if curIndex - self.factorial[leafCut] > 0:
                curIndex -= self.factorial[leafCut]
                # self.backTracking(curList, curIndex, curLayer)
                continue
            curList.append(i)
            self.visited[i] = True
            # print(curList)
            self.backTracking(curList, curIndex, curLayer + 1)
            # 不能回溯，因为根据这个算法得到的第一个答案就是正确答案
            # curList.pop()
            # self.visited[i] = False


# print(type(Solution().getPermutation(3, 3)))
# 213
# print(Solution().getPermutation(3, 3))
# 2314
print(Solution().getPermutation(4, 9))
# 194627853
# print(Solution().getPermutation(9, 37098))
