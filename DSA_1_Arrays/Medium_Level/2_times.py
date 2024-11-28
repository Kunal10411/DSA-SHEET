#Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. 
# You may consider that such an element always exists in the array.

# use hashing
def Maj(arr):
    n=len(arr)
    Box={}

    for num in arr:
        if num in Box:
            Box[num]+=1
        else:
             Box[num]=1   

        if Box[num]> n/2:
            return num    
    return None    





n= int(input("Enter the sixe of array:"))
arr=[]
for i in range(n):
    ele=int(input("Enter the elements:"))
    arr.append(ele)
    print(arr)

print(Maj(arr))    