def groupAnagrams(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


if __name__ == "__main__":
    strs = input().strip().split()
    result = groupAnagrams(strs)
    print(result)
