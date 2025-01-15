#Given an array, print all the elements which are leaders.
#  A Leader is an element that is greater than all of the elements on its right side in the array.

def leaders(arr):
    n=len(arr)
    arr2=[]
    max_from_right=arr[n-1]    #rightmost always the leader

    for i in range(n-2,-1,-1):
        if arr[i] > max_from_right:
            max_from_right=arr[i]
            arr2.append(max_from_right)
    return  arr2        






n= int(input("Enter the sixe of array:"))
arr=[]
for i in range(n):
    ele=int(input("Enter the elements:"))
    arr.append(ele)
    print(arr)

print(leaders(arr))    