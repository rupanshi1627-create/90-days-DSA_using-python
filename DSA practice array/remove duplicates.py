#Problem: Ek function likho jo ek array le aur usme se saare duplicate elements hata de, order maintain karte hue (yani jo pehle aaya wahi rahe, baad wale duplicates hat jayein).
#Input: [4, 5, 4, 3, 5, 8, 3]
#Output: [4, 5, 3, 8]

N=[4, 5, 4, 3, 5, 8, 3 ]
remove_duplicates = [] #this is an empty list which will store the unique elements from the original list N
for number in N:
    if number not in remove_duplicates: #how this checks if the current number is already present in the remove_duplicates list or not. If it is not present, then it will be added to the remove_duplicates list.
        remove_duplicates.append(number)
        
print("Array after removing duplicates:", remove_duplicates)