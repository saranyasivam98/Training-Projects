############ LIST ###########
### Creating a list
lst=[1,2,3,4,5,'Hello', 'World']
### Appending to list
lst.append('Program')
print(lst)

### Accessing the elements
print(lst[0])
print(lst[2:6])
print(lst[:2])
print(lst[-3])

### Slicing
lst_slicing= lst[0:5]
print(lst_slicing)

### Mutating list
lst[5]=6
print(lst)

### Popping the last element
lst.pop()
print(lst)

### Removing
lst.remove('World')
print(lst)

### Deleting
del lst[5]
print(lst)

### Nested lists
lst.append(['This' ,'is', 'nested list'])
print(lst[5][2])

### Deleting the entire list
del lst
print(lst)


########### SETS ###########
### Creating a set
set1={'Jake', 'Amy', 'Gina', 'Holt', 'Joey', 'Ross'}

### Adding elements
set1.add('Charles')
set1.update(['Rosa', 'Terry'])
print(set1)

### Deleting the elements
set1.remove('Joey')
set1.discard('Ross')
print(set1)
print(type(set1))

### Deleting the whole set
set1.clear()
print(set1)

### Set operations
# Defining the sets 
A = {'Ross', 'Joey', 'Chan', 'Ben', 'Carol'}
B = {'Mon', 'Joey', 'Pheebs', 'Chan', 'Emma'}

# union 
print("Union :", A | B) 
  
# intersection 
print("Intersection :", A & B) 
  
# difference 
print("Difference :", A - B) 
  
# symmetric difference 
print("Symmetric difference :", A ^ B)

######### DICTIONARY ##########
# Creating a Dictionary  
# with Integer Keys 
Dict = {1: 'Game', 2: 'of', 3: 'Thrones'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
  
# Creating a Dictionary  
# with Mixed keys 
Dict = {'Name': 'Game of Thrones', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict)

# Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Game', 2: 'of', 3:'Thrones'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Game'), (2, 'of'), (3,'Thrones')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 

# Creating a Nested Dictionary  
# as shown in the below image 
Dict = {1: 'Game', 2: 'of',  
        3:{'A' : 'Thrones', 'B' : 'by', 'C' : 'GRRM'}} 
  
print(Dict)

Dict = {} 
 
  
# Adding elements one at a time 
Dict[0] = 'Game'
Dict[2] = 'Thrones'
Dict[1] = 'of' 
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Adding set of values  
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict)

# Updating existing Key's Value 
Dict[3] = 'by GRRM'
print("\nUpdated key value: ") 
print(Dict)

# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'Ned Stark' : 'Dead', 'Arya Stark' : 'Alive'}} 
print("\nAdding a Nested Key: ") 
print(Dict)

# accessing a element using key 
print(Dict['Value_set'])
print(Dict[5]['Nested'])

# accessing a element using get() method 
print("Accessing a element using get:") 
print(Dict.get(3))

# Deleting a Key value 
del Dict[3] 
print("\nDeleting a specific key: ") 
print(Dict)

# Deleting a key using pop() method 
pop_ele = Dict.pop(1) 
print(Dict)

# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict)

############ TUPLES ##########
# Creating tuples 
  
# One way of creation 
tup = 'Sheldon', 'Amy'
print(tup) 
  
# Another for doing the same 
tup = ('Sheldon', 'Amy') 
print(tup)

# Code for concatenating 2 tuples 
  
tuple1 = ('Sheldon', 'Lee') 
tuple2 = ('Cooper', 'weds', 'Amy')
tuple3 = ('Farah', 'Fowler')  
  
# Concatenating above two 
print(tuple1 + tuple2+tuple3)

# Code for creating nested tuples
tuple4 = (tuple1, tuple2) 
print(tuple4)

### Immutable tuples
tuple1 = (0, 1, 2, 3) 
#tuple1[0] = 4
print(tuple1) 

# code to test slicing 
  
tuple1 = (0 ,1, 2, 3) 
print(tuple1[1:]) 
print(tuple1[::-1]) 
print(tuple1[2:4])

# Code for printing the length of a tuple 
  
print(len(tuple1))

# Code for converting a list and a string into a tuple 
  
list1 = [0, 1, 2] 
print(tuple(list1))


del tuple1
print(tuple1)
