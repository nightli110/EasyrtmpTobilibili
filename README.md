# EasyrtmpTobilibili
B站 rtmp推流脚本  

环境：  
1. python3  
2. ffmpeg
3. ffmpy3


conf文件：  
dir  视频目录

live_address与live_code 为rtmp地址和直播码,B站可以在直播管理中找到

食用方法：
修改conf中dir，live_address,live_code  
安装环境，运行  
```
python listvideo.py
```
生成ideolist.csv 可以手动改其中的播放顺序
运行：
```
python publishrtmp.py
```
可以用nohup和tmux等来守护进程