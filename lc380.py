import random


class RandomizedSet:

    def __init__(self):
        self.hashMap = dict()
        self.list = list()

    def insert(self, val: int) -> bool:
        if val in self.hashMap.keys():
            return False
        self.list.append(val)
        self.hashMap[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap.keys():
            return False
        rmIndex = self.hashMap.get(val)
        rmVal = self.list[rmIndex]
        updateVal = self.list[-1]
        self.list[rmIndex] = updateVal
        self.hashMap[updateVal] = rmIndex
        self.list.pop()
        # del self.hashMap[val]
        self.hashMap.pop(val)
        return True


    def getRandom(self) -> int:
        return random.choice(self.list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()