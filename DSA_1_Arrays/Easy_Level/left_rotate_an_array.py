#Given an array of N integers, left rotate the array by one place.

# Example 1:

# Input:
 # N = 5, array[] = {1,2,3,4,5}
# Output:2,3,4,5,1
#Explanation:
 #Since all the elements in array will be shifted 
#toward left by one so ‘2’ will now become the 
#first index and and ‘1’ which was present at 
#first index will be shifted at last.

def rotateleft(arr):
    temp=arr[0]
    n=len(arr)

    for i in range(1,n):
        arr[i-1]=arr[i]

    arr[i-1]=temp
    return arr    


n=int(input("enter the size of the array:"))
arr=[]
for i in range(n):
    ele=int(input("enter the element:"))
    arr.append(ele)
    print(arr)

print(rotateleft(arr))    