# -*- coding: utf-8 -*-

import requests
import json

def get_musicurl(text):
    try:
        url = 'http://s.music.163.com/search/get/?src=lofter&type=1&filterDj=true&s='+text+'&limit=2&offset=0&callback=loft.w.g.cbFuncSearchMusic'
        res = requests.get(url)
        j = json.loads(res.text[27:-1])
        id = j['result']['songs'][0]['id']
        _url = 'http://music.163.com/song/media/outer/url?id='+str(id)+'.mp3'
        return _url
    except Exception:
        return "我找不到歌名【%s】" % text