class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def cll(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while fast and fast.next:
        if fast == slow or fast.next == head:
            return True
        slow =slow.next
        fast = fast.next.next
    return False

if __name__ == "__main__":
    # Circular linked list
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c
    c.next = a  # Circular
    print(cll(a))  # Should print True

    # Non-circular linked list
    x = Node(10)
    y = Node(20)
    z = Node(30)
    x.next = y
    y.next = z
    print(cll(x))  # Should print False

