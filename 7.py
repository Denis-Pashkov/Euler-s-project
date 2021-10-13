# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
# Какое число является 10001-м простым числом?

count = 4
number = 11
numbers = [2, 3, 5, 7]

while (count != 10001):
    if (str(number)[-1] != ('5')) and (all(number % n != 0 for n in numbers)):
        count += 1
        if (count != 10001):
            numbers.append(number)
            number += 2
        else:
            break
    else:
        number += 2

print(number)

# out:104743
# time:4.295078754425049
