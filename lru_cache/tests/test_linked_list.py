from lru_cache.linked_list import LinkedList


def test_insert():
    ll = LinkedList()
    ll.insert(5)
    assert ll._head is not None and ll._head.data == 5
