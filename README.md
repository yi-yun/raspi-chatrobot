<p align="center">
  <img src="https://i.loli.net/2018/07/22/5b542f5c58d76.jpg" alt="IMG_5686.jpg" title="IMG_5686.jpg" width=250 />

</p>



## 基于树莓派的微信机器人

### 写在前面
本项目采用的是```itchat```在```python3```的模块

### 准备材料
* 搭载 Raspbian 的树莓派3 (只要是带有 python3 的 Linux 的系统都可以)
* 微信个人号 2 个(一个需要登录 WebService ，另一个用来使用)
* DHT11(温湿度传感模块)、LED 灯(两者非必须)
* 音箱一台(耳机也行)

### 搭建环境
用 PuTTY 或其他远程工具远程登录树莓派，先确认有 python3 环境
```shell
pip3 install itchat 
pip3 install requests
pip3 install BeautifulSoup4
sudo apt-get install mplayer #很多人推荐的音乐播放器，感觉还不错
```

有 DHT11 模块的话还需输入
```shell
sudo apt-get install build-essential python-dev
sudo git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install  
```

### 如何运行
```shell
git clone https://github.com/yi-yun/raspi-chatrobot.git
git clone -b dhtnoled https://github.com/yi-yun/raspi-chatrobot.git #没有 DHT11 传感模块和 LED 灯的人输入这个命令

cd raspi-chatrobot
sudo python3 Robot.py #若想后台运行可在最后面加 &
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
具体代码以及爬坑过程可详见我的[博客](https://yi-yun.github.io/2018/07/30/%E7%88%AC%E5%9D%91%E6%8C%87%E5%8D%97/#more)  
对此感兴趣的小伙伴可以私信或[邮件](mailto:yi--yun@outlook.com)我一起探讨学习  
欢迎各位朋友star、fork 和 Issue

-----
*下学期还有一门课我打算结合MQTT做树莓派机器人V2.0，希望大家不吝赐教*