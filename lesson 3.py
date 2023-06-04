# Последовательностью Фибоначчи называется
# последовательность чисел a0# , a1 , ..., an , ..., где
# a0  = 0, a1  = 1, ak  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
 
# print(fib(int(input())))


# n = int(input())
# a = list(map(int, input().split()))

# min_ = 10
# max_ = -10

# for el in a:
# 	if el > max_:
# 		max_ = el
# 	if el < min_:
# 		min_ = el

# for i in range(n):
# 	if a[i] == max_:
# 		a[i] = min_

# print(*a)


# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# def isPrime(n):
#     d = 2
#     while d*d <= n and n % d != 0:
#         d +1= 1
#     return d * d> n
# n = int (input())

# if isPrime (n):
#     print('yes')
# else:
#     print('no')

n = int (input('Введите число'))
my_list = [x for x in range(1,n+1)]

my_list.reverse()
res = 0 
for i in my_list:
    if n == i:
        res += 1
print(my_list)








# i = len(my_list)
# while i != 0:
#        print(my_list[i-1], end= " ")
# i -= 1