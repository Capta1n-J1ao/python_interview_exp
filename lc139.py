from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sLen = len(s)
        wSet = set(wordDict)
        dp = [False for _ in range(sLen + 1)]
        dp[0] = True
        for i in range(1, sLen + 1):
            for k in range(i):
                curWord = s[k: i]
                if dp[k] and s[k: i] in wSet:
                    dp[i] = True
        return dp[sLen]

# print(Solution().wordBreak("leetcode", ["leet","code"]))
# print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))