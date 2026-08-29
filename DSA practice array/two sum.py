def two_sum(nums, target):
    seen = {}  # value -> index (yehi hamari "notebook" hai)
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # no solution found

# Example
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]