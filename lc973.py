import heapq
from typing import List


class Solution:
    def __init__(self):
        self.a = 1
        self.b = 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            curDist = -self.dist(x, y)
            if len(heap) < k:
                heapq.heappush(heap, (curDist, point))
            else:
                if curDist > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (curDist, point))

        return [_[1] for _ in heap]

    def dist(self, x, y):
        return x * x + y * y



# s = Solution()
# print(s.kClosest([[1, 3], [-2, 2]], 1))
# print(Solution().kClosest([[1, 3], [-2, 2]], 1))



ret = 0

def dfs():
    dfs()
    global ret
    ret += 1


def func_a():
    a = 1
    def func_b():
        nonlocal a
        a += 1
        print(a)
    func_b()

func_a()