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
                if sorted_array[j] > sorted_array[j + 1]:
                    sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
        return sorted_array


class OptimizedBubbleSort(Sort):
    def sorted(self):
        has_swapped = True
        sorted_array = self.array[:]
        while has_swapped:
            has_swapped = False
            for i in range(len(sorted_array) - 1):
                if sorted_array[i] > sorted_array[i + 1]:
                    sorted_array[i], sorted_array[i + 1] = sorted_array[i + 1], sorted_array[i]
                    has_swapped = True

        return sorted_array


class InsertionSort(Sort):
    def sorted(self):
        sorted_array = self.array[:]
        for i in range(1, len(sorted_array)):
            j = i - 1
            while j >= 0 and sorted_array[i] < sorted_array[j]:
                sorted_array[j + 1] = sorted_array[j]
                j -= 1
            sorted_array[j + 1] = sorted_array[i]
        return sorted_array
