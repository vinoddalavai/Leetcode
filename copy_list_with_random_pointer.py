from typing import Optional

from node import Node


class CopyListWithRandomPointer:
    def copy_random_list(self, head: Optional[Node]) -> Optional[Node]:
        hash_map = {None: None}
        copy = Node(0, head)
        result = copy
        while head:
            hash_map[head] = Node(head.val)
            head = head.next

        copy = copy.next
        while copy:
            hash_map[copy].next = hash_map[copy.next]
            hash_map[copy].random = hash_map[copy.random]
            copy = copy.next
        return hash_map[result.next]
