def merge_sort(arr, low, high):
    # Base case: if there's only one element, it's already sorted
    if low < high:
        # Calculate the middle point
        mid = (low + high) // 2

        # Recursively sort the two halves
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        # Merge the sorted halves
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    # Create temporary arrays to hold the left and right sublists
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    # Initialize pointers for left, right, and the main array
    i = j = 0
    k = low

    # Merge the two sorted sublists into the main array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements of left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements of right
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
