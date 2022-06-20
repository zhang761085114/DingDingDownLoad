import urllib.parse
import os
import time
import threading


def run():
    os.system("Fiddler\Fiddler.exe")

def Download_Dingding(Video_Num):
    with open("./Fiddler/request_dingding.txt", "r") as file:  # 打开文件
        Ding_Url = file.read()  # 读取文件
        Ding_Url = urllib.parse.unquote(Ding_Url)
        
        oldlist=['']
        newlist=list("http://")
        oldlist=list(Ding_Url)
        for index in range(len(Ding_Url)):
            if oldlist[index]=="a" and oldlist[index+1]=="r"and oldlist[index+2]=="g" and oldlist[index+3]=="s"and oldlist[index+4]=="_"and oldlist[index+5]=="u"and oldlist[index+6]=="r"and oldlist[index+7]=="l":
                for j in range(15,1000):
                    if oldlist[index+j]=="\\":
                        break
                    newlist.append(oldlist[index+j])
                    
        Ding_Url=''.join(newlist) 
        os.system("ffmpeg -i " + '"' + Ding_Url + '"' + " -c copy " + str(Video_Num) + ".mp4")
        print("**********************\n" + "下载完成！" + "\n**********************\n")
        file.close()
        os.remove('./Fiddler/request_dingding.txt')



if __name__ == '__main__':
    thread = threading.Thread(target = run)
    thread.start()
    if(os.path.exists('./Fiddler/request_dingding.txt')):
        os.remove('./Fiddler/request_dingding.txt')
    Video_Num = 1
    while(1):
        if(os.path.exists(r'./Fiddler/request_dingding.txt')):
            time.sleep(5)
            Download_Dingding(Video_Num)
            Video_Num = Video_Num + 1
            
        time.sleep(2)
