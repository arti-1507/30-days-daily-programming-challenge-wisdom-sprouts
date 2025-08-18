def merge_two_arrays(arr1, arr2, m, n):
    for i in range(m):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]

            first = arr2[0]
            k = 1
            while k < n and arr2[k] < first:
                arr2[k - 1] = arr2[k]
                k += 1
            arr2[k - 1] = first


if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    m, n = len(arr1), len(arr2)

    merge_two_arrays(arr1, arr2, m, n)

    print("arr1:", arr1)
    print("arr2:", arr2)
