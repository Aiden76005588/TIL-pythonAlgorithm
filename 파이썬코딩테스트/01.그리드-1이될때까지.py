# N, K를 공백을 기준으로 구분하여 입력받기
# n, k = map(int, input().split()) # 입력받은 문자열을 공백기준으로 나눈다
"""
n, k에 공백을 기준으로 수가 들어간다.
split()으로 공백기준으로 나눈다.
map함수를 이용해서 각가 int형 즉 정수로 바꾼뒤에 n, k에 넣는다.
"""
n = 999
k = 2

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    print("target----", target)
    """
    n을 k로 나눈 값에 다시 k를 곱해준다.
    그러면 n은 k로 나누어 떨어질 수 있는 가장 큰 값이 된다.
    """
    print("n------",n)
    result += (n - target)
    print("result----", result)

    """
    result는 우리가 연산하는 총 횟수라고 할 수 있다.
    1을 빼는 연산을 몇 번 수행할지 한번에 계산해서 넣어준다.
    """
    n = target
    print("n----", n)
    # N이 K보다 작을 때( 더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # K로 나누기
    result += 1
    print("result2------", result)
    """
    n_k = n // k
    n = n_k
    """
    n //= k


# 마지막으로 남은 수에 대하여 1씩 빼기
# n이 1일때도 계간이 되므로 1을 빼준다.
result -= 1
print("결과-----", result)
