# Count Number of Divisors - HackerRank Style


def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:  # perfect square case
                count += 1
            else:
                count += 2  # i and n//i
        i += 1
    return count


if __name__ == "__main__":
    # HackerRank style input
    N = int(input().strip())

    # Compute and print result
    print(count_divisors(N))
