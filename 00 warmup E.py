#https://contest.yandex.ru/contest/53027/problems/E/
#E. Средний уровень

#засыпался на тестах по превышению времени выполнения
from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip())

scores = list(map(int, lines[1].split()))
rates = []
for score in scores:
    summ = 0
    for item in scores:
        summ += abs(item-score)
    rates.append(str(summ))
print(' '.join(rates))