'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = res = ListNode()
        carres = 0
        while l1 or l2 or carres:
            if l1:
                carres += l1.data
                l1 = l1.next
            if l2:
                carres += l2.data
                l2 = l2.next
            carres, value = carres // 10, carres % 10
            cur.next = ListNode(value)
            cur = cur.next
        return res.next

# Check Custom Input

s = Solution()

l1_node1 = ListNode(3)
l1_node2 = ListNode(4)
l1_node3 = ListNode(3)

l1_node1.next = l1_node2
l1_node2.next = l1_node3

l2_node1 = ListNode(7)
l2_node2 = ListNode(6)
l2_node3 = ListNode(4)

l2_node1.next = l2_node2
l2_node2.next = l2_node3

answer = s.addTwoNumbers(l1_node1, l2_node1)

while answer:
    print(answer.data)
    answer = answer.next