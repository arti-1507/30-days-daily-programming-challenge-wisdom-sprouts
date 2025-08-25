def permute_unique(s):
    result = []
    chars = list(s)
    chars.sort()
    used = [False] * len(chars)

    def back(path):
        if len(path) == len(chars):
            result.append("".join(path))
            return
        for i in range(len(chars)):
            if used[i]:
                continue
            if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(chars[i])
            back(path)
            path.pop()
            used[i] = False

    back([])
    return result


if __name__ == "__main__":
    s = input().strip()
    ans = permute_unique(s)
    print(ans)
