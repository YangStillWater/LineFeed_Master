__author__ = 'Peng'
from datetime import timedelta

def count_word(text):
    wlist = text.split()
    return len(wlist)


def line_feed(text, width=40):
    rtn=[]
    while len(text) > width:
        line = text[:width]
        text = text[width:]
        #如果这一行第width个字符是字母或数字
        if str(line[-1]).isalnum():
            for i, s in enumerate(reversed(line[:-1])):
                if not s.isalnum():
                    line, text = line[:-i - 1], line[-i - 1:] + text
                    break
        rtn.append(line)
    rtn.append(text)
    return rtn

def seperate_time(time1,time2,piece):
    delta=(time2-time1)/(piece-1)
    timelist=[]
    for i in range(piece):
        timelist.append(time1+delta*i)
    return timelist

def string_to_timedelta(stime,brackets=True):
    if brackets:
        stime=stime[1:-1]
    min,sec=str(stime).split(sep=':')
    min=int(min)
    sec=float(sec)
    delta=timedelta(minutes=min,seconds=sec)
    return delta

def timedelta_to_string(delta):
    min,sec=divmod(delta.seconds,60)
    min='%02d'%min
    sec='{:02d}.{:02d}'.format(sec,int(delta.microseconds/10000))
    rtn='[{}:{}]'.format(min,sec)
    return rtn

