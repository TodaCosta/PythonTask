from collections import Counter

n = [10, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 1]
print(Counter(n))
print(Counter(n).most_common())  # Counter({2: 6, 3: 3, 10: 1, 4: 1, 1: 1})
print(dict(Counter(n).most_common()))  # {2: 6, 3: 3, 10: 1, 4: 1, 1: 1}
print(list(Counter(n).most_common()))  # [(2, 6), (3, 3), (10, 1), (4, 1), (1, 1)]
print(Counter(n).most_common(3))  # [(2, 6), (3, 3), (10, 1)]
print(Counter(n).most_common(1)[0][0])  # 2