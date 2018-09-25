# -*- coding: utf-8 -*-

import requests
import json

userId = "your id"
apiKey = "your api key"
apiUrl = "http://openapi.tuling123.com/openapi/api/v2"



xiaodouKey = 'your key'
xiaodouUrl = 'http://api.douqq.com/?key=' + xiaodouKey + '&msg='

GONGNENG = '''
############################################################
# .聊天
# .点歌+歌名(点歌小苹果，输入'停止播放'可停止)
# .报时(输入本地天气)
# .每日一句
# .抽签
# .猜谜
# .笑话
# .糗事
# .md5+空格+欲加密的内容(md5加密admin)
# .城市名+空气质量(厦门空气质量)
# .城市名+天气(厦门天气)
# .翻译+中文(翻译我爱你)
# .一言(一言)
# .人民币数字转大写 大写+数字(大写1542)
# .成语+汉字(成语大智若愚)
# .疾病名+症状(感冒症状)
# .疾病名+病因(感冒病因)
# .疾病名+怎么治疗(感冒怎么治疗)
# .菜名+的做法(豆沙包的做法)
# .什么是+名词(什么是机器人)
# .历史上的今天
# .电影+影片名(电影疯狂动物城)
# .脑筋急转弯(脑筋急转弯)
############################################################
'''


def get_response(msg):
    try:
        res = requests.get(xiaodouUrl + msg)
        if res.text=="":
            return get_tuling(msg)
        else:
            return res.text.replace("小豆", "我")
    except Exception:
        return get_tuling(msg)


def get_tuling(msg):
    
    data = {
        "perception": {
            "inputText": {
                "text": msg
            },
        },
        "userInfo": {
            "apiKey": apiKey,
            "userId": userId
        }
    }
    try:
        res = requests.post(url=apiUrl, data=json.dumps(data))
        b = res.json()
        print(b)
        return b['results'][0]['values'][b['results'][0]['resultType']]       
    except Exception:
        return "我无法理解【%s】的含义" % msg
