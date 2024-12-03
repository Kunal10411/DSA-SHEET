#Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52

def bubble(arr):

    n=len(arr)
    

    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True

        if not swapped:
            break
    return arr    


n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    ele=int(input("enter the elements: "))
    arr.append(ele)
    print(arr)

print("sorted array:",bubble(arr))





