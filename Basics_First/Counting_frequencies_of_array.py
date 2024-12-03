#Given an array, we have found the number of occurrences of each element in the array.

# Example 1:
# Input: arr[] = {10,5,10,15,10,5};
# Output: 10  3
#	 5  2
 #       15  1
# Explanation: 10 occurs 3 times in the array
#	      5 occurs 2 times in the array
 #             15 occurs 1 time in the array

def count(arr):
    frequency_map={}
    
    for element in arr:
        if element in frequency_map:
            frequency_map[element]+=1

        else:
            frequency_map[element]=1
    return frequency_map


n=int(input("enter the size of the array:\n"))
arr=[]
for _ in range(n):
    x=int(input("enter the elements:\n"))
    arr.append(x)
    print(arr)

frequency_map=count(arr)    
print(frequency_map)