# -*- coding: utf-8 -*-

import requests

apiKey = '6477caf1d53244d2be0996a51471b5f5'
apiUrl = 'http://www.tuling123.com/openapi/api'

xiaodouKey = 'Rzd5bW49Mj0vZ09hbmh0MEJ1VENReGdWd2hZQUFBPT0'
xiaodouUrl = 'http://api.douqq.com/?key=' + xiaodouKey + '&msg='

GONGNENG = '''
############################################################
# .点歌+歌名(点歌小苹果，输入'停止播放'可停止)
# .报时(输入本地天气)
# .开关灯
# .每日一句
# .抽签
# .猜谜
# .笑话
# .糗事
# .md5+空格+欲加密的内容(md5加密admin)
# .城市名+空气质量(厦门空气质量)
# .城市名+天气(厦门天气)
# .快递+单号(快递1106279322505)
# .翻译+中文(翻译我爱你)
# .一言(一言)
# .人民币数字转大写 大写+数字(大写1542)
# .磁力+电影名称(磁力变形金刚)
# .梦见+梦中的事物(梦见结婚)
# .成语+汉字(成语大智若愚)
# .歌词+歌名(歌词小苹果)
# .疾病名+症状(感冒症状)
# .疾病名+病因(感冒病因)
# .疾病名+怎么治疗(感冒怎么治疗)
# .菜名+的做法(豆沙包的做法)
# .什么是+名词(什么是机器人)
# .历史上的今天
# .百家姓(李)
# .电影+影片名(电影疯狂动物城)
# .短网址+网页地址(短网址http://www.baidu.com)
# .脑筋急转弯(脑筋急转弯)
# .成语接龙
############################################################
'''


def get_response(msg):
    try:
        res = requests.get(xiaodouUrl + msg)
        try:
            if res.text.__contains__("<html>"):
                return get_tuling(msg)
            else:
                return res.text.replace("小豆", "我")
        except Exception:
            return get_tuling(msg)
    except Exception:
        return "小豆无法理解【%s】的含义" % msg


def get_tuling(msg):
    data = {
        'key': apiKey,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        res = requests.post(apiUrl, data=data).json()
        title = res.get('text')
        try:
            return title
        except Exception:
            return "小豆无法理解【%s】的含义" % msg
    except Exception:
        return "小豆无法理解【%s】的含义" % msg
