import datetime

date = datetime.datetime.now()

print(date)
print("year   =", date.year)
print("month  =", date.month)
print("day    =", date.day)
print("hour   =", date.hour)
print("minute =", date.minute)
print(date.strftime("%A"))
