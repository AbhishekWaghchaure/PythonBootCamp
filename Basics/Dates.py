from datetime import date
from datetime import time
from datetime import datetime

#todays date
today = date.today()
print("Todays date is ", today)

#individual date components
print("Date components :",today.day,today.month,today.year)

#priniting weekday
print("Todays weekday number: ",today.weekday())
days = ["Mon","Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print("Which is a:", days[today.weekday()])

############################################################

today = datetime.now()
print(today)

# to get the current time
t = datetime.time(datetime.now())
print(t)

#formating date
today = datetime.now()
print(today.strftime("The current year is : %Y"))
print(today.strftime())
