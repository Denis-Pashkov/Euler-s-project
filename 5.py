# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

a = [i for i in range(2, 21)]

def razlojenie(a):
    i = 2
    new_array = []
    while(i <= a):
        if (a % i == 0):
            a /= i
            new_array.append(i)
            i = 2
        else:
            i += 1
    new_array.sort()
    return(new_array)

b = a
z = {}

for i in range(len(a)):
    h = razlojenie(a[i])
    y ={}
    for j in h:
        name = str(j)
        y[j] = y.get(j,0) + 1
        if (z.get(name) == None):
            z[name] = y[j]
        else:
            if (z[name] < y[j]):
                z[name] = y[j]

res = 1

for i in z:
    key = str(i)
    value = z[key]
    res *= int(key)**int(value)

print('res = ', res)

# out:232792560
# time:0.0009737014770507812
