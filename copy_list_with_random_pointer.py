"""
Approach: Linked List
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        if not self:
            return None
        rand = None if self.random is None else self.random.val
        return f"{self.val}(Random -> {rand}) -> {self.next}"

class CopyListWithRandomPointer:
    def _copy_random_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Return new linked list that is a copy of the original
        Accept a linked list, create an exact replica of it with both next and random pointers and return the replica
        :param head: ListNode of the head of the linked list
        :return: ListNode that is an exact replica of the input linked list
        """

        # declare and initialize a hashmap with a default None mapping
        old_to_new_map = {None: None}
        # create a temp node that will be used to create replica nodes
        temp = head
        # traverse through the input linked list
        while temp:
            # create replica nodes of the input nodes
            old_to_new_map[temp] = ListNode(temp.val)
            temp = temp.next
        # create a temp node that will be used to link the next and random pointers to the newly created replicas
        temp = head
        # traverse through the input linked list
        while temp:
            # link replica next pointer
            old_to_new_map[temp].next = old_to_new_map[temp.next]
            # link replica random pointer
            old_to_new_map[temp].random = old_to_new_map[temp.random]
            temp = temp.next
        # return the head of th linked list of the replicated nodes
        return old_to_new_map[head]

    def process(self, input_head: Optional[ListNode]) -> None:
        print(f"\nOutput:\n\t{self._copy_random_list(input_head)}\n")


if __name__ == '__main__':
    count = int(input("Enter the number of nodes in the linked list: "))
    input_map = {"None": None}
    for index in range(count):
        if index == 0:
            value = int(input(f"Enter the value of Head: "))
        else:
            value = int(input(f"Enter the value of Node {index}: "))
        input_map[index] = ListNode(value)
    for index in range(count):
        if index == 0:
            print("For Head")
        else:
            print(f"For Node {index}: ")
        nxt = input(f"\tEnter the next pointer: ")
        rand = input(f"\tEnter the random pointer: ")
        if rand == "Head":
            rand = 0
        elif rand != "None":
            rand = int(rand)

        if nxt == "Head":
            nxt = 0
        elif nxt != "None":
            nxt = int(nxt)
        input_map[index].next = input_map[nxt]
        input_map[index].random = input_map[rand]
    print(f"You have created the following linked list: {input_map[0]}")
    CopyListWithRandomPointer().process(input_map[0])
