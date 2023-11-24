from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]):
    print(l1.val)
    print(l2.val)
    answer = ListNode()
    begin = 0
    carry = 0
    flag1 = 0
    flag2 = 0
    begin = ListNode()
    xt = ListNode()
    begin.next = xt
    while l1.next is not None or l2.next is not None:
        val = 0
        if flag1 != 1:
            val += l1.val
        if flag2 != 1:
            val += l2.val
        if l2.next is None:
            flag2 = 1
        if l1.next is None:
            flag1 = 1
        if carry > 0:
            val += carry
            carry = 0
        if val > 9:
            carry += 1
            val -= 10
        if l2.next is None:
            l2 = l2.next
        if l1.next is None:
            l1 = l1.next
        if begin == 0:
            begin += 1
            begin.val = val
        elif begin == 1:
            xt.val = val
        else:
            temp = ListNode()
            temp.val = val
            xt.next = temp
            xt = temp

    return begin




l3 = addTwoNumbers(k1, k2)
while l3.next is not None:
    print(l3.val)
    l3 = l3.next
