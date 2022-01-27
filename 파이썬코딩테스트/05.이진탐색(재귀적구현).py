# 이진탐색 소스코드 구현( 재귀 함수 )
def binary_search(array, target, start, end):
    # 탐색하고하는 범위에 데이터가 존재하지않는다
    if start > end:
        return None
    # 중간점을 명시
    mid = (start + end) // 2
    # 찾고자하는 값을 찾은 경우 중감점 인덱스 반환
    if array[mid] == target:
        # 찾고자 했던 값
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        #                                        끝점을 mid-1로 옮긴다
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        #                                 시작점을 mid+1로 옮긴다
        return binary_search(array, target, mid + 1, end)

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



