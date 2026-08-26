#N = [2, 7, 11, 15], target = 9

N= [2, 7, 11, 15]
target = 9

N = [2, 7, 11, 15]
target = 9

left = 0                   # left pointer array ke start pe
right = len(N) - 1         # right pointer array ke end pe

while left < right:        # jab tak dono pointers mil na jayein ya cross na karein
    
    current_sum = N[left] + N[right]     # dono ends ke numbers ka sum
    
    if current_sum == target:
        # match mil gaya — answer print karo aur loop se bahar niklo
        print("The two numbers are:", N[left], "and", N[right])
        break
    
    elif current_sum < target:
        # sum chhota hai, humein bada number chahiye
        # array sorted hai, isliye left ko aage badhane se bada number milega
        left += 1
    
    else:
        # sum bada hai, humein chhota number chahiye
        # right ko peeche lane se chhota number milega
        right -= 1
        