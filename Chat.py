# -*- coding: utf-8 -*-

import Tuling 
import Weather 
import time
import re
import os
import threading 
import led 
     
def play(url):
    os.system('mplayer "%s"' % url)
    
def has_music(text):
    thre=threading.Thread();
    if text[0].__eq__("点") and text[1].__eq__("歌"):
        reply = Tuling.get_response(text)
        pattern=re.compile(r'http://zhangmenshiting.*')
        url=re.findall(pattern,reply)
        url=url[0][0:-1]
        thre=threading.Thread(target=play,args=[url])
        thre.start()
    elif text.__contains__("停止"):
        os.system('killall -9 mplayer' )
    else:
        return deng(text)

def deng(text):
    if text[0].__eq__("开") and text[1].__eq__("灯"):
        led.on()
    elif text[0].__eq__("关") and text[1].__eq__("灯"):
        led.off()
    else:
        return has_weather(text)

def has_weather(text):
    if text[-2].__eq__("天") and text[-1].__eq__("气"):
        if text.__contains__("本地"):
            return Weather.main()
        else:
            return no_music_distance(text)
    else:
        return no_music_distance(text)


def no_music_distance(text):
    if '功能' in text:
        return Tuling.GONGNENG
    elif '时间' in text or '几点' in text:
        return "现在是北京时间{}".format(time.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        reply = Tuling.get_response(text)
        return reply
