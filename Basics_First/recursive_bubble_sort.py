#Given an array of N integers, write a program to implement the Recursive Bubble Sort algorithm.

# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52


def recursive_bubbble(arr,n=None):
    if n is None:
        n=len(arr)
    if n==1:
        return
    
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]

    recursive_bubbble(arr,n-1)

n=int(input("enter the size of the array:"))
arr=[]
for _ in range(n):
    ele=int(input("enter the elements:"))
    arr.append(ele)
    print(arr)

recursive_bubbble(arr)
print(arr)










