from lru_cache.linked_list import LinkedList


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
