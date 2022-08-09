import datetime

b_day = datetime.date(2007, 9, 1)
print("My birthday is", b_day)

today = datetime.date.today()
print("Today's date is", today)

print(b_day.strftime("%A, %B, %d, %Y"))

age = (today - b_day)
print(age)

print(today.isoweekday())

# time

time = datetime.time(8, 30, 45, 1000)
print(time.hour)
print(time.minute)
print(time.second)

# date and timer both

whole_day = datetime.datetime.today()
print(whole_day)

# Time delta

time_delta = datetime.timedelta(days= 20)
print(whole_day - time_delta)

print("--------------------------------")
