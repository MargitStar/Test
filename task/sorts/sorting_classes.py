from abc import ABC, abstractmethod


class Sort(ABC):
    def __init__(self, array):
        self.array = array

    @abstractmethod
    def sorted(self):
        pass


class BubbleSort(Sort):
    def sorted(self):
        sorted_array = self.array[:]
        for i in range(len(sorted_array)):
            for j in range(len(sorted_array) - 1):
                if sorted_array[j] > sorted_array[j+1]:
                    sorted_array[j], sorted_array[j+1] = sorted_array[j+1], sorted_array[j]
        return sorted_array


clas
