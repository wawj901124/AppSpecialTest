import csv,os,time

from config.config import *
from config.matpPicture import MatpPicture


#控制类
class Controller(object):
    def __init__(self):
        self.counter = RunCPUCount  #  运行次数
        self.alldata = [("deviceid","appversion","timestamp", "cpuoccupancy")]  #  要保存的数据，时间戳及cup占用率
        self.cpuoccupancy=[]
        self.data = {}
        self.timestr = self.GetCurrentTimeString()

    #单次测试过程
    def TestProcessOnce(self):
        cmd = 'adb shell "dumpsys cpuinfo | grep %s"' % AppPackageName   # 获取cup占用率命令
        content = os.popen(cmd)
        result = content.readlines()
        # print("result:%s"% result)
        if result != []:
            for line in result:
                cpuoccupancy = line.split("%")[0].strip(" ")
                if cpuoccupancy:   #如果取到值，就终止循环
                    print("获取到CPU占有率为百分之%s"% cpuoccupancy)
                    break
            currenttime = self.GetCurrentTime()  #  获取当前时间
            self.alldata.append((TestDeviceID,AppVersion,currenttime,cpuoccupancy))  #  写入数据到self.alldata
            self.cpuoccupancy.append(cpuoccupancy)
        else:
            print("没有找到相应APP的信息，请确定APP已经启动运行")

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
            self.DeleyTime(5)  # 间隔5秒取一次值

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
        csvfile = "./../dataFile/cpuoccupancy/%s_%s" % (self.timestr,AppCPUOccupancyCSVFile)
        opencsvfile = open(csvfile, "w",newline="") #加入newline=""，解决python3写入csv出现空白行
        writercsv = csv.writer(opencsvfile)  #  写入文件
        writercsv.writerows(self.alldata)  # 写入数据,将字符串数据转换为字节，存储到CSV中
        opencsvfile.close()  #  关闭文件
        print("数据：%s" % self.alldata)
        print("数据保存路径：%s"% csvfile)

    def GetData(self):
        self.data.update({'cpuoccupancy':self.cpuoccupancy})

    #存储图片
    def GetPicture(self):
        xlabel = '次数'
        ylabel = 'Cpu占比'
        title = 'Cpu占比统计'
        picturefile = "./../dataFile/cpuoccupancy/%s_%s" % (self.timestr,AppCPUOccupancyPictureFile)
        matppicture = MatpPicture()
        matppicture.GetLineChart(self.data, xlabel, ylabel, title, savefilename=picturefile)
        print("数据：%s" % self.data)
        print("数据统计图片保存路径：%s"% picturefile)

    def run(self):  #  运行
        self.RunMore()
        self.SaveDataToCSV()
        self.GetData()
        self.GetPicture()


if __name__ == "__main__":
    controller = Controller()
    controller.run()