from typing import Any, Optional


class LinkedListNode:
    list_ref: Optional['LinkedList']
    previous: Optional['LinkedListNode']
    next: Optional['LinkedListNode']
    data: Any = None

    def __init__(self, data: Any):
        self.previous = None
        self.next = None
        self.data = data

    def is_middle_node(self) -> bool:
        return (self.previous is not None) and (self.next is not None)


class LinkedList:
    _head: LinkedListNode | None
    _tail: LinkedListNode | None
    length: int = 0

    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self) -> bool:
        return (self._head is None) and (self._tail is None)

    def contains(self, node: LinkedListNode) -> bool:
        return node.list_ref is self

    def insert(self, data: Any):
        """ Insert new node containing 'data'
        at the head of the linked list

        :param data: Data to be stored in the new node
        """

        node = LinkedListNode(data)
        node.list_ref = self

        if self.is_empty():
            self._head = node
            self._tail = self._head
        else:
            node.next = self._head
            self._head.previous = node  # type: ignore
            self._head = node

        self.length += 1

    def move_to_head(self, node: LinkedListNode):
        if node is self._head:
            return
        if node.is_middle_node():
            previous = node.previous
            next = node.next

            previous.next = next  # type: ignore
            next.previous = previous  # type: ignore

            node.previous = None
            node.next = self._head

            self._head = node
        else:
            previous = node.previous
            previous.next = None  # type: ignore

            self._tail = previous

            node.next = self._head
            node.previous = None
            self._head = node
