# -*- coding: utf-8 -*-
import os
import re

def get_url(text):
    try:
        os.system('coscmd upload %s %s' % (text, text))
        url = "Your url"
        return '![](' + url + text + ')'
    except Exception:
        return '上传失败'