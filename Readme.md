# ZiDongGuoJuQing
## EN

A tool for automatically skipping dialogues in the game Genshin Impact.
The principle is to simulate mouse clicks during dialogue scenes to quickly skip conversations.

This program works very well for me and saves a lot of time, but it still has a drawback: **poor portability**.
Since each player's screen resolution is different, and whether fullscreen mode is enabled varies from person to person, if someone else downloads and uses this code, they **must** reconfigure the screenshot area coordinates and template images according to their own setup.

I’ve made the source code public, so let’s improve it together! Hehe~

------

Update: Added build.py. Using `python3 build.py` can automatically package it into an exe file, which you can send to your friends~ (provided that pyinstaller is installed).

Update (2025/1/3): Added automatic detection of dialogue bubbles, which can automatically click on the bubbles. It is suitable for 2K resolution screens.

## 中文

一个用于原神游戏自动过剧情的工具。
原理是在出现剧情的环节模拟鼠标点击，快速跳过对话。

这个程序在我这里用的效果很好，能节省大量的时间，但它仍然是有缺点的，那就是【移植性不太好】。
因为每个玩家的屏幕分辨率是不同的，是否开启全屏游戏也因人而异，所以如果别人下载使用这个代码，截图区域的坐标和模板图片都【必须】根据自己的情况来重新设定。
我把源码公开，大家一起边改进吧，欸嘿~

------

更新：加入了build.py，使用python3 build.py可自动打包成exe文件，可以发送给你的好友~前提是装了pyinstaller。

更新（2025/1/3)：自动识别对话气泡，能够自动点击气泡。适用于2k分辨率屏幕。对于多屏或者笔记本屏幕(?)，可能点不到气泡，因为win32api的cursor函数使用的坐标和窗口坐标会不一致。我在笔记本上玩时需要对max_loc乘以0.5711得到cursor使用的坐标。
