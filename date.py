
from datetime import datetime
#获取当前日期和时间
#获取当前时间
now = datetime.now()
print('now=',now)
print(type(now))
print('-------------------------1')


#获取指定日期和时间
dt = datetime(2018,4,2,15,30)
print('dt=',dt)

print('-------------------------2')

#datetime转换为timestamp,获取当前时间的时间戳
now = datetime.now()
print(now.timestamp())
print('-------------------------3')

#timestamp也可以直接被转换到UTC标准时区的时间：

print(datetime.fromtimestamp(now.timestamp()))
print('-------------------------4')

#str转换为datetime

day_time = datetime.strptime('2018-4-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print('day_time=',day_time)
print('-------------------------5')

#datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

print('-------------------------6')
#datetime加减
from datetime import datetime, timedelta
now = datetime.now()
print(now)

#加上2小时
print(now+ timedelta(hours=2))
#减去1天
print(now-timedelta(days=1))
#加上1天，2小时
print(now+timedelta(days=1,hours=2))

print('-------------------------7')

