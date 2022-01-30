import heapq

# 这道题目的核心就是无论插入什么数两个大小顶堆都必须要经过一下
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []


    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.minHeap, num)
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.maxHeap, -num)
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))



    def findMedian(self) -> float:
        totalNum = len(self.minHeap) + len(self.maxHeap)
        if totalNum % 2 == 1:
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(-1)
obj.addNum(-2)
obj.addNum(-3)
param_1 = obj.findMedian()
print(param_1)
obj.addNum(-4)
obj.addNum(-5)
param_2 = obj.findMedian()
print(param_2)