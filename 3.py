import math as mt
i = 1
num = 600851475143
simle_factors = []

while(i < num):
    result = mt.prod(simle_factors)
    if (result < num):
        if ((num % i == 0)):
            simle_factors.append(i)
    else:
        break
    i += 1

print('Answer: ', simle_factors[-1])
