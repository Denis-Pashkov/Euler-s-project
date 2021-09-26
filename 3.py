i = 2
num = 600851475143

while(i <= num):
    if (num % i == 0):
        num /= i
        max_simple_num = i
        i = 2
    else:
        i += 1

print(max_simple_num)

#out:6857
#time:0.002006053924560547
#memory_usage:18.89453125
