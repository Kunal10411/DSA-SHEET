def check(arr):
    n=len(arr)
    
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
        
    return True




n=int(input("enter the size o the array:"))
arr=[]
for i in range(n):
    ele=int(input("enter the element:"))
    arr.append(ele)
    print(arr)

if check(arr):
    print("the array is sorted")

else:
    print("the arrray is not sorted")    