class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        v1Len, v2Len = len(v1), len(v2)
        for i in range(max(v1Len, v2Len)):
            if i > v1Len - 1:
                val1 = 0
            else:
                val1 = int(v1[i])
            if i > v2Len - 1:
                val2 = 0
            else:
                val2 = int(v2[i])
            if val1 > val2:
                return 1
            elif val2 > val1:
                return -1
        return 0
print(Solution().compareVersion("1.0.1", "1"))