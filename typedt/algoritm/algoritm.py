class Algoritms:

    def bubblesort(self, arr):
        '''===пузырьковая сортировка===
def bubblesort(self, arr):
    for iteration in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]'''
        for iteration in range(len(arr) - 1):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

    def selection_sort(self, arr: list):
        '''===сортировка выбором===
def selection_sort(self, arr: list):
    new_arr = len(arr)
    for i in range(len(new_arr - 1)):
        max_index = 0
        for index in range(new_arr - i):
            if arr[index] > arr[max_index]:
                max_index = index
        arr[n-i-1], arr[max_index] = arr[max_index], arr[n-i-1]'''
        n = len(arr)
        for i in range(n - 1):
            max_index = 0
            for index in range(n - i):
                if arr[index] > arr[max_index]:
                    max_index = index
            arr[n - i - 1], arr[max_index] = arr[max_index], arr[n - i - 1]

    def insertion_sort(self, arr: list):
        """===сортировка вставками===
def insertion_sort(self, arr: list):
    n = len(arr)
            for i in range(n):
                for j in range(n - i - 1, n-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]"""
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1, n - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def quick_sort(self, arr):
        '''===быстрая сортировка===
def quick_sort(self, arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return self.quick_sort(less) + [pivot] + self.quick_sort(greater)'''
        if len(arr) < 2:
            return arr
        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]
            return self.quick_sort(less) + [pivot] + self.quick_sort(greater)

    def mergesort(self, arr: list):
        """===сортировка слиянием===
def mergesort(self, arr: list):
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    A = arr[:mid]
    B = arr[mid:]
    self.merge(A, B, arr)

def merge(self, A: list, B: list, arr: list):
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            arr[i+j] = A[i]
            i += 1
        else:
            arr[i+j] = B[j]
            j += 1
"""
        if len(arr) < 2:
            return
        mid = len(arr) // 2
        A = arr[:mid]
        B = arr[mid:]
        self.mergesort(A)
        self.mergesort(B)
        self.merge(A, B, arr)

    def merge(self, A: list, B: list, arr: list):
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                arr[i + j] = A[i]
                i += 1
            else:
                arr[i + j] = B[j]
                j += 1
            arr[i + j:] = A[i:] + B[j:]

    def binary_search(self, arr: list, item: int | float):
        """===двоичный поиск===
def binary_search(self, arr: list, item: int|float):
    if len(arr) == 0:
        return False
    median = len(arr) // 2
    if item == arr[median]:
        return True
    elif item < arr[median]:
        return self.binary_search(arr[:median], item)
    else:
        return self.binary_search(arr[median + 1:], item)
"""
        low = 0
        hight = len(arr) - 1
        while low <= hight:
            mid = (low + hight)
            guess = arr[mid]
            if guess == item:
                return mid
            if guess > item:
                hight = mid - 1
            else:
                low = mid + 1
        return False
