#Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

#Example 1:

#Input: prices = {1, 1, 0, 1, 1, 1}

#Output: 3

#Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

def Cons(arr):
    n=len(arr)
    maxi=0
    cnt=0

    for i in range(n):
        if arr[i]==1:
            cnt+=1
            maxi=max(maxi,cnt)

        else:
            cnt=0
    return maxi            


n= int(input("Enter the sixe of array:"))
arr=[]
for i in range(n):
    ele=int(input("Enter the elements:"))
    arr.append(ele)
    print(arr)

print(Cons(arr))