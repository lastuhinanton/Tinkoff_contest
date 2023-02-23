def inscriptions(n1, s1, a1, n2, s2, a2):
    count = 0
    i = j = 0
    while i < n1 and j < n2:
        if s1[i] != s2[j]:
            count += min(a1[i], a2[j])
        if a1[i] < a2[j]:
            i += 1
        else:
            j += 1
    return count

n1 = int(input().strip())
s1 = list(map(int, input().strip().split()))
a1 = list(map(int, input().strip().split()))
n2 = int(input().strip())
s2 = list(map(int, input().strip().split()))
a2 = list(map(int, input().strip().split()))
print(inscriptions(n1, s1, a1, n2, s2, a2))