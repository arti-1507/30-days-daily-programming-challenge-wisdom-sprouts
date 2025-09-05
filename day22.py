def first_element_to_repeat_k_times(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in arr:
        if freq[num] == k:
            return num

    return -1


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    k = int(input().strip())
    print(first_element_to_repeat_k_times(arr, k))
