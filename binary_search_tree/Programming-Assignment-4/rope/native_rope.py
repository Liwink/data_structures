# python3
import sys


class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        # Write your code here
        sub = self.s[i: j + 1]
        s = self.s[:i] + self.s[j + 1:]
        self.s = s[:k] + sub + s[k:]

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
