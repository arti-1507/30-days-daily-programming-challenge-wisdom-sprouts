def longest_palindrome(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    start, max_len = 0, 1

    def expand(l, r):
        nonlocal start, max_len
        while l >= 0 and r < n and s[l] == s[r]:
            curr_len = r - l + 1
            if curr_len > max_len:
                max_len = curr_len
                start = l
            l -= 1
            r += 1

    for i in range(n):
        expand(i, i)
        expand(i, i + 1)

    return s[start : start + max_len]


if __name__ == "__main__":
    s = input().strip()
    print(longest_palindrome(s))
