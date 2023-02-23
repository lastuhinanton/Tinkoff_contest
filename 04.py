def sheep_pens(n, k):
    return (k, (4 * n // 4) * k)

n = int(input().strip())
k = int(input().strip())

min_area, max_area = sheep_pens(n, k)

print(min_area, max_area)

