from datetime import datetime, timedelta, date, time
import pytz  

# specified date
my_date = date(1998, 5, 28)   
print("Date passed as argument is", my_date)

# calling the today function of date class 
today = date.today() 
  
print("Today's date is", today) 
  
# Printing date's components 
print("Date components", today.year, today.month, today.day)

# specified time
my_time = time(13, 24, 56) 
print("Entered time", my_time)

my_time = time(minute=1) 
print("Entered time", my_time)

# Components of time
Time = time(11, 34, 56) 
  
print("hour =", Time.hour) 
print("minute =", Time.minute) 
print("second =", Time.second) 
print("microsecond =", Time.microsecond)

# Initializing constructor 
a = datetime(1999, 12, 12) 
print(a) 
  
# Initializing constructor  
# with time parameters as well 
a = datetime(1999, 12, 12, 12, 12, 12, 342380) 
print(a)

a = datetime(1999, 12, 12, 12, 12, 12) 
  
print("year =", a.year) 
print("month =", a.month) 
print("hour =", a.hour) 
print("minute =", a.minute) 
print("timestamp =", a.timestamp())

# Calling now() function 
today = datetime.now() 
print("Current date and time is", today)

# Using current time  
ini_time = datetime.now()  
    
# printing initial_date  
print ("initial_date", str(ini_time))  
    
# Calculating future dates  
# for two years  
future_date_after_2yrs = ini_time + timedelta(days = 730)  
    
future_date_after_2days = ini_time + timedelta(days = 2)  
    
# printing calculated future_dates  
print('future_date_after_2yrs:', str(future_date_after_2yrs))  
print('future_date_after_2days:', str(future_date_after_2days))

import time
curr_time = time.localtime() 
curr_clock = time.strftime("%H:%M:%S", curr_time) 
  
print(curr_clock) 

# it will get the time zone  
# of the specified location 
IST = pytz.timezone('Asia/Kolkata') 
  
# print the date and time in 
# standard format 
 
print("IST in Default Format : ", datetime.now(IST)) 
  
# print the date and time in  
# specified format 
  
datetime_ist = datetime.now(IST) 
print("Date & Time in IST : ", datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))