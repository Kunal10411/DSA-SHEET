# You are given an array of ‘N’ integers. 
# You need to find the length of the longest sequence which contains the consecutive elements.

def Consequetive(arr):
    arr.sort()
    longest=1
    cnt=0
    small=int

    for i in range(n):
        if arr[i]-1 == small:
            cnt+=1
            small=arr[i]

        elif arr[i] != small:
            cnt=1
            small=arr[i]

        longest=max(longest,cnt)        


    return longest




n= int(input("Enter the sixe of array:"))
arr=[]
for i in range(n):
    ele=int(input("Enter the elements:"))
    arr.append(ele)
    print(arr)
print(Consequetive(arr))