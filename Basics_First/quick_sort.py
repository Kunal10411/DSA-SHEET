 #Given an array of n integers, sort the array using the Quicksort method.

# Example 1:
# Input:  N = 5  , Arr[] = {4,1,7,9,3}
# Output: 1 3 4 7 9 

# Explanation: After sorting the array becomes 1, 3, 4, 7, 9


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        # Move `i` to the right until an element greater than the pivot is found
        while arr[i] <= pivot and i < high:
            i += 1
        # Move `j` to the left until an element less than or equal to the pivot is found
        while arr[j] > pivot and j > low:
            j -= 1
        # Swap elements at `i` and `j` if they are in the wrong order
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        p_index = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr, p_index + 1, high)

def quick_sort_main(arr):
    quick_sort(arr, 0, len(arr) - 1)

    return arr
    
    

# Example usage
arr = [4, 6, 2, 5, 7, 9, 1, 3]
print("Before Using Quick Sort:")
print(arr)

sorted_arr = quick_sort_main(arr)
print("After Using Quick Sort:")
print(sorted_arr)
