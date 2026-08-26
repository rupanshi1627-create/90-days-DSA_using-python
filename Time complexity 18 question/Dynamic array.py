#Dynamic array 
#lets see we have a list empty
#i want to know how muxh space is allocated to this list-- i will call a function called getsizeof() from sys module
import sys
L=[]
sys.getsizeof(L) #this will give me the size of the list in bytes.
L.append('hello') #now i will add an element to the list
sys.getsizeof(L) #this will give me the size of the list in bytes.
##another way
import sys
l=[]
for i in range(100):
    print(i, sys.getsizeof(l))
    l.append(i)