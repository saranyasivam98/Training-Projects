### For
lst=[1,2,3,4,5,6]
for ele in lst:
  print(ele**2)

### Range: printing the multiples of 2
for i in range(2,10,2):
  print(i)

### Enumerate
l1 = ["January","February","March"]
s1 = "Olive"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print(list(obj1))
print(list(obj2))

### List comprehension
obj = ["Even" if i%2==0 else "Odd" for i in range(1,20,3)]
print(obj)

### Generators
 #Basic generator functions
import random

def lottery():
  for i in range(6):

    yield random.randint(1,15) 
for ele in lottery():
  print("And the next number is... !" , ele)

### LAMBDA
adder = lambda x, y: x + y
print(adder (1, 2))

# filter() with lambda() 
lst = [i for i in range(2,20)] 
  
filter_list = list(filter(lambda x: (x%2 != 0) , lst)) 
print(filter_list)

# map() with lambda()
lst1 = [i for i in range(6,12)] 
  
map_list = list(map(lambda x: x*2, lst1)) 
print(map_list) 

# reduce() with lambda() 

  
from functools import reduce
lst3 = [5, 8, 10, 20, 50, 100] 
max = reduce(lambda a,b : a if a > b else b, lst3)
print(max)