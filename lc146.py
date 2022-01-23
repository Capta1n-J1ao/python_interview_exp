

class Node:
    def __init__(self, key, value, pre = None, next = None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def addFirst(self, node):
        self.size += 1
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def remove(self, node):
        self.size -= 1
        node.next.pre = node.pre
        node.pre.next = node.next

    def removeLast(self):
        if self.size == 0:
            return None
        toDelete = self.tail.pre
        self.remove(toDelete)
        return toDelete

    def getSize(self):
        return self.size


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.doubleLinkedList = DoubleLinkedList()


    def get(self, key: int) -> int:
        # print(self.hashMap)
        if key not in self.hashMap:
            return -1
        curNodeVal = self.hashMap.get(key).value
        self.put(key, curNodeVal)
        return curNodeVal


    def put(self, key: int, value: int) -> None:
        curNode = Node(key, value)
        if key in self.hashMap:
            self.doubleLinkedList.remove(self.hashMap.get(key))
            self.doubleLinkedList.addFirst(curNode)
            self.hashMap[key] = curNode
        else:
            if self.doubleLinkedList.size >= self.capacity:
                lastNode = self.doubleLinkedList.removeLast()
                self.hashMap.pop(lastNode.key)
            self.doubleLinkedList.addFirst(curNode)
            self.hashMap[key] = curNode







# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
print(obj.put(1,1))
print(obj.put(2,2))
print(obj.get(1))
print(obj.put(3,3))
print(obj.get(2))
# param_1 = obj.get(key)
# obj.put(key,value)