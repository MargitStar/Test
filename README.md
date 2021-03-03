## 1. Implement a hierarchy of classes
Parent class is an abstract sorting class. It is inherited by 4 classes:
* BubbleSort
* OptimizedBubbleSort
* MergeSort
* InsertionSort

Every child overrides `sorted` method with the corresponding sorting algorithm.

## 2. Create a decorator that measures the time of execution
Decorator `@measure` measures the time of function execution.
It prints the measured time to the console, since `sorted` method returns a sorted array,
which interferes with returning the execution time. To store the execution time in the DB,
we could choose to use `sort` method which would sort the array stored in the class and return None originally.
We could then use the decorator to return the execution time instead.

[comment]: <> (## 3. Django model and admin section)