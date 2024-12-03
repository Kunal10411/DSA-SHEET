
#Given an array, find the second smallest and second largest element in the array.
#  Print ‘-1’ in the event that either of them doesn’t exist.

#Example 1:

#Input: [1,2,4,7,7,5]
#Output:
 #Second Smallest : 2
#	Second Largest : 5
#Explanation:
 #The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

def largest(arr):
    n=len(arr)
    slarge=-1
    large=arr[0]
    for i in range(0,n):
        if arr[i]>large:
            slarge=large
            large=arr[i]
    
        elif arr[i]>slarge and arr[i]!=large:
            slarge=arr[i]
    return slarge        


n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    x=int(input("enter the elements:\n"))
    arr.append(x)
    print(arr)

print("secordlargest is:",largest(arr))
    
