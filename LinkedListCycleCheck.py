class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def isCycle(head):
    t1 = head
    t2 = head

    while t2 != None and t2.next != None:

        t1 = t1.next
        t2 = t2.next.next
        
        if t1 == t2:
            return True

    return False


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a


print isCycle(a)

a.next = None

print isCycle(a)



