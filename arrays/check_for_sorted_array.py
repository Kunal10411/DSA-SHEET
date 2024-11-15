def check(arr):
    for i in range(1,n):
        if arr[i]>=arr[0]:
            return True
        
        else:
            return False




n=int(input("enter the size o the array:"))
arr=[]
for i in range(n):
    ele=int(input("enter the element:"))
    arr.append(ele)
    print(arr)

if check(arr)==True:
    print("the array is sorted")

else:
    print("the arrray is not sorted")    