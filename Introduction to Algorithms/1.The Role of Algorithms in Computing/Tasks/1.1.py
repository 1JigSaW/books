from prettytable import PrettyTable
import math
mytable = PrettyTable()

ms = 1000000
mn = ms*60
hour = mn*60
day = hour*24
month = day*30
year = month*12
y100 = year*100



mytable.field_names = [None, "Секунда", "Минута", "Час", "День", "Месяц", "Год", "Век"]

mytable.add_row(['lgn', math.log(ms), math.log(mn), math.log(hour), math.log(day), math.log(month), math.log(year), math.log(y100)])
mytable.add_row(['√n', math.sqrt(ms), math.sqrt(mn), math.sqrt(hour), math.sqrt(day), math.sqrt(month), math.sqrt(year), math.sqrt(y100)])
mytable.add_row(['n', ms, mn, hour, day, month, year, y100])
mytable.add_row(['nlgn', ms*math.log(ms), mn*math.log(mn), hour*math.log(hour), day*math.log(day), month*math.log(month), year*math.log(year), y100*math.log(y100)])
mytable.add_row(['n^2', ms**2, mn**2, hour**2, day**2, month**2, year**2, y100**2])
mytable.add_row(['n^3', ms**3, mn**3, hour**3, day**3, month**3, year**3, y100**3])
mytable.add_row(['2^n', pow(2, ms), pow(2, mn), pow(2, hour), pow(2, day), pow(2, month), pow(2, year), pow(2, y100)])
mytable.add_row(['n!', math.factorial(ms), math.factorial(mn), math.factorial(hour), math.factorial(day), math.factorial(month), math.factorial(year), math.factorial(y100)])

print(mytable)