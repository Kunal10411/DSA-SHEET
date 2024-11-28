#Given an integer array arr, find the contiguous subarray (containing at least one number) which
#has the largest sum and returns its sum and prints the subarray.

# using Kadane's Algorithm

def Maxi(arr):
    n=len(arr)
    current_sum=0
    max_sum=0

    for i in range(n-1):

        current_sum+=arr[i]

        if current_sum>max_sum:
            max_sum=current_sum

        if current_sum <0:
            current_sum=0
    return max_sum        




n= int(input("Enter the sixe of array:"))
arr=[]
for i in range(n):
    ele=int(input("Enter the elements:"))
    arr.append(ele)
    print(arr)

print(Maxi(arr))    