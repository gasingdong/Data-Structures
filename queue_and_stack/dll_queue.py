import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList  # nopep8


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        node = None
        if self.size > 0:
            node = self.storage.remove_from_head()
            self.size -= 1
        return node

    def len(self):
        return self.size
