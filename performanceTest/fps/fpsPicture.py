import csv,os,time

from config.config import *
from config.matpPicture import MatpPicture


#控制类
class Controller(object):
    def __init__(self):
        self.counter = RunFpsCount  #  定义测试的次数
        #定义收集数据的数组
        self.alldata = [("deviceid","appversion","timestamp", "fps（ms）")]  #  要保存的数据，时间戳及电量
        self.fps = []
        self.data = {}
        self.timestr = self.GetCurrentTimeString()


    #单次测试过程
    def TestProcessOnce(self):
        #执行获取fps时间的命令
        cmd = 'adb shell dumpsys SurfaceFlinger --latency  %s' % AppPackageName # 获取fps
        content = os.popen(cmd)
        result = content.readlines()
        fps = int(result[0])/1000/1000   #单位是毫秒
        print("fps:%s" % fps)

        #获取电量的Level
        # for line in result:
        #     if "level" in line:
        #         power = line.split(":")[1]
        #         print("power:%s" % power)
        currenttime = self.GetCurrentTime()  #  获取当前时间
        #将获取到的数据存储到数组中
        self.alldata.append((TestDeviceID,AppVersion,currenttime,fps))  #  写入数据到self.alldata
        self.fps.append(fps)

    #延时函数
    def DeleyTime(self,delaytime):
        delaytime = int(delaytime)
        time.sleep(delaytime)  # 等待5秒
        print("等待%s秒..."% delaytime)

     #多次执行测试过程
    def RunMore(self):
        #设置手机进入非充电状态   设置电源网址：http://www.cnblogs.com/lialong1st/p/8297928.html
        cmd = 'adb shell dumpsys battery set status 1'
        os.popen(cmd)
        self.DeleyTime(3)
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
        csvfile = "./../dataFile/fps/%s_%s" % (self.timestr,AppFpsCSVFile)
        opencsvfile = open(csvfile, "w",newline="") #加入newline=""，解决python3写入csv出现空白行
        writercsv = csv.writer(opencsvfile)  #  写入文件
        writercsv.writerows(self.alldata)  # 写入数据,将字符串数据转换为字节，存储到CSV中
        opencsvfile.close()  #  关闭文件
        print("数据：%s" % self.alldata)
        print("数据保存路径：%s"% csvfile)

    def GetData(self):
        self.data.update({'fps':self.fps})

    #存储图片
    def GetPicture(self):
        xlabel = '次数'
        ylabel = 'fps(单位：ms)'
        title = 'fps统计'
        picturefile = "./../dataFile/fps/%s_%s" % (self.timestr,AppFpsPictureFile)
        matppicture = MatpPicture()
        matppicture.GetLineChart(self.data, xlabel, ylabel, title, savefilename=picturefile)
        # print("数据：%s" % self.alldata)
        print("数据统计图片保存路径：%s"% picturefile)

    def run(self):  #  运行
        self.RunMore()
        self.SaveDataToCSV()
        self.GetData()
        self.GetPicture()


if __name__ == "__main__":
    controller = Controller()
    controller.run()