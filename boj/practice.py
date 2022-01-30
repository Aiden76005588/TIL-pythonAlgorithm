import heapq
import sys

number = int(input())
heap = []

for _ in range(number):
    """
    sys.stdin.readline()
    대량의 데이터를 반복적으로 입력받아야 할 때, input()대신 sys.stdin.readline()을 이용하면 
    성능(속도)이 향상됩니다. 

    """
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
