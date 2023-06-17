class ListStack:
    """===Абстрактный тип данных(АТД) Stack===
push(item) – добавление нового элемента в стек.
pop() – удаление и возврат очередного элемента в порядке «последним во-
шел, первым вышел» (Last In First Out – LIFO).
peek() – возврат очередного элемента в порядке «последним вошел, пер-
вым вышел» (LIFO).
__len()__ – возврат числа элементов в стеке (будет использоваться метод
в стиле Python __len__).
isempty() – возврат True, если в стеке нет элементов, иначе возврат False.
"""

    def __init__(self):
        self.arr = []

    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[-1]

    def __len__(self):
        return len(self.arr)

    def isempty(self):
        return len(self) == 0


class ListQueueSimple:
    """===АТД Queue(очередь)===
enqueue(item) – добавление нового элемента в очередь.
dequeue() – удаление и возврат очередного элемента в порядке «первым
вошел, первым вышел» (First In First Out – FIFO).
peek() – возврат (без удаления) очередного элемента в очереди в поряд-
ке FIFO.
__len()__ – возврат числа элементов в очереди.
isempty() – возврат True, если в очереди нет элементов, иначе возврат
False.
"""

    def __init__(self):
        self.arr = []

    def enqueue(self, item):
        self.arr.append(item)

    def dequeue(self):
        return self.arr.pop(0)

    def peek(self):
        return self.arr[0]

    def __len__(self):
        return len(self.arr)

    def isempty(self):
        return len(self) == 0


class ListDeque:
    """===АТД Deque(дек)===
addfirst(item) – добавляет элемент item в начало дека.
addlast(item) – добавляет элемент item в конец дека.
removefirst(item) – удаляет и возвращает первый элемент в деке.
removelast(item) – удаляет и возвращает последний элемент в деке.
len – возвращает число элементов в деке.
"""

    def __init__(self):
        self.arr = []

    def addfirst(self, item):
        self.arr.insert(0, item)

    def addlast(self, item):
        return self.arr.append(item)

    def removefirst(self):
        return self.arr.pop(0)

    def removelast(self):
        return self.arr.pop()

    def __len__(self):
        return len(self.arr)


class ListNode:
    """узел для АТД связные списки"""

    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    """===АКД связный список===
addfirst(item) - добавляет элемент item в начало.
removefirst() – удаляет и возвращает первый элемент.
"""

    def __init__(self):
        self.head = None

    def addfirst(self, item):
        self.head = ListNode(item, self.head)

    def removefirst(self):
        item = self.head.data
        self.head = self.head.link
        return item


class ListNodeDoubly:
    def __init__(self, data, prev=None, link=None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self


class DoublyLinkedList:
    """===АТД двухсвязный список(double linked list)===
__len()__ – возвращает число элементов в списке.
addbetween(item, before, after) - добавляет элемент iter между before and after.
addfirst(item) - добавляет элемент item в начало.
addfirst(item) - добавляет элемент item в конец.
remove(item, before, after)– удаляет элемент iter между before and after.
removefirst() - удаляет элемент item в началe.
removelast() - удаляет элемент item в концe.
iadd(other) - конкатенация двухсвязных списков (быстрее чем в других списках).
"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def addbetween(self, item, before, after):
        node = ListNodeDoubly(item, before, after)
        if after is self.head:
            self.head = node
        if before is self.tail:
            self.tail = node
        self.length += 1

    def addfirst(self, item):
        self.addbetween(item, None, self.head)

    def addlast(self, item):
        self.addbetween(item, self.tail, None)

    def remove(self, node):
        before, after = node.prev, node.link
        if node is self.head:
            self.head = after
        else:
            before.link = after
        if node is self.tail:
            self.tail = before
        else:
            after.prev = before
        self.length -= 1
        return node.data

    def removefirst(self):
        return self.remove(self.head)

    def removelast(self):
        return self.remove(self.tail)

    def iadd(self, other):
        if other.head is not None:
            if self.head is None:
                self.head = other.head
            else:
                self.tail.link = other.head
                other.head.prev = self.tail
            self.tail = other.tail
            self.length = self.length + other.length
        return self


class OrderedListSimple:
    """===АТД упорядоченный список===
add(item) – добавляет элемент item в список.
remove(item) – удаляет первый найденный экземпляр элемента item из
списка. Если элемента item нет в списке, то генерируется исключение
ValueError.
__getitem__(index) – возвращает элемент с заданным индексом index из
отсортированного списка. Эта операция также известна как выбор (se-
lection).
__contains__(item) – возвращает значение True, если в списке существу-
ет элемент, равный item(return item in self.arr), можно заменить двоичным поиском
__iter__ – возвращает итератор для упорядоченного списка, который
передает элементы в отсортированном порядке.
__len__ – возвращает длину упорядоченного списка.
"""

    def __init__(self):
        self.arr = []

    def add(self, item):
        self.arr.append(item)
        self.arr.sort()

    def remove(self, item):
        self.arr.remove(item)

    def __getitem__(self, index):
        return self.arr[index]

    def __contains__(self, item):
        left, right = 0, len(self.arr)
        while right - left > 1:
            median = (right + left) // 2
            if item < self.arr[median]:
                right = median
            else:
                left = median
        return right > left and self.arr[left] == item

    def __len__(self):
        return len(self.arr)

    def __iter__(self):
        return iter(self.arr)


class Tree:
    """===АТД дерево(tree)===
__init__(L) – инициализирует новое дерево заданным списком списков.
Используется то же соглашение: первый элемент списка – это данные,
все последующие элементы (если они существуют) – его прямые потомки.
height() – возвращает высоту дерева.
__str__() – возвращает строку, представляющую все дерево в целом.
__eq__(other) – возвращает True, если данное дерево равно другому дереву other.
Это означает, что они оба содержат одинаковые данные и их
потомки равны (и расположены в одинаковом порядке).
__contains__(k) – возвращает True, если и только если дерево содержит
данные k либо в корне, либо в одном из его потомков. Иначе возвращает
False.
preorder() – возвращает итератор по данным в дереве, который выдает
значения в соответствии с прямым порядком обхода (preorder traversal)
дерева.
postorder() – возвращает итератор по данным в дереве, который вы-
дает значения в соответствии с обратным порядком обхода (postorder
traversal) дерева.
__iter__() – псевдоним для метода preorder.
layerorder() – возвращает итератор по данным в дереве, который выдает
значения в соответствии с поуровневым порядком обхода (layer order
traversal) дерева.
"""

    def __init__(self, arr):
        iterator = iter(arr)
        self.data = next(iterator)
        self.children = [Tree(i) for i in iterator]

    def _listwithlevels(self, level, trees):
        trees.append(' ' * level + str(self.data))
        for child in self.children:
            child._listwithlevels(level + 1, trees)

    def __str__(self, level=0):
        """обход дерева"""
        trees = []
        self._listwithlevels(0, trees)
        return '\n'.join(trees)

    def __eq__(self, other):
        """являются ли равными(==) два дерева(имеют одинаковую форму и данные)"""
        return self.data == other.data and self.children == other.children

    def height(self):
        """высота дерева"""
        if len(self.children) == 0:
            return 0
        else:
            return 1 + max(child.height() for child in self.children)

    def __contains__(self, k):
        """позволяет воспользоваться (in)для проверки присутствия элемента в наборе данных."""
        return self.data == k or any(k in child for child in self.children)

    def preorder(self):
        """итерационный проход по деревьям (т. е. по их узлам)"""
        yield self
        for child in self.children:
            for descendant in child.preorder():
                yield descendant

    def _postorder(self):
        node, childiter = self, iter(self.children)
        stack = [(node, childiter)]
        while stack:
            node, childiter = stack[-1]
            try:
                child = next(childiter)
                stack.append((child, iter(child.children)))
            except StopIteration:
                yield node
                stack.pop()

    def postorder(self):
        return (node.data for node in self._postorder())

    def _layerorder(self):
        """обхода дерева по уровням (уровень за уровнем)"""
        node, childiter = self, iter(self.children)
        queue = ListQueueSimple()
        queue.enqueue((node, childiter))
        while queue:
            node, childiter = queue.peek()
            try:
                child = next(childiter)
                queue.enqueue((child, iter(child.children)))
            except StopIteration:
                yield node
                queue.dequeue()

    def layerorder(self):
        return (node.data for node in self._layerorder())
