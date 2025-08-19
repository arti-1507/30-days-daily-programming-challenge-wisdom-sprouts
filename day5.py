def findLeaders(arr, n):
    leader = []
    max = arr[-1]
    leader.append(max)

    for i in range(n - 2, -1, -1):
        if arr[i] >= max:
            leader.append(arr[i])
            max = arr[i]

    leader.reverse()
    return leader


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    n = len(arr)
    output = findLeaders(arr, n)
    print(output)
