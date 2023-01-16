class Node:
    """
    Node class representing the node of a Doubly Linked List
    """

    def __init__(self, key: int, val: int):
        """ Constructor for the Node
        Accepts key and value as input and creates the Node object for the doubly linked list
        :param key: Integer for key of the node
        :param val: Integer for value of the node
        """

        self.key, self.val = key, val
        # pointers to the previous and next node for the current node. Defaulted to None
        self.prev = self.nxt = None


class LRUCache:
    """
    For designing LRU Cache we will make use of a Doubly Linked List and HashMap. The left most node represents the least
    used value and the right most node represents the most used value. In order to get the values in constant time, we
    will make use of a HashMap.
    Every time we add a node to the cache, we will add it to the right and update the hashmap. If the hashmap contains the
    max capacity of nodes then we will remove the node from the left.
    Every time we get a node from the cache, we will remove it from the linked list and add it to the right of the list.
    This is because we have recently accessed that node, so it becomes the most used node. This operation will also be in
    constant time as we are not traversing through the linked list because we use the doubly linked list's left and right
    nodes for get and put.
    """

    def __init__(self, capacity: int) -> None:
        """ Constructor for the LRU Cache
        Accepts the capacity of the cache and sets other fields.
        :param capacity: Integer representing the number of values that the cache can hold.
        """

        # declare and initialize cache (hashmap) and capacity of the LRU Cache
        self.cache, self.cap = {}, capacity
        # declare and initialize left and right nodes to represent the least and most used values in the list
        self.left, self.right = Node(0, 0), Node(0, 0)
        # point the left and right nodes to each other
        self.left.nxt, self.right.prev = self.right, self.left

    def _remove(self, node: Node) -> None:
        """ Remove a node from the linked list
        Accept a node and remove it from the linked list
        :param node: Node to be removed from the linked list
        :return: None
        """

        prev_node, nxt_node = node.prev, node.nxt
        prev_node.nxt, nxt_node.prev = nxt_node, prev_node

    def _insert(self, node: Node) -> None:
        """ Insert a node to the linked list
        Accept a node and add it to the right of linked list
        :param node: Node to be added to the linked list
        :return: None
        """

        prev_node, nxt_node = self.right.prev, self.right
        prev_node.nxt = nxt_node.prev = node
        node.prev, node.nxt = prev_node, nxt_node

    def get(self, key: int) -> int:
        """ Get the value associated with the key
        Accept a key and fetch the value of that key from the hashmap
        :param key: Integer for which value needs to be fetched
        :return: Integer representing the value associated with the input key
        """

        # check if key is in the hashmap
        if key in self.cache:
            # remove the corresponding node from the linked list
            self._remove(self.cache[key])
            # insert the corresponding node to the right of the linked list
            self._insert(self.cache[key])
            # return the value of that node
            return self.cache[key].val
        # if key is not present in the hashmap then return -1
        return -1

    def put(self, key: int, value: int) -> None:
        """ Add a node to the linked list
        Accept key and value (integers), create a node and add it to the linked list
        :param key: Integer value which is the key of the node
        :param value: Integer value which is the value of the node
        :return: None
        """

        # if key is present in hashmap
        if key in self.cache:
            # remove the corresponding node from the linked list
            self._remove(self.cache[key])
        # create a node with the key and value and add it to the hashmap
        self.cache[key] = Node(key, value)
        # insert it in the linked list to the right
        self._insert(self.cache[key])

        # check if the length of the hashmap is greater than the capacity
        if len(self.cache) > self.cap:
            # fetch the node that left node points to
            lru = self.left.nxt
            # remove that node from the linked list
            self._remove(lru)
            # remove it from the hashmap
            del self.cache[lru.key]


if __name__ == '__main__':
    input_capacity = int(input("Enter the capacity of the LRU Cache: "))
    lru_obj = LRUCache(input_capacity)
    print(lru_obj.put(1, 1))
    print(lru_obj.put(2, 2))
    print(lru_obj.get(1))
    print(lru_obj.put(3, 3))
    print(lru_obj.get(2))
    print(lru_obj.put(4, 4))
    print(lru_obj.get(1))
    print(lru_obj.get(3))
    print(lru_obj.get(4))
