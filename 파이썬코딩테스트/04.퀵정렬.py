"""
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법입니다.
일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나입니다.
병합정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘입니다.
가장 기본적인 퀵 정렬은 첫번째 데이터를 기준 데이터(Pivot)로 설정합니다.
"""

[5, 6, 9, 0, 3, 1, 6, 2, 4, 8]
"""
[step0] 현재 피벗의 값은 '5'입니다. 왼쪽에서부터 '5'보다 큰 데이터를 선택하므로 '7'이 선택되고, 오른쪽에서부터 '5'보다 작은 데이터를 선택하므로 '4'가 
선택됩니다. 이제 이 두 데이터의 위치를 서로 변경합니다.
"""

[5, 4, 9, 0, 3, 1, 6, 2, 7, 8]
"""
[step1] 현재 피벗의 값은 '5'입니다. 왼쪽에서부터 '5'보다 큰 데이터를 선택하므로 '9'가 선택되고, 오른쪽에서부터 '5'보다 작은 데이터를 선택하므로 '2'가
선택됩니다. 이제 이 두 데이터의 위치를 서로 변경합니다.
"""

[5, 4, 2, 0, 3, 1, 6, 9, 7, 8]
"""
[step2] 현재 피벗의 값은 '5'입니다. 왼쪽에서부터 '5'보다 큰 데이터를 선택하므로 '6'가 선택되고, 오른쪽에서부터 '5'보다 작은 데이터를 선택하므로 '1'가
선택됩니다. 이제 이 두 데이터의 위치를 서로 변경합니다. ** 단, 이처럼 위치가 엇갈리는 경우 '피벗'과 '작은 데이터'의 위치를 서로 변경합니다.
"""

[1, 4, 2, 0, 3, 5, 6, 9, 7, 8]
"""
[분할완료] 이제 '5'의 왼쪽에 있는 데이터는 모두 5보다 작고, 오른쪽에 있는 데이터는 모두 '5'보다 크다는 특징이 있습니다. 이렇게 피벗을 기준으로
데이터 묶음을 나누는 작업을 분할(Divide)이라고 합니다.
"""
[1, 4, 2, 0, 3], [5, 6, 9, 7, 8]

"""
퀵정렬이 빠른 이유
이상적인 경우 분할이 절반씩 일어난다면 전체 연산횟수로 O( N * log N)를 기대할 수 있습니다.
넓이가 N 높이가 log N

시간복잡도
평균 :O( N * log N)
최악 :O( N^2 )
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
