class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def are_the_same(head1: Node, head2: Node) -> bool:
    i = j = 0
    p1, p2 = head1, head2
    while p1 and p2:
        val1, val2 = p1.val, p2.val
        while i < len(val1) and j < len(val2):
            if val1[i] != val2[j]:
                return False
            i += 1
            j += 1

        if i == len(val1):
            i = 0
            p1 = p1.next
        if j == len(val2):
            j = 0
            p2 = p2.next
    
    return not p1 and not p2

def build_linked_list(values):
    """Helper to build linked list from list of strings"""
    head = None
    prev = None
    for val in values:
        node = Node(val)
        if not head:
            head = node
        else:
            prev.next = node
        prev = node
    return head


def test_are_the_same():
    # Test 1: Exact match, single node
    head1 = build_linked_list(["abc"])
    head2 = build_linked_list(["abc"])
    assert are_the_same(head1, head2) == True

    # Test 2: Exact match, split across nodes
    head1 = build_linked_list(["ab", "c"])
    head2 = build_linked_list(["a", "bc"])
    assert are_the_same(head1, head2) == True

    # Test 3: Different content
    head1 = build_linked_list(["ab", "x"])
    head2 = build_linked_list(["a", "bc"])
    assert are_the_same(head1, head2) == False

    # Test 4: One longer than the other
    head1 = build_linked_list(["abc", "d"])
    head2 = build_linked_list(["abcd", "e"])
    assert are_the_same(head1, head2) == False

    # Test 5: Both empty lists
    head1 = None
    head2 = None
    assert are_the_same(head1, head2) == True

    print("✅ All tests passed!")


if __name__ == "__main__":
    test_are_the_same()