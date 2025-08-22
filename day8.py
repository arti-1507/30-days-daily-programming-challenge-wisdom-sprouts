def reverseWords(s):
    n = len(s)
    words = []
    word = ""

    for i in range(n):
        if s[i] != " ":
            word += s[i]
        else:
            if word:
                words.append(word)
                word = ""

    if word:
        words.append(word)

    result = ""
    for i in range(len(words) - 1, -1, -1):
        result += words[i]
        if i != 0:
            result += " "

    return result


if __name__ == "__main__":
    s = input().strip()
    print(reverseWords(s))
