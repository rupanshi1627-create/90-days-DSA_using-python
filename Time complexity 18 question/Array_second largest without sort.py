#Question 1 (Easy) — Warm-upProblem: 
# Ek array diya hai integers ka. Tumhe uska second largest element dhoondhna hai — bina Python ka sort() use kiye.
#first using sort() function
#N=[4,1,7,3,9,2]
#N.sort()
#print(N[-2]) #this will give me second largest element in the list N
#second method without using sort() function
N=[4,1,7,3,9,2]
largest=N[0]
second_largest=None

for number in N:
    if number > largest: #consider the current number is greater than the largest number found so far
        second_largest = largest
        largest = number
    elif second_largest is None or number > second_largest: #if the current number is not greater than the largest number but is greater than the second largest number found so far
        second_largest = number # because the current number is greater than the second largest number found so far, we update the second largest number to be the current number
  
print("Second largest element is:", second_largest)      
    