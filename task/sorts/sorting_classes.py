from abc import ABC, abstractmethod


class Sorting(ABC):
    def __init__(self, array):
        self.array = array

    @abstractmethod
    def sorted(self):
        return sorted(self.array)

