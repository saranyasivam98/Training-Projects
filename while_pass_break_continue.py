i=1
while i<21:
  if i%5==0:
    print(i,'is divisible by 5')
  i=i+1 

#break the loop if number is 7
i=1
while i<21:
  if i%7==0:
    break
  else:
    print(i)
  i=i+1
#skip numbers divisible by 4
i=1
while i<21:
  if i%4==0:
    i=i+1
    continue
  print(i)
  i=i+1

#pass statement
a = 'Chennai Super Kings'
i = 0
  
while i < len(a): 
    i += 1
    pass
print('Length of the string :', i)