from abc import ABC, abstractmethod

from .decorators import measure


class Sort(ABC):
    def __init__(self, array):
        self.array = array

    @abstractmethod
    def sorted(self):
        pass


class BubbleSort(Sort):
    @measure
    def sorted(self):
        sorted_array = self.array[:]
        for i in range(len(sorted_array)):
            for j in range(len(sorted_array) - 1):
                if sorted_array[j] > sorted_array[j + 1]:
                    sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
        return sorted_array


class OptimizedBubbleSort(Sort):
    @measure
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
    @measure
    def sorted(self):
        sorted_array = self.array[:]
        for i in range(1, len(sorted_array)):
            j = i - 1
            while j >= 0 and sorted_array[i] < sorted_array[j]:
                sorted_array[j + 1] = sorted_array[j]
                j -= 1
            sorted_array[j + 1] = sorted_array[i]
        return sorted_array


class MergeSort(Sort):
    @measure
    def sorted(self):
        sorted_array = self.array[:]

        def merge_sort(array):
            if len(array) > 1:
                middle = len(array) // 2
                left = array[:middle]
                right = array[middle:]

                merge_sort(left)
                merge_sort(right)

                i = j = k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        array[k] = left[i]
                        i += 1
                    else:
                        array[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    array[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    array[k] = right[j]
                    j += 1
                    k += 1
            return array

        return merge_sort(sorted_array)


def read_file(file):
    numbers = file.read().strip().split()
    new_numbers = [int(number) for number in numbers]
    return new_numbers


def write_file(array):
    from io import StringIO
    new_array = [str(number) for number in array]
    file = StringIO(" ".join(new_array))
    return file
