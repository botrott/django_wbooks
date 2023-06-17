from functions.other import random_lst, check_sorted

from insert.insert import (ALGORITMS, STACK, QUEUE, DEQUE, LINKEDLST, DOUBLE_LINKLST,
                           D2, ORDERED)

NUM_1 = 12
NUM_2 = 3
STR_1 = 'stack'


def test_stack():
    STACK.push(NUM_1)
    STACK.push(NUM_2)
    STACK.push(STR_1)
    STACK.__len__()
    STACK.pop()
    STACK.isempty()
    return STACK.peek() + STACK.isempty()


def test_queue():
    QUEUE.enqueue(NUM_1)
    QUEUE.enqueue(NUM_2)
    QUEUE.enqueue(STR_1)
    QUEUE.dequeue()
    QUEUE.peek()
    QUEUE.__len__()
    QUEUE.isempty()
    return QUEUE.peek() + QUEUE.isempty()


def test_deque():
    DEQUE.addfirst(NUM_1)
    DEQUE.addlast(NUM_2)
    return int(DEQUE.__len__()) + DEQUE.removefirst() + DEQUE.removelast()


def test_linked_list():
    LINKEDLST.addfirst(NUM_1)
    LINKEDLST.addfirst(NUM_2)
    return LINKEDLST.removefirst()


def test_double_linked_list():
    DOUBLE_LINKLST.addfirst(1)
    DOUBLE_LINKLST.addlast(2)
    res = DOUBLE_LINKLST.removefirst()
    res2 = DOUBLE_LINKLST.removelast()
    assert res == 1
    assert res2 == 2
    DOUBLE_LINKLST.addfirst(NUM_2)
    DOUBLE_LINKLST.addlast(4)
    D2.addfirst(10)
    D2.addlast(20)
    D2.addlast(34)
    D2.iadd(DOUBLE_LINKLST)
    return D2.__len__()


def test_ordered_list():
    ORDERED.add(NUM_1)
    ORDERED.add(NUM_2)
    assert ORDERED.__getitem__(1) == NUM_1
    assert ORDERED.__contains__(NUM_1) == True
    ORDERED.remove(NUM_1)
    assert ORDERED.__contains__(NUM_1) == False
    return ORDERED.__len__()


def test_structure():
    try:
        assert test_stack() == NUM_2
        assert test_queue() == NUM_2
        assert test_deque() == 17
        assert test_double_linked_list() == 5
        assert test_ordered_list() == 1
    except AssertionError:
        return f'error test_structure'
    return 'OK test_structure'


def test_algoritms():
    error = ''
    try:
        for key, value in ALGORITMS.items():
            if 0 in value:
                RANDOM_LIST = random_lst()
                ALGORITMS[key][2](RANDOM_LIST)
                if check_sorted(RANDOM_LIST) == False:
                    error = ALGORITMS[key][0]
                assert check_sorted(RANDOM_LIST)
            if 1 in value:
                if check_sorted(ALGORITMS[key][2](random_lst())) == False:
                    error = ALGORITMS[key][0]
                assert check_sorted(ALGORITMS[key][2](random_lst()))
            if 2 in value:
                error = ALGORITMS[key][0]
                assert (ALGORITMS[key][2]([2, 3, 4, 11], 12)) == False
                assert (ALGORITMS[key][2]([2, 3, 4, 11], 2)) == True

    except AssertionError:
        return f'Error in assert {error}'
    else:
        return 'OK test_algoritms'


if __name__ == '__main__':
    print(test_algoritms())
    print(test_structure())
