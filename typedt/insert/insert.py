from algoritm.algoritm import Algoritms
from structures.data_struct import (ListStack, ListQueueSimple, ListDeque,
                                    LinkedList, DoublyLinkedList, OrderedListSimple,
                                    )

FIRST = Algoritms()
STACK = ListStack()
QUEUE = ListQueueSimple()
DEQUE = ListDeque()
LINKEDLST = LinkedList()
DOUBLE_LINKLST = DoublyLinkedList()
D2 = DoublyLinkedList()
ORDERED = OrderedListSimple()

TEXT_INS = 'Введите числа через пробел : '
TEXT_INSERT = 'd => документация, для ввода ваших значений => l, q <= Вернуться назад : '
TEXT_INSERT_STRUCTUR = 'd => документация, q <= Вернуться назад : '
ALGORITMS = {
    '1': ['пузырьковая сортировка', FIRST.bubblesort.__doc__, FIRST.bubblesort, 0],
    '2': ['сортировка выбором', FIRST.selection_sort.__doc__, FIRST.selection_sort, 0],
    '3': ['сортировка вставками', FIRST.insertion_sort.__doc__, FIRST.insertion_sort, 0],
    '4': ['сортировка слиянием', FIRST.mergesort.__doc__, FIRST.mergesort, 0],
    '5': ['быстрая сортировка', FIRST.quick_sort.__doc__, FIRST.quick_sort, 1],
    '6': ['двоичный поиск', FIRST.binary_search.__doc__, FIRST.binary_search, 2],
}
STRUCTURES = {
    '1': ['Stack', STACK.__doc__],
    '2': ['Queue', QUEUE.__doc__],
    '3': ['Deque', DEQUE.__doc__],
    '4': ['Linked list', LINKEDLST.__doc__],
    '5': ['Doubly link list', DOUBLE_LINKLST.__doc__],
    '6': ['Ordered', ORDERED.__doc__],
}


def response_for_structures(num: str):
    if num in STRUCTURES.keys():
        print(STRUCTURES[num][0])
        INSERT = input(TEXT_INSERT_STRUCTUR)
        if INSERT == 'd':
            return STRUCTURES[num][1]


def response_for_insert_sort(num: str):
    if num in ALGORITMS.keys():
        print(ALGORITMS[num][0])
        INSERT = input(TEXT_INSERT)
        if INSERT == 'd':
            return ALGORITMS[num][1]
        if INSERT == 'l':
            if ALGORITMS[num][3] == 2:
                INT = int(input('Введите число для поиска : '))
                INSERT_LIST = list(map(int, input(TEXT_INS).split()))
                return f'индекс = {ALGORITMS[num][2](INSERT_LIST, INT)}'
            else:
                INSERT_LIST = list(map(int, input(TEXT_INS).split()))
                if ALGORITMS[num][3]:
                    return ALGORITMS[num][2](INSERT_LIST)
                ALGORITMS[num][2](INSERT_LIST)
                return INSERT_LIST


def response_menu(INS):
    print('=' * 200)
    if INS in 'фаaf':
        with open('text/algoritm_text.txt') as file_a:
            print(file_a.read())
    else:
        with open('text/structures_text.txt') as file_a:
            print(file_a.read())

    try:
        while True:
            print('=' * 200)
            INSERT = input(
                f'Введите цифру {"алогоритма" if INS in "фаaf" else "структуры данных"} =>, q <= Вернуться назад : ')
            print('=' * 200)
            if INSERT in 'qй':
                break
            if not INSERT.isdigit():
                return 'только числа, через пробел'
            print(response_for_insert_sort(INSERT) if INS in 'фаaf' else response_for_structures(INSERT))

    except ValueError:
        print('!!!Вводить необходимо, только числа через пробел!!!')
