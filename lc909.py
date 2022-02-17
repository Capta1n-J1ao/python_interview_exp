from collections import deque
from typing import List

# 注意这里并不是每次只前进一步，而是用骰子决定的，也就是[1, 6]
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.bLen = len(board)

        queue = deque()
        queue.append((1, 0))
        visited = set()
        visited.add(1)
        self.flag = True
        self.target = self.bLen * self.bLen
        # goalRow, goalCol = self.indexCalc(self.bLen * self.bLen,  True if self.bLen % 2 == 1 else False)
        while queue:
            # for k in range(self.bLen):
            for _ in range(len(queue)):
                # print(len(queue))
                index, step = queue.popleft()


                row, col = self.indexCalc(index)
                # 注意这里的逻辑，如果!= -1， 那就代表梯子直接让他去对应的index了，直接更新，而不是把(board[row][col], step + 1)放入queue
                if board[row][col] != -1:
                    # 不能这么写
                    # queue.append((board[row][col], step + 1))
                #     应该这么写
                    index = board[row][col]
                if index >= self.target:
                    return step
                # dice has 6 dimensions
                for i in range(1, 7):
                    if index + i in visited:
                        continue
                    visited.add(index + i)
                    queue.append((index + i, step + 1))
        return -1

    def indexCalc(self, index):
        # curRow = self.bLen - (index / self.bLen)
        # curCol = ((index - 1) % self.bLen) + 1 if flag else (self.bLen - ((index - 1) % self.bLen) + 1)
        # return (int(curRow), int(curCol))
        r, c = (index - 1) // self.bLen, (index - 1) % self.bLen
        if r % 2 == 1:
            c = self.bLen - 1 - c
        return self.bLen - 1 - r, c

# answer is 4
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# board = [[-1, -1], [-1 ,3]]
# answer is 1
# board = [[-1,-1,-1],[-1,9,8],[-1,8,9]]
print(Solution().snakesAndLadders(board))