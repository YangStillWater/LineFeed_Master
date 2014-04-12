__author__ = 'Peng'
from linefeed import *

text='[00:00.49]The Moon is likely to become the industrial hub of the Solar System, supplying the rocket fuels fro its ships, easily obtainable from the lunar rocks in the from of liquid oxygen.'

lst=line_feed(text)
print('\n'.join(lst))

t1=convert_to_timedelta('[01:00.49]')
t2=convert_to_timedelta('[01:03.49]')
sep=seperate_time(t1,t2,3)
print(sep)