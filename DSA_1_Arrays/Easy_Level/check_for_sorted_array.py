#Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. 
# If the array is sorted then return True, Else return False.

#Note: Two consecutive equal values are considered to be sorted.
# Example 1:

#Input:
# N = 5, array[] = {1,2,3,4,5}
#Output: True.
# Explanation:
 #The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

def check(arr):
    n=len(arr)
    
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
        
    return True




n=int(input("enter the size o the array:"))
arr=[]
for i in range(n):
    ele=int(input("enter the element:"))
    arr.append(ele)
    print(arr)

if check(arr):
    print("the array is sorted")

else:
    print("the arrray is not sorted")    