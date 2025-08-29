def KDistinct(s, k):
    count = {}
    left = 0
    total = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1

        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1

        total += right - left + 1

    return total


def countExactlyKDistinct(s, k):
    if k == 0:
        return 0
    return KDistinct(s, k) - KDistinct(s, k - 1)


if __name__ == "__main__":
    s = input().strip()
    k = int(input().strip())

    result = countExactlyKDistinct(s, k)
    print(result)
