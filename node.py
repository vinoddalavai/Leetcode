from typing import List


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        if not self:
            return None
        return str(self.val) + " -> " + str(self.next)


def create_list_node(nodes: List[int]) -> Node:
    list_node = Node()
    result = list_node
    for node in nodes:
        list_node.next = Node(node)
        list_node = list_node.next
    return result.next


if __name__ == "__main__":
    test_list = Node(1, Node(2, Node(3)))
    print(test_list)
