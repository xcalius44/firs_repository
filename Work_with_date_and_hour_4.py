from datetime import date
import calendar 
import time
import datetime
today_date = date.today()  
current_time = datetime.datetime.now()
# today_time = date.ctime()
days = [31 ,59 ,90 ,120 ,151 ,181 ,212 ,243 ,273 ,304 ,334 ,365]

print("Current date and time:", current_time) 
print("Current year:", today_date.year) 
print("Current month:", today_date.strftime("%B")) 
print("week number of the year:", today_date.strftime("%U") )
print("Current day:", today_date.weekday() + 1)
print("day of year:", today_date.strftime("%j")) 
print("Current day:", today_date.day)
print("Day of Week:", today_date.strftime("%A"))