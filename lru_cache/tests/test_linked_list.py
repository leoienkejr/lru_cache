from lru_cache.linked_list import LinkedList, LinkedListNode


def test_insert():
    ll = LinkedList()
    ll.insert(5)
    ll_head = getattr(ll, '_head')
    assert ll_head is not None and ll_head.data == 5
    assert ll_head.list_ref == ll


def test_is_empty():
    ll = LinkedList()
    assert ll.is_empty()

    ll.insert(4)
    assert not ll.is_empty()


def test_contains():
    ll = LinkedList()
    ll.insert(1)
    loose_node = LinkedListNode(data=1)

    assert ll.contains(getattr(ll, '_head'))
    assert not ll.contains(loose_node)


def test_move_to_head():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.move_to_head(getattr(ll, '_tail'))

    assert getattr(ll, '_head').data == 1
