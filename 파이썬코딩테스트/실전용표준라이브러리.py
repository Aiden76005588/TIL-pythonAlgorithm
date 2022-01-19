## 실전에서 유용한 표준 라이브러리

## 내장함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공합니다.
## 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함하고 있다.

sum_result = sum([1, 2, 3, 4, 5])
print(sum_result)

min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)

print(min_result, max_result)

eval_result = eval("(3+5)*7")
print(eval_result)

sorted_result = sorted([9, 1, 8, 5, 4])
sorted_reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(sorted_result)
print(sorted_reverse_result)

array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

## itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공합니다.
## 특히 순열과 조합 라이브러리는 코딩테스트에서 자주 사용된다.
# 순열 : 서로다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것 nPr
# 조합 : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것 nCr

data = ['A', 'B', 'C']
from itertools import permutations  # 순열

permutations_result = list(permutations(data, 3))
print(permutations_result)

from itertools import combinations  # 조합

combinations_result = list(combinations(data, 2))
print(combinations_result)

from itertools import product  # 중복순열

product_result = list(product(data, repeat=2))
print(combinations_result)

from itertools import combinations_with_replacement  # 중복조합

combinations_with_replacement_result = list(combinations_with_replacement(data, 2))
print(combinations_with_replacement_result)

# collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공
# 리스트와 같은 반복 가능한(iterablae) 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지를 알려줍니다.

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'blue', 'red', 'blue', 'green'])
print(counter['blue'])  # 등장횟수
print(counter['green'])
print(dict(counter))  # 사전 자료형으로 반환

## heapq: 힙(heap) 자료구조를 제공한다.
## 일반적으로 우선순위 큐 기능을 구현하기 위해 사용된다.

## bisect: 이진탐색(Binary Search) 기능을 제공한다.

## collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함한다.

## math : 필수적인 수학적 기능을 제공한다.
## 팩토리얼, 제곰근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함한다.
## GCD (Greatest Common Divisor) 최대공약수

import math


# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)


a = 21
b = 14

print(math.gcd(21, 14))
print(lcm(21, 14))
