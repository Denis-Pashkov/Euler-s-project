# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
# a2 + b2 = c2
# Например, 32 + 42 = 9 + 16 = 25 = 52.
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

res = 0

for a in range(100, 450):
    for b in range(100, 450):
        hypotenuse = (a**2 + b**2)**0.5
        if hypotenuse % 1 == 0 and (a + b + hypotenuse == 1000):
            res = int(a*b*hypotenuse)
            break

print(res)

# out:31875000
# time:0.13866138458251953

# Alternative

n = 1
m = 2

while True:
    summ = m**2 + m * n
    if summ < 500:
        m += 1
    elif summ > 500:
        n += 1
        m = n + 1
    else:
        break

a = m**2 - n**2
b = 2 * m * n
c = m**2 + n**2

print (a * b * c)

# out:31875000
# time:0.0009865760803222656
