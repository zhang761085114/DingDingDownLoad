# DingDingDownLoad

        目前钉钉的直播回放只能保存12个月，但一些重要直播网课可能是一辈子都需要回看的，此时管理员还设置了不可下载的权限

![image](https://user-images.githubusercontent.com/41890243/174531819-23b3f9f3-0f58-4e76-b1df-055d1786fc59.png)

        首先电脑上打开fiddler，点击直播回放，看个2、3秒，然后关闭，此时可以看到抓包结果

![image](https://user-images.githubusercontent.com/41890243/174531932-521f45de-79be-4c48-a6c0-93aa2cfad4d5.png)

搜索.m3u8，发现该网址里含有m3u8字段

        为什么搜索.m3u8字段，因为钉钉一直以来的防范策略是这样的，服务器会下发一个m3u8文件，里面包含了许多个短视频链接，这些短视频拼接起来就是一个完整的直播回放。每次用户观看直播回放的时候，钉钉会一点一点地下载，直到你看完，才会将所有短视频下载下来。总不能为了下载这一个回放，又将它完整看一遍吧。
        
![image](https://user-images.githubusercontent.com/41890243/174532052-79ed3467-8120-42b8-8047-b1655477537a.png)

通过url解密得到m3u8文件的下载链接（记得自己在前面加个https://），知道该链接后，就可以使用ffmpeg来下载整合视频了。ffmpeg直接在网上下载，下载好后，在bin目录下执行以下cmd命令：ffmpeg -i "m3u8下载链接" -c copy 整合好的.mp4

        最后本人进行了一波优化，用python脚本+bat命令行文件+fiddler实现了全自动直播回放下载软件。
