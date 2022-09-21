def count_c(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0

    return count_c(n-1, k) + count_c(n-1, k - 1)


n, k = map(int, input().split())
print(count_c(n, k))
