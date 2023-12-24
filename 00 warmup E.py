# https://contest.yandex.ru/contest/53027/problems/E/
# E. Средний уровень

# засыпался на тестах по превышению времени выполнения
from sys import stdin
from itertools import accumulate

lines = []
for line in stdin:
    lines.append(line.rstrip())

scores = list(map(int, lines[1].split()))
accum_scores = list(accumulate(scores, initial=0))
n = len(scores)
rates = [str(i * scores[i] - accum_scores[i] + accum_scores[-1] - accum_scores[i + 1] - (n - i - 1) * scores[i])
         for i in range(n)]
print(' '.join(rates))

# 1 solution, bug: low speed
# for score in scores:
#     summ = 0
#     for item in scores:
#         summ += abs(item-score)
#     rates.append(str(summ))

