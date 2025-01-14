import pytest
from src.heap import Heap

@pytest.fixture
def heap() :
    return Heap()

def teat_heap_is_empty(heap) :
    assert heap.is_empty() == True 


def test_heap_insert_and_remove_min(heap):

    heap.insert(10)
    heap.insert(5)
    heap.insert(20)

    assert heap.remove_min() == 5
    assert heap.remove_min() == 20
    assert heap.remove_min() == 20

    assert heap.is_empty() == True

