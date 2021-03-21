#####                                     DATETIME
### Firstly we need tp import the datetime module in python.



## Example: Get Current Date and Time
import datetime as dt  ## Here we have imported datetime module using import datetime statement.

currentdatetime = dt.datetime.now()
print(currentdatetime)

##Example 2: Get Current Date
todaysdate = dt.date.today()
print(todaysdate)



#####                                  datetime.timedelta
###             A timedelta object represents the difference between two dates or times.

##Example: Difference between two dates and times

from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3))
print("type of t6 =", type(t6))



## Example: Difference between two timedelta objects
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)




####                              Python strftime() - datetime object to string
###                      The strftime() method is defined under classes date, datetime and time.
###                  The method creates a formatted string from a given date, datetime or time object.

###Example: Format date using strftime()
from datetime import datetime

# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)

# mm/dd/YY H:M:S format
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("s1:", s1)

# dd/mm/YY H:M:S format
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("s2:", s2)


####                                    Python strptime() - string to datetime
###                 The strptime() method creates a datetime object from a given string (representing date and time).

## Example: strptime()

from datetime import datetime

date_string = "05 March, 2021"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)



