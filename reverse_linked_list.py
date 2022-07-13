from typing import Optional

import list_node
from list_node import ListNode


class ReverseLinkedList:
    def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        reverse = self.reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None
        return reverse

    def reverse_list_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            temp, current.next = current.next, previous
            previous, current = current, temp
        return previous


if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    nodes = list_node.create_list_node(values)
    print("Original linked list: \n\t" + str(nodes))
    print("\nReversed Linked List: ")
    reversed_ll = ReverseLinkedList().reverse_list_recursive(nodes)
    print("\tRecursive Solution: \n\t" + str(reversed_ll))
    values = [1, 2, 3, 4, 5]
    nodes = list_node.create_list_node(values)
    reversed_ll = ReverseLinkedList().reverse_list_iterative(nodes)
    print("\n\tIterative Solution: \n\t" + str(reversed_ll))
