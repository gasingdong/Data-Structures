class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        self.storage[0], self.storage[self.get_size(
        ) - 1] = self.storage[self.get_size() - 1], self.storage[0]
        val = self.storage.pop()
        self._sift_down(0)
        return val

    def get_max(self):
        if self.storage:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent = (index - 1)//2
        while self.storage[index] > self.storage[parent] and parent >= 0:
            self.storage[index], self.storage[parent] = \
                self.storage[parent], self.storage[index]
            index = parent
            parent = (index - 1)//2

    def _sift_down(self, index):
        while index * 2 + 1 < self.get_size():
            first = index * 2 + 1
            second = index * 2 + 2
            largest = second if second < self.get_size(
            ) and self.storage[second] > self.storage[first] else first
            if self.storage[largest] > self.storage[index]:
                self.storage[index], self.storage[largest] = \
                    self.storage[largest], self.storage[index]
                index = largest
            else:
                break
