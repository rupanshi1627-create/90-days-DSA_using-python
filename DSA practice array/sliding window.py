numbers = [2, 1, 5, 1, 3, 2]
k = 3

# First window: first k elements
window_sum = sum(numbers[:k])

# Initially, first window is our maximum
max_sum = window_sum

# Start from the element after the first window
for i in range(k, len(numbers)):

    # Remove the element leaving the window
    window_sum -= numbers[i - k]

    # Add the new element entering the window
    window_sum += numbers[i]

    # Update maximum if current window is bigger
    max_sum = max(max_sum, window_sum)

print("Maximum sum =", max_sum)