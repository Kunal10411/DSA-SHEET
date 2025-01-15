# Given an array of N integers. Find the elements that appear more than N/3 times in the array. If no such element exists, return an empty vector.

#Example 1:

#Input Format
# : N = 5, array[] = {1,2,2,3,2}
#Result
#: 2
#Explanation:
# Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.

#Example 2:

#Input Format
#:  N = 6, array[] = {11,33,33,11,33,11}
#Result:
# 11 33

def majority(arr,n):
    hashmap={}

    for num in arr:
        if num in hashmap:
            hashmap[num]+=1

        else:
            hashmap[num]=1

    result=[]
    for num,count in hashmap.items():
        if count > n//3:
            result.append(num)

    return result




n= int(input("Enter the sixe of array:"))
arr=[]
for i in range(n):
    ele=int(input("Enter the elements:"))
    arr.append(ele)
    print(arr)

print(majority(arr,n))