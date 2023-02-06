from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if len(self.list) == 0:
            return None
        return self.list.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.list):
            raise IndexError("Index out of range")
        return self.list[index]
