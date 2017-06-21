class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


def print_list(node):
    while node:
        print node
        node = node.next

def add_next(tail=None, el=None):
    if el < 10:
        node = Node(el)
        tail.next = node
        tail = node
        add_next(tail, el+1)

def check_cross_point(node1, node2):
    length1, length2 = 0, 0
    node = node1
    while node.next:
        length1 = length1 + 1
        node = node.next
    node = node2
    while node.next:
        length2 = length2 + 1
        node = node.next

    if length1 > length2:
        for x in xrange(length1 - length2):
            node1 = node1.next
    if length1 < length2:
        for x in xrange(length2 - length1):
            node2 = node2.next
    while (node1 and node2):
        if node1.next == node2.next:
            print "cross point is {0}".format(node1.next)
            break
        else:
            node1 = node1.next
            node2 = node2.next

if __name__ == "__main__":
    #node1 = Node(1)
    #add_next(node1, 2)
    #node2 = Node(5)
    #add_next(node2, 6)
    #print_list(node1)
    #print_list(node2)
    #check_cross_point(node1, node2)
    
    node4 = Node(4)
    node3 = Node(3)
    node2 = Node(2)
    node1 = Node(1)
    node1.next = node4
    node2.next = node3
    node3.next = node4
    check_cross_point(node1, node2)
