# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

res = 0

def fun_1(array_num):
    if (array_num == array_num[::-1]):
        array_num = int(array_num)
        return(True)
    else:
        return(False)

for i in range(100, 1000):
    for j in range(100, 1000):
        array_num = i * j
        array_num = str(array_num)
        if (fun_1(array_num) == True):
            array_num = int(array_num)
            if (array_num > res):
                res = array_num
                break

print(res)

#out:906609
#time:0.7156836986541748
#memory_usage:18.75
