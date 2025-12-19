class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next

class LinkedList:
    def __init__(self, values=None):
        self._head = None
        if values:
            for value in values:
                self.push(value)
        

    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = current.next()

    def __len__(self):
        counter = 0
        current = self._head
        while current:
            counter += 1
            current = current.next()
        return counter

    def head(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        node = Node(value)
        node._next = self._head
        self._head = node

    def pop(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        node = self._head
        val = node.value()
        next = node.next()
        self._head = next
        return val

    def reversed(self):
        new_list = LinkedList()
        current = self._head
        while current:
            new_list.push(current.value())
            current = current.next()
        return new_list
            
            
