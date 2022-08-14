# На вход программе подается строка текста из натуральных чисел.
# Из неё формируется список чисел. Напишите программу подсчета количества чисел,
# которые больше предшествующего им в этом списке числа, то есть, стоят вслед за меньшим числом.

n = [int(i) for i in input().split()]
count = 0
for i in range(len(n) - 1):
    if n[i-len(n)+1] > n[i]:
        count += 1
print(count)

#лучше
a = list(map(int, input().split()))
print(a)
print(sum(a[i - 1] < a[i] for i in range(1, len(a))))

print(sum([True, True, True]))