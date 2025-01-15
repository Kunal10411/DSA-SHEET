# Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. 
# In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.

#Example 1:
 #Input:
 #nums = [-1,0,1,2,-1,-4]

#Output:
# [[-1,-1,2],[-1,0,1]]

#Explanation:
# Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k

def three_sum(arr):
    arr.sort()
    res = []

    for i in range(len(arr) - 2):  # Iterate through the array up to the third last element
        low = i + 1
        high = len(arr) - 1

        # Skip duplicates for the first element of the triplet
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        while low < high:
            sum = arr[i] + arr[low] + arr[high]

            if sum == 0:
                res.append([arr[i], arr[low], arr[high]])

                # Skip duplicates for the second element
                while low < high and arr[low] == arr[low + 1]:
                    low += 1

                # Skip duplicates for the third element
                while low < high and arr[high] == arr[high - 1]:
                    high -= 1

                # Move pointers after adding a valid triplet
                low += 1
                high -= 1

            elif sum < 0:
                low += 1
            else:
                high -= 1

    return res


# Input the array size and elements
n = int(input("Enter the size of array: "))
arr = []
for i in range(n):
    ele = int(input("Enter the element: "))
    arr.append(ele)

# Output the result
print("Input array:", arr)
print("Triplets with sum zero:", three_sum(arr))
