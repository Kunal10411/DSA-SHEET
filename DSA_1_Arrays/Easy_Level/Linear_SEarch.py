#Given an array, and an element num the task is to find if num is present in the given array or not. 
# If present print the index of the element or print -1.

# Example 1:
# Input: arr[]= 1 2 3 4 5, num = 3
# Output: 2
# Explanation: 3 is present in the 2nd index

def linear(arr):
    n=len(arr)

    for i in range(n):
        if arr[i]==num:
            return i
        
    return -1

n = int(input("Enter the size of the array: "))
arr = []

for i in range(n):
    ele = int(input(f"Enter element {i + 1}: "))
    arr.append(ele)
    print(arr)
num=int(input("enter the number to be checked:"))    
    
print(linear(arr))    


