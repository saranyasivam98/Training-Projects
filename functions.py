### Function to find the absolute value
def abs_value(num):


    if num >= 0:
        return num
    else:
        return -num


print(abs_value(2))
print(abs_value(-4))

### Functions as objects
def velocity_squared(v):
    return v*v
def energy(func,arr,m=0.5):
    result=[]
    for i in arr:
        result.append(func(i)*0.5*m)
    return result

result= energy(velocity_squared, [1,2,3,4,5,6])
print(result)

### Understanding the variables of a function
def outer():
    x = 20

    def inner():
        global x
        x = 25
    
    print("Before calling inner: ", x)
    print("Calling inner now")
    inner()
    print("After calling inner: ", x)

outer()
print("x in main: ", x)

### Keyword arguments
def netflix(char_name, series):
  return char_name + ' ' + 'is a character in series' + ' ' + series

print(netflix('Chandler Bing', 'Friends'))
print(netflix(char_name='Sheldon Cooper', series='The Big Bang Theory'))
print(netflix(series='Brooklyn 99', char_name='Jake Peralta'))
print(netflix('Eleanor Shellstrop', series='The Good Place'))

### Arbitary Arguments
def netflx(*names):
  print([name for name in names])
netflx('Chandler Bing', "Monica Geller", 'Joey Tribbiani')

### Default values
def eval_pressure(h,ro=1000, g=9.81):
  return ro*g*h

print(eval_pressure(50))

### Programatically calling functions
def assign_char(chre):
    def wrap_text(ser):
        print(f'{chre} : {ser} ')
    return wrap_text
char_1=assign_char('Chandler Bing')
char_1('Friends')
char_2=assign_char('Jake Peralta')
char_2("Brooklyn 99")

### Arbitary Keyword Arguments
def family(**names):
  print(f'{names["kid_name"]} is the child of {names["mother_name"]} and {names["father_name"]}')

family(father_name = "Chandler Bing", mother_name = "Monica Geller", kid_name="Erica Bing")