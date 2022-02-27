from collections import *
from typing import List

# 国内题解太少，找了个国外参考，思路可以参考liweiwei，再结合代码容易看懂,而且这个方法是类似于先正向求一遍路径，然后反向DFS
# https://leetcode.com/problems/word-ladder-ii/discuss/352661/Simple-Python-BFS-solution-(similar-problems-listed)
# liweiwei思路，用level的原因就是在于要把他理解为一个图，如果不是最短路径光靠visited极有可能绕一个圈转换到同层的单词，需要特别注意
# https://leetcode-cn.com/problems/word-ladder-ii/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you--2/

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        res = []
        if endWord not in wordSet:
            return res
        curLevel = {beginWord}
        parents = defaultdict(list)
        while curLevel:
            wordSet -= curLevel
            nextLevel = set()
            for word in curLevel:
                # print(curLevel)
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        curWord = word[:i] + ch + word[i + 1:]
                        if curWord in wordSet:
                            parents[curWord].append(word)
                            nextLevel.add(curWord)
            # 个人感觉放在最后应该也可以
            if endWord in nextLevel:
                break
            curLevel = nextLevel

#         反向DFS
        def DFS(word, path:list):
            path += [word]
            if word == beginWord:
                # path += [word]
                # https://www.programiz.com/python-programming/methods/list/reverse
                # The reverse() method doesn't return any value. It updates the existing list
                # 因此不能像下面这么用
                # res.append(path.reverse())
                # 但是可以这么用，太麻烦了
                # temp = path + [word]
                # temp.reverse()
                # res.append(temp[:])
                res.append(path[::-1])
                return
            else:
                for parentWord in parents[word]:
                    DFS(parentWord, path[:])
        DFS(endWord, [])
        return res

wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().findLadders("hit", "cog", wordList))
