from collections import defaultdict


def solution(id_list, report, k):
    # 신고자 신고한아이디 신고당한 횟수
    # 게시판 이용정지를 시키면서 정지메일을 발송
    # 한명의 신고자가 신고한건 한번으로 처리
    # k 번 신고당하면 정지

    answer = [0] * len(id_list)

    # 주어진 report 리스트 중복제거.
    report = set(report)

    # defaultdict 는 value의 타입만 지정해준다면 key에 매핑되는 값을 따로 지정해주지않아도
    # 자동으로 기본값이 들어간다.
    # 유저별로 신고한 아이디정보를 담고있는 dict
    # 유저별로 신고당한 횟수 정보를 담고 있는 dict
    user_list_who = defaultdict(set)  # 신고를 한 유저 A: 유저 A가 신고한 유저목록(set)
    num_of_reported = defaultdict(int)  # 신고를 당한 유저 A: 유저 A가 신고당한 횟수(int)


    suspended = []

    # x, y= report
    for r in report:
        # 신고하는 사람 , 신고받는 사람.
        do_report, be_reported = r.split()

        num_of_reported[be_reported] += 1
        print(num_of_reported[be_reported])
        user_list_who[do_report].add(be_reported)

        if num_of_reported[be_reported] == k:
            suspended.append(be_reported)

    for s in suspended:
        for i in range(len(id_list)):
            if s in user_list_who[id_list[i]]:
                answer[i] += 1
    return answer