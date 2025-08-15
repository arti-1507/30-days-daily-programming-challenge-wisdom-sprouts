def sort012(arr):
    c0 = c1 = c2 = 0
    for x in arr:
        if x == 0:
            c0 += 1
        elif x == 1:
            c1 += 1
        else:
            c2 += 1

    idx = 0
    for _ in range(c0):
        arr[idx] = 0
        idx += 1
    for _ in range(c1):
        arr[idx] = 1
        idx += 1
    for _ in range(c2):
        arr[idx] = 2
        idx += 1

    return arr


arr = [0, 1, 2, 1, 0, 2, 1, 0]
print(sort012(arr))
