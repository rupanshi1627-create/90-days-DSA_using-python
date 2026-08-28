numbers = [2, 1, 5, 1, 3, 2]
k = 3
left=0 #left pointer
right=k #right pointer

#first sum
window_sum=sum(numbers[:3])
max_sum=window_sum #consider abhi yahi sum hai maximum sum

#ab chalayenge loop to get if there is anything else also max sum
#we will use while loop and not for because we need to keep track of the window size and the sum of the elements in the window. in for loop we will not be able to keep track of the window size and the sum of the elements in the window. so we will use while loop.
while right<len(numbers):
    window_sum=window_sum-numbers[left]+numbers[right] #remove the first element of the window and add the next element of the window
    if window_sum>max_sum:
        max_sum=window_sum
        #put condition to check if the current window sum is greater than the max sum, if yes then update the max sum and also update the left and right pointers to the current window.
    left+=1
    right+=1       
print("the maximum sum of array is:", max_sum)
        









