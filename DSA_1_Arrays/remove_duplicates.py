def dup(arr):
    unique_ele=[]
    n=len(arr)
    for i in arr:
        if i not in unique_ele:
            unique_ele.append(i)

    return unique_ele


n=int(input("enter the size of the array:"))
arr=[]
for i in range(n):
    ele=int(input("enter the element:"))
    arr.append(ele)
    print(arr)

print(dup(arr))    