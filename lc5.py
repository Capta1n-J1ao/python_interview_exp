class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        if sLen < 2 or (sLen == 2 and s[0] == s[1]):
            return s
        maxLen = 0
        res = s[0]
        dp = [[False for i in range(sLen)] for k in range(sLen)]
        for i in range(sLen):
            dp[i][i] = True
        for i in reversed(range(sLen)):
            for k in range(i + 1, sLen):
                if s[i] != s[k]:
                    dp[i][k] = False
                elif s[i] == s[k] and (dp[i + 1][k - 1] or (k - i) < 2):
                    # print(i, k)
                    dp[i][k] = True
                    if k - i + 1 > maxLen:
                        maxLen = k - i + 1
                        res = s[i: k + 1]
        return res

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("bbb"))