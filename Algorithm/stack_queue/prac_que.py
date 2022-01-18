from Algorithm.stack_queue.structures import Node, Stack, Queue


def test_node():
    assert Node(1, None).item == 1


def test_queue():
    """
    스택은
    1. push
    2. pop
    3.is_empty

    """

    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.pop() is None
    assert queue.is_empty()


test_node()
test_queue()