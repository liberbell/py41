import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime("%d/%m/%y-%H%M%S%f"))

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime("%d/%m/%y"))