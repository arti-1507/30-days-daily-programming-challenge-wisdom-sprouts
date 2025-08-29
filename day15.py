def longest_unique_substring(s: str) -> int:
    char_index = {}
    start = 0
    max_length = 0

    for i, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= start:
            start = char_index[ch] + 1
        char_index[ch] = i
        max_length = max(max_length, i - start + 1)

    return max_length


if __name__ == "__main__":
    S = input().strip()
    print(longest_unique_substring(S))
