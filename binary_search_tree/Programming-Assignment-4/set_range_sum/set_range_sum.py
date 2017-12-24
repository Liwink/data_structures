# python3

from sys import stdin

# Splay tree implementation


# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
        v.right.parent = v


def smallRotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)


# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    global root
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            smallRotation(v)
            break
        bigRotation(v)
    root = v
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    # Don’t forget to splay the node which was accessed last during the find operation.
    v = root
    last = root
    next = None
    while v is not None:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)


def split(root, key):
    (result, root) = find(root, key)
    if result is None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def erase(x):
    global root
    # Implement erase yourself
    r, root = find(root, x + 1)
    splay(r)
    v, root = find(root, x)
    splay(v)
    if v is None or v.key != x:
        return
    if r is None:
        l = v.left
        if l is None:
            root = None
            return
        l.parent = None
        root = l
        return
    r.left = v.left
    r.parent = None
    update(r)
    root = r


def search(x):
    global root
    v, root = find(root, x)
    if v is not None and v.key == x:
        return True
    return False


def sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
    # Complete the implementation of sum
    ans = middle.sum if middle else 0
    # if to == 10:
    #     import pdb; pdb.set_trace()
    root = merge(merge(left, middle), right)

    return ans


def print_tree():
    global root
    if root is None:
        return
    print('\n')
    print('***tree***')
    print(root.key)
    r = root
    line = '{0} {1}'.format(r.left.key if r.left else '\t', r.right.key if r.right else '\t')
    print(line)
    r = root.left
    if r is None:
        l1 = '\t \t'
    else:
        l1 = '{0} {1}'.format(r.left.key if r.left else '\t', r.right.key if r.right else '\t')
    r = root.right
    if r is None:
        l2 = '\t \t'
    else:
        l2 = '{0} {1}'.format(r.left.key if r.left else '\t', r.right.key if r.right else '\t')
    print(l1 + ' ' + l2)
    print('******')
    print('\n')


MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        # if (x + last_sum_result) % MODULO == 31190791:
        #     import pdb; pdb.set_trace()
        # print('add:', (x + last_sum_result) % MODULO)
        insert((x + last_sum_result) % MODULO)
        # print_tree()
    elif line[0] == '-':
        x = int(line[1])
        # print('delete:', (x + last_sum_result) % MODULO)
        erase((x + last_sum_result) % MODULO)
        # print_tree()
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
