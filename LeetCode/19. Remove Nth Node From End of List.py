# Problem : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Date : 2021-06-02


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        list_len = self.length(head)
        node = head
        if list_len == 1:
            return None
        elif list_len == n:
            head = head.next
            return head
        for _ in range(list_len - n - 1):
            node = node.next
        node.next = node.next.next
        return head

    def length(self, head: ListNode) -> int:
        leng = 1
        node = head
        while node.next is not None:
            node = node.next
            leng += 1
        return leng
