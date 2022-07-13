from typing import Optional

import list_node
from list_node import ListNode


class RemoveNthNodeFromEnd:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0
        curr = head
        while curr:
            list_length += 1
            curr = curr.next

        result = ListNode(0, head)
        node_to_remove = list_length - n
        previous, current = result, head
        while current:
            if node_to_remove == 0:
                previous.next = current.next
                current.next = None
            previous, current = current, current.next
            node_to_remove -= 1
        return result.next


head1, node1 = list_node.create_list_node([1, 2, 3, 4, 5]), 2
head2, node2 = list_node.create_list_node([1]), 1
print(RemoveNthNodeFromEnd().remove_nth_from_end(head1, node1))
print(RemoveNthNodeFromEnd().remove_nth_from_end(head2, node2))
