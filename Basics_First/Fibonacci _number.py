def fibo(n):
    if n<=1:
        return n
    
    else:
        last=fibo(n-1)
        slast=fibo(n-2)
        return last + slast
    
n=int(input("enter the number for fibonacci:\n"))
print(fibo(n))    