#https://contest.yandex.ru/contest/53027/problems/D/
#D. Анаграмма?
from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip())

a1 = sorted([ord(i) for i in lines[0]])
a2 = sorted([ord(i) for i in lines[1]])
if a1 == a2:
    print('YES')
else:
    print('NO')