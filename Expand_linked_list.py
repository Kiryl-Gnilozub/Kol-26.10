import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    if head is None:
        return None

    if head.next is None:
        return head

    rest_reversed = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return rest_reversed


class LinkedListTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(reverse_linked_list(None))

    def test_single_node_list(self):
        node = Node(1)
        self.assertEqual(reverse_linked_list(node), node)

    def test_multiple_nodes_list(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.next = node2
        node2.next = node3

        reversed_head = reverse_linked_list(node1)
        self.assertEqual(reversed_head.data, 3)
        self.assertEqual(reversed_head.next.data, 2)
        self.assertEqual(reversed_head.next.next.data, 1)
        self.assertIsNone(reversed_head.next.next.next)


if __name__ == "__main__":
    unittest.main()
