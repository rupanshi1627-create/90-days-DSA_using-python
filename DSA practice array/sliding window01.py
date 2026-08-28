N = [1, 3, 2, 6, 4, 8]
k = 3

left =0         # kya value?
right =k       # kya value? (Question 4 wala yaad karo)

window_sum = sum(N[0:k])   # pehli window ka sum kaise nikaloge?
averages = []         # result store karne ke liye empty list

first_avg = window_sum / k    # pehli window ka average
averages.append(first_avg)

while right < len(N):
    window_sum = window_sum - N[left] + N[right]    # kaunsa index minus, kaunsa add?
    
    current_avg = window_sum / k    # average kaise nikaloge window_sum se?
    averages.append(current_avg)
    
    left += 1
    right += 1

print(averages)