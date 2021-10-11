# Сумма квадратов первых десяти натуральных чисел равна: 12 + 22 + ... + 102 = 385. Квадрат суммы первых десяти натуральных чисел равен:

# (1 + 2 + ... + 10)2 = 552 = 3025. Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет: 3025 − 385 = 2640.

# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

numbers = [i for i in range(1, 101)]

z = 1
result = 0

for i in numbers:
    new_numbers = numbers[z:]
    for j in new_numbers:
        result += 2*i*j
    z += 1

print(result)

# out:25164150
# time:0.000997304916381836
# memory_usage:18.7