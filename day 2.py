def missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total - arr_sum


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    missing_num = missing_number(arr)
    print(missing_num)
