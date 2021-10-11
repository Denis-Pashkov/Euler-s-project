# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
# Какое число является 10001-м простым числом?

count = 4
number = 11

while (count != 10001):
    if (str(number)[-1] in ('1', '3', '7', '9')) and (all(number % n != 0 for n in range(3, (number//2) + 1))):
        count += 1
        if (count == 10001):
            break
        else:
            number += 2
    else:
        number += 2

print(number)

# out:104743
# time:23.26738929748535
