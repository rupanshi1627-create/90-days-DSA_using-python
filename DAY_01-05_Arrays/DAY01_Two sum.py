#Brute Force Approach (Basic Thinking)
class Solution:
    def twoSum(self, nums, target):
        # Loop through all pairs
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                # Check if sum equals target
                if nums[i] + nums[j] == target:
                    return [i, j]
#in leetcode it calls function by default, so we don't need to create object of class and call function, but here in vscode we are doing it for demonstration purpose.
# Create object of class
obj = Solution()

# Input
nums = [2, 7, 11, 15]
target = 9

# Call function and print result
print(obj.twoSum(nums, target))
print(nums[0], nums[1])  # This will print the values at indices 0 and 1, which are 2 and 7 respectively.
