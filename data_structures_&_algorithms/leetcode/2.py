from typing import Optional
from utils import ListNode, print_linked_list

#link: https://leetcode.com/problems/add-two-numbers/submissions/1934394181/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        # steps = 0
        
        head = None
        tail = None

        while l1 is not None or l2 is not None:
          # steps += 1
          a = l1.val if l1 is not None else 0
          b = l2.val if l2 is not None else 0
          c = (a + b) + carry

          sum = c % 10
          carry = c // 10
          # print(f"Steps: {steps}, l1: {a}, l2: {b}, sum: {sum}, carry: {carry}")

          if head is None:
            head = ListNode(sum)
            tail = head
          else:
            tail.next = ListNode(sum)
            tail = tail.next

          l1 = l1.next if l1 is not None else None
          l2 = l2.next if l2 is not None else None

        # print(f"carry: {carry} sum: {sum}")

        if carry > 0:
            tail.next = ListNode(carry)
            tail = tail.next

        return head

# Helper to build linked list from Python list
def build_linked_list(values):
    head = None
    current = None
    for val in values:
        node = ListNode(val)
        if not head:
            head = node
            current = node
        else:
            current.next = node
            current = node
    return head


# ===== Test Case 1 =====
l1 = build_linked_list([2, 4, 3, 9])
l2 = build_linked_list([5, 6, 4])
ans = Solution().addTwoNumbers(l1, l2)
print_linked_list(ans, "Solution")

# ===== Test Case 2 =====
l1 = build_linked_list([0])
l2 = build_linked_list([0])
ans = Solution().addTwoNumbers(l1, l2)
print_linked_list(ans, "Solution")


# ===== Test Case 3 =====
l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = build_linked_list([9, 9, 9, 9])
ans = Solution().addTwoNumbers(l1, l2)
print_linked_list(ans, "Solution")

# Intendede Solution

# class Solution:
#     def addTwoNumbers(
#         self,
#         l1: Optional[ListNode],
#         l2: Optional[ListNode]
#     ) -> Optional[ListNode]:

#         dummy = ListNode(0)
#         current = dummy
#         carry = 0

#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0

#             total = val1 + val2 + carry
#             carry = total // 10

#             current.next = ListNode(total % 10)
#             current = current.next

#             if l1: l1 = l1.next
#             if l2: l2 = l2.next

#         return dummy.next