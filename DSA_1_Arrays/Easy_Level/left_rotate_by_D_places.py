#Given an array of integers, rotating array of elements by k elements either left or right.

# Example 1:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .

def rotate_by_D(arr,d):
    n = len(arr)  # Calculate the length of the array
    temp = arr[:d]  # Store the first d elements in temp
    for i in range(d, n):
        arr[i - d] = arr[i]

    for i in range(n - d, n):
        arr[i] = temp[i - (n - d)]

    return arr

# Change 'n' to 'arr' in the function call
arr = [1, 4, 5, 3, 2]  # Define arr
print(rotate_by_D(arr, 3))