a='Chennai Super Kings'
print(a)
### Strings as arrays
print(a[10])

### Looping through the string
for x in 'Chennai Super Kings':
  print(x)

### Length of the string
print(len(a))

### Check if a word or letter is present in a string
print('C' in a)
print('Super' in a)

### Replacing a word or letter
repl=a.replace('Super', 'sooper')
repl=a.replace('a', '@')
print(repl)

### String slicing
new_a= a[0:7]
print(new_a)

### Concatenate strings
a1,a2,a3=a.split() 
final= a1+a2+a3
print(final)

### Enumerate function
list_enumerate = list(enumerate(a))
print(list_enumerate)

### Escape Sequence
print("Sheldon says 'Bazinga' ")
print("Sheldon says \" Bazinga\" ")

# Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('Chandler','Ross','Joey')
print('Default Order:')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('Chandler','Ross','Joey')
print('Positional Order:')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='Chandler',b='Ross',s='Joey')
print('Keyword Order:')
print(keyword_order)

print('chandler'.upper())
print('CHAndler'.lower())

print(' '.join(['Forms', 'a', 'string']))