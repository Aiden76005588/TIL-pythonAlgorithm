from functools import cmp_to_key

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]


def solution(files):
    filenames = []
    # foo뒤의 넘버 0 무시. 어떻게 무시하지? 제거?
    # 대소문자 구분하지않는다.

    for file in files:
        filenames.append(split_filename(file))
    filenames.sort(key=cmp_to_key(compare))

    for i, filename in enumerate(filenames):
        filenames[i] = join_filename(filename)

    return filenames


def join_filename(filename: list) -> str:
    return ''.join(filename)


def split_filename(filename: str) -> list:  # 파일이름을 [HEAD, NUMBER, TAIL]로 변환
    i = 0
    while not filename[i].isnumeric():  # isnumeric() 문자가 숫자에 해당이 되는지 판단
        i += 1  # i가 숫자가 아닐때 즉 문자일때 i를 더해준다.
        HEAD = filename[:i]

    j = i

    while filename[j].isnumeric():
        j += 1
        if j == len(filename):
            return [HEAD, NUMBER, '']
        NUMBER = filename[i:j]

    TAIL = filename[j:]

    return [HEAD, NUMBER, TAIL]


def compare(s1, s2) -> int:
    head1, number1, tail1 = s1[0], s1[1], s1[2]
    head2, number2, tail2 = s2[0], s2[1], s2[2]

    head1, head2 = head1.upper(), head2.upper()
    number1, number2 = int(number1), int(number2)

    # if head1 < head2:
    #     return -1
    # elif head1 > head2:
    #     return 1
    # else:
    #     return 1
    #
    # if number1 > number2:
    #     return -1
    # elif number1 < number2:
    #     return 1
    # else:
    #     return 1
    if head1 != head2:
        return -1 if head1 < head2 else 1
    else:
        return number1 - number2 if number1 != number2 else -1


for file in files:
    print(split_filename(file))
answer = solution(files)
print(answer)
