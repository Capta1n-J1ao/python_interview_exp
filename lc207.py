from collections import deque
from typing import List


# https://leetcode-cn.com/problems/course-schedule/solution/tuo-bu-pai-xu-by-liweiwei1419/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pLen = len(prerequisites)
        if pLen == 0:
            return True
        inDegree = [0 for _ in range(numCourses)]
        preCourseList = [set() for _ in range(numCourses)]
        for prerequisite in prerequisites:
            post, pre = prerequisite[0], prerequisite[1]
            inDegree[post] += 1
            preCourseList[pre].add(post)

        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        #  if cycle, return false
        if not queue:
            return False

        counter = 0
        while queue:
            qLen = len(queue)
            for i in range(qLen):
                curCourse = queue.popleft()
                counter += 1
                for postCourse in preCourseList[curCourse]:
                    inDegree[postCourse] -= 1
                    if inDegree[postCourse] == 0:
                        queue.append(postCourse)
        return counter == numCourses
