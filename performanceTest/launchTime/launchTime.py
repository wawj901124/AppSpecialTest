import csv,os,time

from config.config import *

class LaunchTime(object):
    def __init__(self):
        self.content = ""   #  记录执行启动命令后保存的内容
        self.startTime = 0   #  记录启动时间

    #  启动APP
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n %s/%s'% (AppPackageName,AppLaunchActivity)
        content = os.popen(cmd)
        self.content = content.readlines()
        print("启动App...")
        self.DeleyTime(2)  # 等待3秒
        print("启动命令返回数据：\n %s" % self.content)


    #冷启动-停止App
    def StopAppCold(self):
        cmd = 'adb shell am force-stop %s'% AppPackageName
        os.popen(cmd)
        print("冷启动停止App...")
        self.DeleyTime(2)  # 等待3秒

    #热启动-停止App
    def StopAppHot(self):
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)
        print("热启动停止App...")
        self.DeleyTime(2)  # 等待3秒

    #获取启动时间
    def GetLaunchTime(self):
        for line in self.content:   #  遍历启动命令后返回的文本信息
            if "TotalTime" in line:  #  如果某行包含有"ThisTime"内容
                self.startTime = line.split(":")[1]  #  获取"ThisTime"的值（启动时间）
                print("启动时间：%s" % self.startTime)
                break  #  结束循环
        # print('self.startTime:%s'% self.startTime)
        return self.startTime  #  返回启动时间

    #延时函数
    def DeleyTime(self,delaytime):
        delaytime = int(delaytime)
        time.sleep(delaytime)  # 等待delaytime秒
        print("等待%s秒..."% delaytime)


#控制类
class Controller(object):
    def __init__(self):
        self.launchtime = LaunchTime()  #  实例化
        self.counter = AppLaunchCountCold  #  启动次数
        self.alldata = [("deviceid","appversion","timestamp", "elapsedtimecold","elapsedtimehot")]  #  要保存的数据，时间戳及启动时间

    #单次测试过程
    def TestProcessOnce(self):
        self.launchtime.StopAppCold()  #  冷启动关闭
        self.launchtime.LaunchApp()   #  冷启动应用
        self.DeleyTime(5)  #  等待5秒
        elapsedtimecold = self.launchtime.GetLaunchTime()  #  获取冷启动时间
        self.launchtime.StopAppHot()  #  热启动关闭
        self.launchtime.LaunchApp()  # 热启动应用
        self.DeleyTime(5)  # 等待5秒
        elapsedtimehot = self.launchtime.GetLaunchTime()  #  获取热启动时间
        self.launchtime.StopAppCold()  #  冷启动关闭
        currenttime = self.GetCurrentTime()  #  获取当前时间
        self.alldata.append((TestDeviceID,AppVersion,currenttime,elapsedtimecold,elapsedtimehot))  #  写入数据到self.alldata

    #延时函数
    def DeleyTime(self,delaytime):
        delaytime = int(delaytime)
        time.sleep(delaytime)  # 等待5秒
        print("等待%s秒..."% delaytime)

     #多次执行测试过程
    def RunMore(self):
        while self.counter>0:  #  如果次数大于0
            self.TestProcessOnce()  #  则执行一次测试过程
            self.counter = self.counter -1 #  测试次数减一

    #获取当前存储数据的时间戳
    def GetCurrentTime(self):
        currenttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  #  获取当前时间
        return currenttime  #  返回当前时间

    # 获取当前时间的字符串
    def GetCurrentTimeString(self):
        currenttime = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 获取当前时间
        return currenttime  # 返回当前时间

    #存储数据到CSV时间
    def SaveDataToCSV(self):
        # csvfile = open("./../dataFile/%s"% AppLaunchTimeCSVFile,"wb",newline="",encoding="utf-8")  #  创建写入一个csv文件launchTime.csv,加入newline=""，解决python3写入csv出现空白
        # csvfile = open("./../dataFile/%s" % AppLaunchTimeCSVFile, "w", newline="", encoding="utf-8")
        csvfile = "./../dataFile/launchtime/%s_%s" % (self.GetCurrentTimeString(),AppLaunchTimeCSVFile)
        opencsvfile = open(csvfile, "w",newline="") #加入newline=""，解决python3写入csv出现空白行
        writercsv = csv.writer(opencsvfile)  #  写入文件
        writercsv.writerows(self.alldata)  # 写入数据,将字符串数据转换为字节，存储到CSV中
        opencsvfile.close()  #  关闭文件
        print("数据：%s" % self.alldata)
        print("数据保存路径：%s"% csvfile)

    def run(self):  #  运行
        self.RunMore()
        self.SaveDataToCSV()


if __name__ == "__main__":
    controller = Controller()
    controller.run()