# 4.	Find the largest of three numbers.

a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
c=int(input("Enter Third Number"))

if a>b and a>c:
    print("Largest Number is",a)
elif b>a and b>c:
    print("Largest Number is",b)
else:
   print("Largest Number is",c)