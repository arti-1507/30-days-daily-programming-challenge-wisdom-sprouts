def findZeroSum(arr):
    n = len(arr)
    prefix_sum = 0
    sum_map = {}
    result = []

    sum_map[0] = [-1]

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum in sum_map:
            for start in sum_map[prefix_sum]:
                result.append((start + 1, i))
            sum_map[prefix_sum].append(i)
        else:
            sum_map[prefix_sum] = [i]

    return result


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    result = findZeroSum(arr)
    print(result)
