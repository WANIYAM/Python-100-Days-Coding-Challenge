# 6.Print all prime numbers in a given range.

upper_limit=int(input("Enter range"))
for num in range(2,upper_limit):
    is_prime = True
    for i in range(2,num):
        if (num % i) == 0:
            is_prime=False
            break
    if is_prime:
            print(num)

   