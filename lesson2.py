# n = int (input("Введите целое неотрицательное число: "))
# res = 1
# i = 1

# while i <= n:
#     res *= i
#     i += 1

# print (res)

n = int(input('Введите N : '))
min = float('inf')
max = 0
for i in range(n):
    a = int(input())
    if a < min:
        min = a
    if a > max :
        max = a
print(f'{min} {max}')