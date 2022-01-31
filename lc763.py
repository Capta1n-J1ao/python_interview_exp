from typing import List

# 官解的python版本就很易懂
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        # print(type(s))
        res = []
        for i, ch in enumerate(s):
            if i > last[ord(ch) - ord('a')]:
                last[ord(ch) - ord('a')] = i
        # 方法一：明显复杂了
        # curRes = 0
        # curTail = 0
        # index = 0
        # while index < len(s):
        #     curTail = last[ord(s[index]) - ord('a')]
        #     temp = index
        #     while temp < curTail:
        #         temp += 1
        #         curTail = max(curTail, last[ord(s[temp]) - ord('a')])
        #     res.append(curTail - index + 1)
        #     index = curTail + 1

        # 方法二：
        preTail = curTail = 0
        for i, ch in enumerate(s):
            curTail = max(curTail, last[ord(ch) - ord('a')])
            if i == curTail:
                res.append(curTail - preTail + 1)
                preTail = curTail + 1

        return res

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))