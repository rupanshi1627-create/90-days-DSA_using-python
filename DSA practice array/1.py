#We need to tell the complexity of the programme

L=[1,2,3,4,5]
sum=0
for number in L:
    sum=sum+number
    print(sum)
    
product=1
for number in L:
    product=product*number
    print(product)

#TIME COMPLEXITY -- here we have two loops, one for sum and one for product, but they are not nested, so the time complexity is O(n) + O(n) = O(n)
#O(n)+O(n)=O(2n) = O(n)so its linear time complexity. Linear time complexity means that the time taken by the algorithm increases linearly with the size of the input. In this case, as the size of the list L increases, the time taken to compute the sum and product will also increase proportionally.