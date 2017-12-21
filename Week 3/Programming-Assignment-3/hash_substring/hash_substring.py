# python3

multiplier = 263
prime = 1000000007


def hash_func(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans


def precompute_hashes(text, l_p):
    hashes = [0] * (len(text) - l_p + 1)
    hashes[-1] = hash_func(text[-l_p: ])
    y = 1
    for i in range(1, l_p + 1):
        y = y * multiplier % prime
    for i in range(len(text) - l_p - 1, -1, -1):
        hashes[i] = (multiplier * hashes[i + 1] + ord(text[i]) - y * ord(text[i + l_p])) % prime
    return hashes


def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    l_p = len(pattern)
    result = []

    hash_pattern = hash_func(pattern)
    hashes = precompute_hashes(text, l_p)
    for i, h in enumerate(hashes):
        if h == hash_pattern:
            if text[i: i + l_p] == pattern:
                result.append(i)

    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

