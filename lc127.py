from typing import List
from collections import *


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wLen = len(beginWord)
        wSet = set(wordList)
        queue = deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)
        res = 0
        if endWord not in wSet:
            return 0
        while len(queue) > 0:
            qLen = len(queue)
            res += 1
            for i in range(qLen):
                curWord = queue.popleft()
                for k in range(wLen):
                    for m in range(ord('a'), ord('z') + 1):
                        nextWord = curWord[:k] + chr(m) + curWord[k + 1:]
                        # print(nextWord)
                        if nextWord == endWord:
                            return res + 1
                        if nextWord in wSet and nextWord not in visited:
                            # print(i, nextWord)
                            queue.append(nextWord)
                            visited.add(nextWord)
        # 注意如果跑到这里说明就是没有符合的了
        return 0

print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))