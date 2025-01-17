# Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

#Example 1:

#Input Format:
 #N = 4, arr[] = {1,2,2,3}, x = 2
#Result:
 #1
#Explanation:
# Index 1 is the smallest index such that arr[1] >= x.

def lowerbound(arr,n):
    res=[]
    for i in range(n-1):
        if arr[i]<x:
            res.append(arr[i])
    return max(res)



n = int(input("Enter the size of array: "))
x= int(input("Enter the lower bound number:"))
arr = []
for i in range(n):
    ele = int(input("Enter the element: "))
    arr.append(ele)
    print(arr)

print(lowerbound(arr,n))    