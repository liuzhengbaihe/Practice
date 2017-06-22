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


def reverse(link):
    pre = link
    cur = pre.next
    pre.next = None

    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre 

if __name__ == "__main__":
    node1 = Node(1, Node(2))
    node2 = Node(3)
    check_cross_point(node1, node2)

    node = Node(4) 
    node1 = Node(1, node)
    node2 = Node(2, Node(3, node))
    check_cross_point(node1, node2)

    link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
    link1 = reverse(link)
    while link1:
        print link1.value
        link1 = link1.next
