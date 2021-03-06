<p align="center">
  <img src="https://i.loli.net/2018/07/22/5b542f5c58d76.jpg" alt="IMG_5686.jpg" title="IMG_5686.jpg" width=250 />
</p>


## 基于树莓派的微信机器人

### 写在前面
本项目采用的是 `itchat` 在 `python3` 的模块，已更新失效的 API，更新过程见[这篇文章](https://yi-yun.github.io/%E5%9F%BA%E4%BA%8E%E6%A0%91%E8%8E%93%E6%B4%BE%E7%9A%84%E5%BE%AE%E4%BF%A1%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%9B%B4%E6%96%B0%E7%89%88/)

### 准备材料
* 搭载 Raspbian 的树莓派3 (只要是带有 python3 的 Linux 的系统都可以)
* 微信个人号 2 个(一个需要登录 WebService ，另一个用来使用)
* DHT11(温湿度传感模块)、LED 灯(两者非必须)
* 音箱一台(耳机也行)
* 腾讯云实名认证账号(用于图床功能非必须，个人喜好才搭建)

### 搭建环境
- 用 PuTTY 或其他远程工具远程登录树莓派，先确认有 python3 环境
```shell 基本环境，最好都加 sudo
sudo pip3 install itchat --upgrade
sudo pip3 install requests BeautifulSoup4
sudo apt-get install mplayer #很多人推荐的音乐播放器，感觉还不错
```

- 有 DHT11 模块的话还需输入
```shell
sudo apt-get install build-essential python-dev
sudo git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install  
```
- 需要图床功能的微信机器人，可以自己搜索相关图床的 API
    - 本人用的是[腾讯云对象存储](https://cloud.tencent.com/document/product/436/10976)，搭建本地即可
    - 也可以使用官网提供的 [Python SDK](https://cloud.tencent.com/document/product/436/12269) ，制作成模块
    - **不需要图床的朋友可以忽略这里，但上传图片会报错**

### 如何运行
```shell
git clone https://github.com/yi-yun/raspi-chatrobot.git
git clone -b master https://github.com/yi-yun/raspi-chatrobot.git #有 DHT11 传感模块和 LED 灯的人输入这个命令

cd raspi-chatrobot
sudo python3 Robot.py #若想后台运行需要运行 sudo apt-get install screen 安装 screen ，然后运行 screen sudo python3 Robot.py &
```
用微信扫码登录命令行中的二维码  
登录成功表示服务端部署完毕  
在另一个微信号向服务端微信号发送`功能`即可获取功能列表，进行愉快地玩耍
### 演示视频
[B站](https://www.bilibili.com/video/av28087089)  
[YouTube](https://youtu.be/m_k38Pbp55U)

### 相关链接
[小豆机器人](http://xiao.douqq.com/)  
[图灵机器人](http://www.tuling123.com/)  
[itchat](https://github.com/littlecodersh/itchat)  
[AdafruitDHT](https://github.com/adafruit/Adafruit_Python_DHT)  

### 写在后面
上述为使用方法  
亲测在 Raspbian (stretch) 上成功运行  
具体代码以及爬坑过程可详见我的[这篇文章](https://yi-yun.github.io/爬坑指南)  
对此感兴趣的小伙伴可以私信或[邮件](mailto:yi--yun@outlook.com)我一起探讨学习  
欢迎各位朋友star、fork 和 Issue

-----
*下学期还有一门课我打算结合MQTT做树莓派机器人V2.0，希望大家不吝赐教*