from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self:
            return None
        return str(self.val) + " -> " + str(self.next)


def create_list_node(nodes: List[int]) -> ListNode:
    list_node = ListNode()
    result = list_node
    for node in nodes:
        list_node.next = ListNode(node)
        list_node = list_node.next
    return result.next


if __name__ == "__main__":
    test_list = ListNode(1, ListNode(2, ListNode(3)))
    print(test_list)