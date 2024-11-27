#Given an array of integers arr[] and an integer target.

#1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

#Brute-force
def twosum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if arr[i]+arr[j]==target:
                return print("yes")
            else:
                return print("No")
     

#optimal one
def twosum2(arr,target):
    n=len(arr)
    Box=set()

    for i in arr:
        complement=target-i
        if complement in Box:
            return "yes"
        Box.add(i)

    return "no"


# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

def index(arr,target):
    n=len(arr)
    index_map={}

    for i,num in enumerate(arr):
        complement=target-num
        if complement in index_map:
            return index_map[complement],i
        index_map[num]=i
    return [-1,-1]    


n= int(input("Enter the sixe of array:"))

arr=[]
for i in range(n):
    ele=int(input("Enter the elements:"))
    arr.append(ele)
    print(arr)

target=int(input("Enter the target number:"))    
print(twosum2(arr,target))
print(index(arr,target))