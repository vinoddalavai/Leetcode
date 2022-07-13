from typing import Optional

import list_node
from list_node import ListNode


class MergeTwoSortedLists:
    #   Time Complexity: O(m+n), m = length of list1; n = length of list2
    #   Space Complexity: O(1)
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        dummy = result
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        return result.next


l1, l2 = list_node.create_list_node([1, 2, 4, 8]), list_node.create_list_node([1, 3, 4, 5, 6])
print("List 1: \n\t" + str(l1))
print("\nList 2: \n\t" + str(l2))
print("\nMerged linked list: \n\t" + str(MergeTwoSortedLists().merge_two_lists(l1, l2)))
