#Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. 
#( Expected: Single pass-O(N) and constant space)
#we are using Dutch National Flag Algorithm



def DNA(arr):
    n=len(arr)
    low=0
    mid=0
    high=n-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1

        elif arr[mid]==1:
            mid+=1

        else:
            arr[mid],arr[high]=arr[high],arr[mid]     
            high-=1
    return arr    
    


n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    x=int(input("enter the elements:\n"))
    arr.append(x)
    print(arr)

print(DNA(arr))