#https://contest.yandex.ru/contest/53027/problems/A/
#A. Не минимум на отрезке
from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip())

N, M = list(map(int, lines[0].split()))
a = list(map(int, lines[1].split()))
for i in range(2, len(lines)):
    L, R = list(map(int, lines[i].split()))
    result = 'NOT FOUND'
    if R-L > 1:
        min_value = min(a[L:R+1])
        for item in a[L:R+1]:
            if item != min_value:
                result = item
                break
    else:
        if a[L] != a[R]:
            result = a[L] < a[R] if a[R] else a[L]
    print(result)
