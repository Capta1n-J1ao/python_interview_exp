# from typing import List
from collections import deque


def shortestPathBinaryMatrix(grid):
    gLen = len(grid)
    if not grid or grid[0][0] == 1 or grid[gLen - 1][gLen - 1] == 1:
        return -1
    elif gLen <= 2:
        return gLen
    queue = deque()
    queue.appendleft((0, 0))
    # visited = [[False] * gLen for _ in range(gLen)]
    visited = [[False for _ in range(gLen)] for _ in range(gLen)]
    visited[0][0] = True
    # visited = {(0, 0): True}
    step = 1
    while queue:
        step += 1
        for _ in range(len(queue)):
            i, k = queue.pop()
            for x, y in [(-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1)]:
                dx, dy = i + x, k + y
                if dx == gLen - 1 and dy == gLen - 1:
                    return step
                if 0 <= dx < gLen and 0 <= dy < gLen and grid[dx][dy] == 0 and not visited[dx][dy]:
                    queue.appendleft((dx, dy))
                    visited[dx][dy] = True
                # print("dx = ", dx, "dy = ", dy, "grid = ", grid[dx][dy])
    return -1


print(shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
