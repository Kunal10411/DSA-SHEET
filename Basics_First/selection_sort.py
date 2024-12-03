# Given an array of N integers, write a program to implement the Selection sorting algorithm.

# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52



n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    x=int(input("enter the elements:\n"))
    arr.append(x)
    print(arr)

print(sorted(arr))    


def sort(arr):
    n=len(arr)
    
   
    for i in range(n):
        min_index=i

        for j in range(i+1,n):
            if arr[j]< arr[min_index]:
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr    
