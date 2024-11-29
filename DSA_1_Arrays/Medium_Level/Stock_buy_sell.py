#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. 
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def stock(arr):
    n = len(arr)

    # Initialize variables
    mini = arr[0]
    min_index = 0
    profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(1, n):
        # Calculate the potential profit if selling on day i
        cost = arr[i] - mini

        # Update profit and selling day if this profit is higher than the previous maximum
        if cost > profit:
            profit = cost
            buy_day = min_index  # The day we bought at the minimum price
            sell_day = i         # The day we sell for maximum profit

        # Update the minimum price and its index
        if arr[i] < mini:
            mini = arr[i]
            min_index = i

    # Return the maximum profit and the corresponding buy and sell days
    return profit, buy_day, sell_day


# Input array
n = int(input("Enter the size of the array: "))
arr = []
for i in range(n):
    ele = int(input("Enter the element: "))
    arr.append(ele)

# Call the function and print the result
result = stock(arr)
print(f"Maximum Profit: {result[0]}")
print(f"Buy on Day (Index): {result[1]}")
print(f"Sell on Day (Index): {result[2]}")
