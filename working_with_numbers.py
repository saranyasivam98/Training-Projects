
## Working with numbers
from decimal import Decimal
from fractions import Fraction
import math
from math import pi

x=6
y=7.5
z=24/25
print(type(x), type(y))
print(isinstance(z, float)) #### Division results in float

a=3+4j
print(type(a))

print(2e-2)  ####Exponential form

print(0b111)   ### 0B or 0b for binary
print(0o111)  ### 0o or 0O for octal
print(0x111) ### 0x or 0X for hexadecimal

### Conversion 

print(int(4.59862)) ### Float to int
print(float(10)) ### Int to float
### Complex cannot be converted to int or float.
print(complex(3))  ### Int to complex

### Converting Int to Binary, Octal and Hexadecimal
print(bin(5))
print(oct(5))
print(hex(5))



print(Decimal(3.14))



print(Fraction(0.625))
print(Fraction(7,12))
print(Fraction(Decimal('3.14')))

print(math.ceil(7.5))
print(math.floor(7.5))
print(math.cos(pi))
print(math.fabs(-1.532))  ### Returns the absolute value
print(math.isnan(1))	### If the input value in a numeral
print(math.factorial(5))