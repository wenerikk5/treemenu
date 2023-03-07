class Node:
    all_nodes = []

    def __init__(self, id, name, parent, level=1, left=0, right=0):
        self.id = id
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
        self.level = level
        self.__class__.all_nodes.append(self)

    def get_childs(self, arr):
        childs = []
        for node in arr:
            if node.level > self.level and node.left > self.left and \
            node.right < self.right:
                childs.append(node)
        return childs
    
    def __str__(self):
        return self.name


def print_nodes():
    for node in Node.all_nodes:
        print(f'id: {node.id}| name: {node.name}| parent: {node.parent}| ' \
              f'level: {node.level}| left: {node.left}| right: {node.right}')
        

def get_parent(child):
    for node in Node.all_nodes:
        if node.id == child.parent:
            return node

def get_children(parent):
    result = []
    for node in parent.__class__.all_nodes:
        if node.parent == parent.id:
            result.append(node)
    return result

def rebuild_tree(parent, left, lvl):
    right = left + 1

    result = get_children(parent)

    for child in result:
        right = rebuild_tree(child, right, lvl + 1)
    
    parent.left = left
    parent.right = right
    parent.level = lvl

    return right + 1


def get_childs(target, arr):
    childs = []
    for node in arr:
        if node.level > target.level and node.left > target.left and \
        node.right < target.right:
            childs.append(node)
    return childs

def clean_duplicats(arr, elements):
    for elem in elements:
        if elem in arr:
            arr.remove(elem)
    return arr

def build_tree(arr):
    if len(arr) == 0:
        return ''
    else:
        html = '<ul>'
        for el in arr:
            childs = el.get_childs(arr)
            arr = clean_duplicats(arr, childs)
            
            html += '<li>' + '<span id="cat_' + str(el.id) + '">' + el.name + '</span>'
            html += build_tree(childs)
            html += '</li>'
        return html + '</ul>'


def main():
    """
    n1  - n2 - n4
        - n3 - n5 - n7
             - n6
    """
    n1 = Node(1, 'n1', 0)
    n2 = Node(2, 'n2', 1)
    n3 = Node(3, 'n3', 1)
    n4 = Node(4, 'n4', 2)
    n5 = Node(5, 'n5', 3)
    n6 = Node(6, 'n6', 3)
    n7 = Node(7, 'n7', 5)

    rebuild_tree(n1, 1, 0)
    print_nodes()

    all_nodes = Node.all_nodes

    print(build_tree(all_nodes))

main()
