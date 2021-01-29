### If-else statements
x=20
a='Chennai Super Kings'
if x%3==0:
  print('Number is divisible by 3')
else:
  print('Number is not divisible by 3')


#Elif statements
if x%3==0:
  print('Number is divisible by only 3 not 5')
elif x%5==0:
  print('Number is divisible by only 5 and not 3')
else:
  print('Number is not divisible by 3 and 5')

#Nested if

if x%3==0:
  if x%5==0:
      print('Number is divisible by both 3 and 5')
  else:
      print('Number is only divisible by 3 and not 5')
else:
    if x%5==0:
      print('Number is divisible by 5')
    else:

        print('Number is not divisible by both 3 and 5')