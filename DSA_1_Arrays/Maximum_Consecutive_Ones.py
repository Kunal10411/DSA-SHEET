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