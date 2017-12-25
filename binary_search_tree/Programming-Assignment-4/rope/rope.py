# python3


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
    if v.size < index:
        return None
    s = v.left.size if v.left else 0
    if s == index:
        root = splay(v)
        return v
    elif s < index:
        return find(v.right, index - s - 1)
    else:
        return find(v.left, index)


def append(key):
    global root
    v = Vertex(key, 0, root, None, None)
    update(v)
    root = v


def split(v, tree):
    pass


def merge(left, right):
    pass


def insert(i, tree, subtree):
    pass

root = None


class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        global root
        s1, s2 = split(i, root)
        s2, s3 = split(j, s2)
        root = merge(s1, s3)
        insert(k, root, s2)

        # Write your code here
        pass

# rope = Rope(sys.stdin.readline().strip())
# q = int(sys.stdin.readline())
# for _ in range(q):
#     i, j, k = map(int, sys.stdin.readline().strip().split())
#     rope.process(i, j, k)
# print(rope.result())

if __name__ == '__main__':
    for i in 'hello':
        append(i)
    import pdb
    pdb.set_trace()
