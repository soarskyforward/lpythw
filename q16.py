import time, datetime

print(time.time())
print(time.localtime())
print(time.asctime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

print(datetime.date.today())
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.date(1949, 2, 1))


#参考q9.py
