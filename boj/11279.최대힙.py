import heapq
import sys

number = int(input())
heap = []  # 배열
# 연산의 개수만큼 반복한다.
for _ in range(number):
    num = int(sys.stdin.readline())
    # x가 0이라면 배열에서 가장 작은 값을 출력한다.
    if num == 0:
        if heap:
            # - 해주어 힙 푸시를 했기 때문에 - 부호를 붙여 출력한다.
            print(-heapq.heappop(heap))
        else:
            # 배열이 비어 있으면 0을 출력한다.
            print(0)
    else:
        # x가 0이 아니라면 배열에 x를 힙 푸시한다.
        # 최대 힙을 구하기 때문에 - 해주어 힙 푸시한다.
        heapq.heappush(heap, -num)
