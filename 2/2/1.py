import datetime

# date = datetime.date(*map(int, input().split()))
date = datetime.datetime.strptime(input(), '%Y %m %d')
number_of_days = int(input())
result_date = date + datetime.timedelta(days=number_of_days)

print(result_date.year, result_date.month, result_date.day)
