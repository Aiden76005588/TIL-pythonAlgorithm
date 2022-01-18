from Algorithm.stack_queue.structures import Queue


def get_card(num):
    # 1. 제일 위 카드를 버린다.
    # 2. 그걸 제일 뒤로 옮긴다
    # 3. 한 장 남은 카드를 반환한다.

    queue = Queue([1,2,3,4,... ])
    while len(queue) >1:

        # 1. 제일 위 카드를 버린다.
        front = queue.pop()
        # 2. 그 다음 제일 위 카드를 제일 위로 옮긴다
        queue.push(queue.pop())
        # 3. 한 장 남은 카드를 반환한다.
        return queue.pop()