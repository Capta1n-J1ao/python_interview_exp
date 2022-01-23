import re
from collections import defaultdict
from typing import List


class Solution:
    # 不允许用re库
    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     word = re.split("[ !?',;.]", paragraph)
    #     wDic = [w.lower() for w in word if len(w) > 0 and w.lower() not in banned]
    #     count = 0
    #     res = ''
    #     for w in wDic:
    #         curCount = wDic.count(w)
    #         if curCount > count:
    #             count = curCount
    #             res = w
    #     return res

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bSet = set(banned)
        para = paragraph.lower()
        curWord = ""
        res = ""
        count = -1
        wCount = defaultdict(int)
        for pChar in para:
            if ord('z') >= ord(pChar) >= ord('a'):
                curWord += pChar
            else:
                if curWord != '' and curWord not in bSet:
                    wCount[curWord] += 1
                    if wCount[curWord] > count:
                        count = wCount[curWord]
                        res = curWord
                curWord = ''
        if len(curWord) > 0:
            if curWord not in bSet:
                wCount[curWord] += 1
                if wCount[curWord] > count:
                    count = wCount[curWord]
                    res = curWord
        return res

print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))