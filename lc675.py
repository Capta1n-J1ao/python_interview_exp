from collections import deque
from typing import List

# 这道题目主要是要注意一个点，那就是整个迷宫可以不用一条线走完，可以由折回，前提是保证树的高度是顺序的
class Solution:
    # row = None
    # col = None
    def cutOffTree(self, forest: List[List[int]]) -> int:
        self.row, self.col = len(forest), len(forest[0])
        self.forest = forest
        toGo = []
        for i in range(self.row):
            for k in range(self.col):
                if forest[i][k] > 1:
                    toGo.append((forest[i][k], i, k))
        toGo.sort()
        res = 0
        sRow, sCol = 0, 0
        for fHeight, gRow, gCol in toGo:
            curRes = self.BFS(sRow, sCol, gRow, gCol)
            if curRes == -1:
                return -1
            res += curRes
            sRow, sCol = gRow, gCol
        return res

    def BFS(self, sRow, sCol, gRow, gCol):
        queue = deque()
        queue.append((sRow, sCol))
        visited = [[False for i in range(self.col)] for k in range(self.row)]
        visited[sRow][sCol] = True
        res = 0
        while queue:
            qLen = len(queue)
            # res += 1
            for i in range(qLen):
                curRow, curCol = queue.popleft()
                if curRow == gRow and curCol == gCol:
                    return res
                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    dx = curRow + x
                    dy = curCol + y
                    if 0 <= dx < self.row and 0 <= dy < self.col and self.forest[dx][dy] >= 1 and not visited[dx][dy]:
                        queue.append((dx, dy))
                        visited[dx][dy] = True
            res += 1
        return -1



print(Solution().cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))

