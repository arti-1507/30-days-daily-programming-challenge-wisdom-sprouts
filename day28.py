from collections import deque


def build_tree(arr):
    if not arr or arr[0] == "null":
        return None
    root = [int(arr[0]), None, None]
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] != "null":
            node[1] = [int(arr[i]), None, None]
            q.append(node[1])
        i += 1
        if i < len(arr) and arr[i] != "null":
            node[2] = [int(arr[i]), None, None]
            q.append(node[2])
        i += 1
    return root


def is_mirror(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    return a[0] == b[0] and is_mirror(a[1], b[2]) and is_mirror(a[2], b[1])


arr = input().strip().split()

root = build_tree(arr)
print("true" if not root or is_mirror(root[1], root[2]) else "false")
