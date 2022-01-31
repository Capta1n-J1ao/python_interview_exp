from collections import *
from typing import List

# 参考题解：
# https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode-solution-tuvc/
class Solution:
    # def trap(self, height: List[int]) -> int:
    #     hLen = len(height)
    #     leftHeighest = [height[0]] + [0] * (hLen - 1)
    #     rightHeighest = [0] * (hLen - 1) + [height[-1]]
    #     res = 0
    #     for i in range(1, hLen):
    #         leftHeighest[i] = max(leftHeighest[i - 1], height[i - 1])
    #     for i in range(hLen - 2, -1, -1):
    #         rightHeighest[i] = max(rightHeighest[i + 1], height[i + 1])
    #     for i in range(1, hLen - 1):
    #         curTrap = min(leftHeighest[i], rightHeighest[i]) - height[i]
    #         if curTrap > 0:
    #             res += curTrap
    #     return res

    def trap(self, height: List[int]) -> int:
        hLen = len(height)
        stack = deque()
        stack.append(0)
        res = 0
        for i in range(1, hLen):
            # print(i)
            # if height[i] > height[stack[-1]]:
            # print(len(stack))
            while len(stack) > 0 and height[i] > height[stack[-1]]:
            # while stack:
                # print(height[i], height[stack[-1]])
                curCol = stack.pop()
                # print(curCol)
                if len(stack) == 0:
                    break
                preCol = stack[-1]
                # print(preCol)
                curWidth = i - preCol - 1
                # print(min(height[i], height[preCol]))
                curHeight = min(height[i], height[preCol]) - height[curCol]
                res += curWidth * curHeight
            stack.append(i)

        return res




# the answer is 9
print(Solution().trap([4,2,0,3,2,5]))