
"""Working on problems which revolve around Prime Numbers"""

# Inputting multiple values and it only outputs the prime numbers

# prime numbers are only divisible by 1 or itself
# checking for number before inpout as n, would one before
n = int(input())
for i in range(2,n):
    if n % i == 0:
        print("not")
        break
    else:
        print(n)