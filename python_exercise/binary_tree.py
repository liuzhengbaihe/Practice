class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def deep(root, deep_list):
    if not root:
        return
    deep(root.left, deep_list)
    deep(root.right, deep_list)
    deep_list.append(root.data)

def layer(root, layer_list):
    stack = [root]
    while stack:
        current = stack.pop(0)
        layer_list.append(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return layer_list

def visible_nodes(root, visible_node_list, max_value=None):
    if root == None:
        return 
    if max_value == None:
        max_value = root.data
    if max_value <= root.data:
        visible_node_list.append(root.data)
        visible_nodes(root.left, visible_node_list, root.data)
        visible_nodes(root.right, visible_node_list, root.data)
    else:
        visible_nodes(root.left, visible_node_list, max_value)
        visible_nodes(root.right, visible_node_list, max_value)

if __name__ == "__main__":
    tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    deep_list = []
    deep(tree, deep_list)
    print "list by deep method:", deep_list
    layer_list = []
    layer(tree, layer_list)
    print "list by layer method:", layer_list
    visible_node_list = []
    visible_nodes(tree, visible_node_list)
    print "visible node list:", visible_node_list
