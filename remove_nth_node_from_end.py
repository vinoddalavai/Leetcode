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

class RemoveNthNodeFromEnd:
    def _remove_nth_node_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ Return the linked list after removing nth node from the end
        Removes the nth node from the end of the input linked list
        :param head: ListNode representing the head of the linked list
        :param n: node to be removed from the end of the list
        :return: ListNode after removing the nth node from the end of the list
        """

        # find out the length of the linked list. Initialize the length to 0
        length = 0
        # assign a temp node to point to the head of the linked list. This is done in order to keep one pointer at
        # the head because after calculating the length, the pointer will point to the last node
        temp = head
        # traverse through the linked list
        while temp:
            # increment length by one
            length += 1
            # move to the next node
            temp = temp.next
        # index value of node to be removed starting at the head of the list
        # example: 2nd from the end is 3rd from the start of the linked list having 5 nodes
        r_index = length - n
        # create a result node that is an empty node pointing to the head of the input linked list
        result = ListNode(0, head)
        # assign a temp node called previous to point at result and current to point to head
        # this is done so that we can have one pointer to point at the result node
        previous, current = result, head
        # traverse through the linked list decrementing r_index
        while current:
            # if r_index is zero, it means that we have reached the node to be removed
            if r_index == 0:
                # change pointers
                previous.next = current.next
                # point the node to be removed to None
                current.next = None
                # break out of the loop because we have removed the node
                break
            # if r_index is not zero then keep traversing previous and current
            previous = current
            current = current.next
            # reduce r_index by 1
            r_index -= 1
        # return head of the input linked list
        return result.next

    def process(self, input_head: Optional[ListNode], input_n: int) -> None:
        print(f"\nOutput:\n\t{self._remove_nth_node_from_end(input_head, input_n)}\n")


if __name__ == '__main__':
    count = int(input("Enter the number of nodes in the linked list: "))
    input_node = ListNode()
    copy_input = input_node
    for index in range(count):
        input_node.val = int(input(f"Enter value for Node {index}: "))
        input_node.next = ListNode() if index < (count - 1) else None
        input_node = input_node.next
    ntr = int(input("Enter the node to be removed from the end of the list: "))
    RemoveNthNodeFromEnd().process(copy_input, ntr)
