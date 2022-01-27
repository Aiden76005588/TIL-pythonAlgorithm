# 이진탐색 소스코드 구현( 반복문 구현 )
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2  # 몫
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# n(원소의 개수)과 target( 찾고자 하는 값) 을 입력 받기
n, target = list(map(int, input().split()))

# 전체 원소 입력 받기
array = list(map(int, input().spilt()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    # 전부 돌았지만 없었다
    print('원소가 존재하지 않습니다.')
else:
    # 해당 인덱스 값을 찾았으면 +1을 더해줘서 몇번째 숫자인지 나타낸다.
    print(result + 1)
