# ZiDongGuoJuQing
一个用于原神游戏自动过剧情的工具。
原理是在出现剧情的环节模拟鼠标点击，快速跳过对话。

这个程序在我这里用的效果很好，能节省大量的时间，但它仍然是有缺点的，那就是【移植性不太好】。
因为每个玩家的屏幕分辨率是不同的，是否开启全屏游戏也因人而异，所以如果别人下载使用这个代码，截图区域的坐标和模板图片都【必须】根据自己的情况来重新设定。
我把源码公开，大家一起边改进吧，欸嘿~

------

更新：加入了build.py，使用python3 build.py可自动打包成exe文件，可以发送给你的好友~前提是装了pyinstaller。

更新（2025/1/3)：自动识别对话气泡，能够自动点击气泡。
