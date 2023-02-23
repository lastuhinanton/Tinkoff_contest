def minimum_days(n, x, bonuses):
    total = 0
    days = 0
    while total < x:
        if days >= n:
            total -= bonuses[n - 1] * (days // n - 1)
        if days < n:
            total += bonuses[days]
        days += 1
        print(1)
    return days if total == x else -1

n, x = map(int, input().strip().split())
bonuses = list(map(int, input().strip().split()))
print(minimum_days(n, x, bonuses))