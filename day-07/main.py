# Generate Fibonacci series up to n terms
 
def  Fibonacci(n):
    
    a,b=0,1
    for i in range(n):
       print(a ,end=" ")
       c=a+b
       a=b
       b=c

Fibonacci(10)



