# https://adventofcode.com/2022/day/7
debug = False
f = open("../debug_input.txt" if debug else "../input.txt", "r")
log = f.read().split('\n')[2:]


class Node:
    def __init__(self, parent, name, size=0, children=None):
        if children is None:
            children = list()
        self.parent = parent
        self.name = name
        self.children = children
        self.size = size

    def add_child(self, name, size=0):
        child = Node(self, name, size)
        self.children.append(child)
        self.increase_size(size)

    def increase_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.increase_size(size)


tree = Node(None, '/')
current_node = tree


for x in log:
    args = x.split()
    if args[0] == '$':
        if args[1] == 'cd':
            if args[2] == '..':
                current_node = current_node.parent
            else:
                for child in current_node.children:
                    if child.name == args[2]:
                        current_node = child
    else:
        if args[0] == 'dir':
            current_node.add_child(args[1])
        else:
            current_node.add_child(args[1], int(args[0]))


def get_sizes(_tree: Node, container):
    if len(_tree.children) > 0:
        container.append(_tree.size)
        for node in _tree.children:
            get_sizes(node, container)


container = []
get_sizes(tree, container)
container.sort(reverse=True)
to_free = 30000000 - (70000000 - tree.size)


for x in range(len(container)):
    if container[x] < to_free:
        print(container[x - 1])
        break
