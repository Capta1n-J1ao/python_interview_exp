from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 此类sorted函数类似于java里面的comparator，
        # 不要把他分开写在主函数外面，而应该直接写在主函数里面，让代码可读性更强
        def sortHelper(log: str) -> tuple:
            lId, lContext = log.split(" ", 1)
            if lContext[0].isalpha():
                return 0, lContext, lId
            else:
                return 1,

        return sorted(logs, key=sortHelper)


print(Solution().reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
