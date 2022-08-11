from typing import Any, Optional


class LinkedListNode:
    _list_ref: Optional['LinkedList']
    _previous: Optional['LinkedListNode']
    _next: Optional['LinkedListNode']
    data: Any = None

    def __init__(self, data: Any):
        self._previous = None
        self._next = None
        self.data = data

    def is_middle_node(self) -> bool:
        return (self._previous is not None) and (self._next is not None)


class LinkedList:
    _head: LinkedListNode | None
    _tail: LinkedListNode | None
    length: int = 0

    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self) -> bool:
        return (self._head is None) and (self._tail is None)

    def insert(self, data: Any):
        """ Insert new node containing 'data'
        at the head of the linked list

        :param data: Data to be stored in the new node
        """

        node = LinkedListNode(data)
        node._list_ref = self

        if self.is_empty():
            self._head = node
            self._tail = self._head
        else:
            node._next = self._head
            self._head._previous = node  # type: ignore
            self._head = node

        self.length += 1

    def move_to_head(self, node: LinkedListNode):
        if node is self._head:
            return
        if node.is_middle_node():
            previous = node._previous
            next = node._next

            previous._next = next  # type: ignore
            next._previous = previous  # type: ignore

            node._previous = None
            node._next = self._head

            self._head = node
        else:
            previous = node._previous
            previous._next = None  # type: ignore

            self._tail = previous

            node._next = self._head
            node._previous = None
            self._head = node
