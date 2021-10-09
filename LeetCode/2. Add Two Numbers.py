# Problem : https://leetcode.com/problems/add-two-numbers/
# Date : 2021-04-23


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = str(l1.val), str(l2.val)
        while l1.next != None:
            l1 = l1.next
            n1 += str(l1.val)
        while l2.next != None:
            l2 = l2.next
            n2 += str(l2.val)
        n3 = str(int(n1[::-1]) + int(n2[::-1]))
        answer = ListNode(val = int(n3[0]))
        for char in n3[1:]:
            answer = ListNode(val=int(char), next=answer)
        return answer
