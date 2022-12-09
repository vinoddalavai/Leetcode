"""
Approach: Linked List
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self:
            return None
        return f"{self.val} -> {self.next}"

class ReorderList:
    def _reorder_list(self, head: Optional[ListNode]) -> None:
        """ Reorder the linked list
        Accept the head node of a linked list and reorder it
        :param head: ListNode which is the first node of the linked list input
        :return: None
        """

        # find middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of the linked list iteratively
        second = slow.next
        previous = slow.next = None
        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp

        # merge two lists
        list1, list2 = head, previous
        while list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2

    def process(self, input_head: Optional[ListNode]) -> None:
        self._reorder_list(input_head)
        print(f"\nOutput:\n\t {input_head}\n")


if __name__ == '__main__':
    count = int(input("Enter the number of nodes in the linked list: "))
    input_node = ListNode()
    copy_input = input_node
    for index in range(count):
        input_node.val = int(input(f"Enter value for Node {index}: "))
        input_node.next = ListNode() if index < (count - 1) else None
        input_node = input_node.next
    ReorderList().process(copy_input)
