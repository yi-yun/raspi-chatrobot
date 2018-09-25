# -*- coding: utf-8 -*-

import itchat

from itchat.content import *
import Chat
import Imgbed
itchat.auto_login(hotReload=True,enableCmdQR=2)


@itchat.msg_register(TEXT)
def text_reply(msg):
    return Chat.has_music(msg['Text'])


@itchat.msg_register([MAP, CARD, NOTE, SHARING])
def map_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(PICTURE)
def add_friend(msg):
    msg.download(msg.fileName)
    return Imgbed.get_url(msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()

itchat.run()
