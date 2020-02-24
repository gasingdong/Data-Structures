import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList  # nopep8


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        node = None
        if self.size > 0:
            node = self.storage.remove_from_tail()
            self.size -= 1
        return node

    def len(self):
        return self.size
