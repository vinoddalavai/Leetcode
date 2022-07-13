from typing import Optional

import list_node
from list_node import ListNode


class ReorderList:
    #   Time Complexity: O(n)
    #   Space Complexity: O(1)
    def reorder_list(self, head: Optional[ListNode]) -> None:
        #   find the mid of list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Mid point : " + str(slow))
        #   reverse the second half of list
        previous, current = None, slow
        while current:
            temp, current.next = current.next, previous
            previous, current = current, temp
        print("Reversed 2nd half: " + str(previous))
        print("1st half: " + str(head))
        #   merge the first half and the reversed second half
        first, second = head, previous
        result = first
        while second.next:
            f_temp = first.next
            first.next = second
            first = f_temp
            s_temp = second.next
            second.next = first
            second = s_temp
        print("Merged: " + str(result))


test_list = list_node.create_list_node([1, 2, 3, 4, 5])
ReorderList().reorder_list(test_list)
