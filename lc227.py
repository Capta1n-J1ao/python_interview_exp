import math
from collections import deque


# 参考链接，下面两个链接的图解都挺好，但是代码还是要参照正规的shunting yard algorithm来写
# https://leetcode-cn.com/problems/basic-calculator-ii/solution/shi-yong-shuang-zhan-jie-jue-jiu-ji-biao-c65k/
# https://leetcode-cn.com/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-shuang-zhan-chao-xi-s2ha/
# 我完全按照wiki里面的pseudo code写的,并且一定要注意优先级是大于等于，不能试大于，代码里面也会说明原因
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm
class Solution:
    def execution(self):
        # pay attention to name
        second = self.numStack.pop()
        first = self.numStack.pop()
        ops = self.opStack.pop()
        res = 0
        if ops == '+':
            res = first + second
        elif ops == '-':
            res = first - second
        elif ops == '*':
            res = first * second
        elif ops == '/':
            res = first / second
        elif ops == '^':
            res = math.pow(first, second)
        elif ops == '&':
            res = first % second
        self.numStack.append(int(res))

    def calculate(self, s: str) -> int:
        opPriority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '%': 2,
            '^': 100,
        }
        self.numStack, self.opStack = deque(), deque()
        # self.res = 0


        curPos = 0
        s = s.strip()
        s = '0' + s
        sLen = len(s)
        while curPos < sLen:
            # print(ord("a"))
            # print(type("a"))
            if s[curPos] == " ":
                curPos += 1
                continue
            if s[curPos] == '(':
                self.opStack.append(s[curPos])
            elif s[curPos] == ')':
                while self.numStack and self.opStack:
                    if self.opStack[-1] != '(':
                        self.execution()
                    else:
                        self.opStack.pop()
                        break
            elif s[curPos].isdigit():
                index = curPos + 1
                curNum = int(s[curPos])
                while index < sLen and s[index].isdigit():
                    curNum = curNum * 10 + int(s[index])
                    index += 1
                self.numStack.append(curNum)
                # ?????
                curPos = index - 1
            else:
                # opPriority[self.opStack[-1]] >= opPriority[s[curPos]很重要，具体参考"1-1+1"test case
                while self.opStack and self.opStack[-1] != '(' and opPriority[self.opStack[-1]] >= opPriority[s[curPos]]:
                    self.execution()
                self.opStack.append(s[curPos])
            curPos += 1
        while self.numStack and self.opStack:
            self.execution()
        return self.numStack[0]


# print(Solution().calculate("3+2*2"))
# print(Solution().calculate("3/2"))
# answer is 19
# print(Solution().calculate("3+ (2^3*2)"))
# print(Solution().calculate(" 3/2 "))
print(Solution().calculate("1-1+1"))
