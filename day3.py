def findDuplicateNumber(arr):
    a = arr[0]
    b = arr[0]
    while True:
        a = arr[a]
        b = arr[arr[b]]
        if a == b:
            break

    a = arr[0]
    while a != b:
        a = arr[a]
        b = arr[b]

    return b


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    result = findDuplicateNumber(arr)
    print(result)
