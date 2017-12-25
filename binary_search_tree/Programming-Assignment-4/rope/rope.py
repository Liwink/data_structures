# python3
import sys


class Vertex:
    def __init__(self, key, size, left, right, parent):
        (self.key, self.size, self.left, self.right, self.parent) = (key, size, left, right, parent)


def update(v):
    if v is None:
        return
    v.size = 1 + (v.left.size if v.left else 0) + (v.right.size if v.right else 0)
    if v.left:
        v.left.parent = v
    if v.right:
        v.right.parent = v


def smallRotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = parent.parent
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
    if (v.parent.left == v and v.parent.parent.left == v.parent) or\
            (v.parent.right == v and v.parent.parent.right == v.parent):
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)


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


def find(v, index):
    # index is 0-based
    global root
    # if v is None:
    #     import pdb; pdb.set_trace()
    if v.size < index:
        return None
    s = v.left.size if v.left else 0
    if s == index:
        root = splay(v)
        return v, root
    elif s < index:
        return find(v.right, index - s - 1)
    else:
        return find(v.left, index)


def append(key):
    global root
    v = Vertex(key, 0, root, None, None)
    update(v)
    root = v


def split(root, key):
    if root is None:
        return None, None
    if key == root.size:
        result, root = find(root, key - 1)
        left = splay(result)
        return left, None
    result, root = find(root, key)
    if result is None:
        return root, None
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


def insert(i, tree, subtree):
    global root
    left, right = split(root, i)
    left = merge(left, subtree)
    root = merge(left, right)


def traverse(tree):
    if tree is None:
        return
    traverse(tree.left)
    print(tree.key)
    traverse(tree.right)


root = None


class Rope:
    def __init__(self, s):
        self.s = s
        for i in s:
            append(i)
        self._result = []

    def traverse(self, tree, init=False):
        if init:
            self._result = []
        if tree is None:
            return
        self.traverse(tree.left)
        self._result.append(tree.key)
        self.traverse(tree.right)

    def result(self):
        self.traverse(root, init=True)
        return ''.join(self._result)

    def process(self, i, j, k):
        global root
        left, right = split(root, i)
        middle, right = split(root, j - i + 1)
        root = merge(left, right)
        insert(k, root, middle)

        # Write your code here
        pass

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
# import pdb
# pdb.set_trace()

# if __name__ == '__main__':
#     for i in 'helloworld':
#         append(i)
#     left, right = split(root, 3)
#     middle, right = split(right, 2 + 1)
#     import pdb
#     pdb.set_trace()
