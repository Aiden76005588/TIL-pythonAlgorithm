from collections import defaultdict
def solution(id_list, report, k):
    # 신고자 신고한아이디 신고당한 횟수
    # 게시판 이용정지를 시키면서 정지메일을 발송
    # 한명의 신고자가 신고한건 한번으로 처리
    # k 번 신고당하면 정지

    answer = [0]*len(id_list) # 각 유저가 받은 결과메일의 수를 담기 위해 id_list의 길이만큼 초기화

    # 주어진 report 리스트 중복제거.
    report = set(report)

    # defaultdict 는 value의 타입만 지정해준다면 key에 매핑되는 값을 따로 지정해주지않아도
    # 자동으로 기본값이 들어간다.
    # 유저별로 신고한 아이디정보를 담고있는 dict
    # 유저별로 신고당한 횟수 정보를 담고 있는 dict
    reporter_list = defaultdict(set) #신고를 한 유저 A: 유저 A가 신고한 유저목록(set)
    count_report = defaultdict(int) # 신고를 당한 유저 A: 유저 A가 신고당한 횟수(int)

    # 정지된 유저
    suspended_user = []

    # x, y= report
    for r in report:
        # 신고하는 사람 , 신고받는 사람.
        reporter, reported_user = r.split()

        # 신고당한 유저 +1
        count_report[reported_user] += 1
        reporter_list[reporter].add(reported_user)
        # print(reporter_list)
        # 신고당한 횟수가 k에 도달하게 된다면 정지 suspended_user에 저장한다.

        if count_report[reported_user] == k:
            suspended_user.append(reported_user)

    # reporter_list 와 id_list를 이용하여 suspended에 속한 유저들이
    # reporter_list[id_list[i]]에 포함되어 있다면 answer에서
    # 해당되는 자리(반복문 &인덱스 접근이므로 순서가 맞는다.)의 수를 1 증가시킨다.
    for s in suspended_user:
        for i in range(len(id_list)):
            if s in reporter_list[id_list[i]]:
                answer[i] += 1

    return answer

# 프로그래머스 답안
# from collections import defaultdict
#
#
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports = {x: 0 for x in id_list}
#     print(reports)
#     print(answer)
#
#     for r in set(report):
#         reports[r.split()[1]] += 1
#         print(reports)
#
#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1
#
#     return answer