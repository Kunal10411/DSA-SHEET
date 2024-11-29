#Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

#If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).


def permu(arr):
    n=len(arr)
    ind=-1

# 1.Find the bReakpoint
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            ind=i
            break
# 2. Find someone who is greater than ind but lesser than remaining
    for i in range(n-1,-1,-1):
        if arr[i] > arr[ind]:
            arr[i],arr[ind]=arr[ind],arr[i]
            break
# 3. Now revere the remaining array after ind
    arr[ind + 1:] = reversed(arr[ind + 1:])  # Reversing the remaining     
    return arr



n= int(input("Enter the size of array:"))
arr=[]
for i in range(n):
    ele=int(input("Enter the elements:"))
    arr.append(ele)
    print(arr)
print(permu(arr))    