def mergeTwoLists(self, l1, l2):
    # 연산순서 우선순위 >, and, or or보다 and의 우선순위가 높다.
    # l1이 아니거나 또는 l1보다 값이 작은 l2이면
    if (not l1) or (l2 and l1.val > l2.val):
        # 변수를 스왑 l2를 l1에 넣고 l1을 l2에 넣고
        l1, l2 = l2, l1
        #l1이 l2보다 작은 값이면 l1.next로 추가한다
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1
