import sys
from collections import deque

# input_number = int(sys.stdin.readline())
input_number = [1,2,3,4,5,6]

input_array = deque()
for i in range(input_number):
    input_array.append(i + 1)

while len(input_array) > 1:
    input_array.popleft()
    temp = input_array.popleft()
    input_array.append(temp)

print(input_array.pop())