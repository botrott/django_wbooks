import random


def check_sorted(arr: list):
    '''проверка сортировки'''
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    else:
        return True


def random_lst():
    '''случайный список'''
    arr = list(range(10, 150))
    random.shuffle(arr)
    return arr
