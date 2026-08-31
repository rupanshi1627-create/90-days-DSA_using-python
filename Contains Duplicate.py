def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True      # pehle bhi dekha ja chuka hai
        seen.add(num)
    return False

# Example
print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False