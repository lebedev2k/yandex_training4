# https://contest.yandex.ru/contest/53027/problems/B/
# B. Сложить две дроби
from sys import stdin
import math

lines = []
for line in stdin:
    lines.append(line.rstrip())

a, b, c, d = list(map(int, lines[0].split()))
m, n = a*d+b*c, b*d
nod = math.gcd(m,n)
print(m//nod, n//nod)
