#Given an integer N. Print the Fibonacci series up to the Nth term.

# Example 1:
# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)


def fibo(n):
    if n<=1:
        return n
    
    else:
        last=fibo(n-1)
        slast=fibo(n-2)
        return last + slast
    
n=int(input("enter the number for fibonacci:\n"))
print(fibo(n))    