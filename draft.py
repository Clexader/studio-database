import datetime

date_str = '09-19-2018'
date = '2020-09-19'
date_object = datetime.datetime.strptime(date, '%Y-%m-%d').date()
print(type(date_object))
print(date_object)


