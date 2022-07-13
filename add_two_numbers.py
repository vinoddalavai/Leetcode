from typing import Optional
from list_node import ListNode


class AddTwoNumbers:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre_result = ListNode()
        result = pre_result
        carry = 0
        while l1 or l2:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            carry, cur_sum = divmod(a + b + carry, 10)
            pre_result.next = ListNode(cur_sum)
            pre_result = pre_result.next
        if carry > 0:
            pre_result.next = ListNode(carry)
        return result.next
