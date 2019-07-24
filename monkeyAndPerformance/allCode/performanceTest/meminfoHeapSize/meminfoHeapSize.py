import csv,os,time

from config.config import *

from monkeyAndPerformance.allCode.util.gettimestr import GetTimeStr

gettimestr = GetTimeStr()  #实例化GetTimeStr


#控制类
class Controller(object):
    def __init__(self):
        self.counter = RunMeminfoCount  #  运行次数
        self.alldata = [("deviceid","appversion","timestamp", "meminfoheapsize")]  #  要保存的数据，时间戳及cup占用率

    #单次测试过程
    def TestProcessOnce(self):
        cmd = 'adb shell "dumpsys meminfo %s | grep TOTAL"' % AppPackageName   # 获取cup占用率命令
        content = os.popen(cmd)
        result = content.readlines()
        print("result:%s"% result)

        if result != []:
            for line in result:
                # meminfosize = line.split("kB")[0]
                print("line:%s" % line)
                meminfototal = line.strip()
                print("meminfototal:%s"% meminfototal)
                meminfosize = meminfototal.split("    ")
                print("meminfosize:%s"% meminfosize)
                meminfoheapsize = meminfosize[5]
                if meminfoheapsize:   #如果取到值，就终止循环
                    print("获取到内存为：%s kB"% meminfoheapsize)
                    break
            currenttime = self.GetCurrentTime()  #  获取当前时间
            self.alldata.append((TestDeviceID,AppVersion,currenttime,meminfoheapsize))  #  写入数据到self.alldata
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
            gettimestr.outPutMyLog("内存统计剩余运行次数为：%s" % self.counter)

    #获取当前存储数据的时间戳
    def GetCurrentTime(self):
        currenttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  #  获取当前时间
        return currenttime  #  返回当前时间

    # 获取当前时间的字符串
    def GetCurrentTimeString(self):
        currenttime = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 获取当前时间
        return currenttime  # 返回当前时间

    #存储数据到CSV时间
    def SaveDataToCSV(self,strtime):

        basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + "/" + "codeResult"
        nyrsfmdir = gettimestr.createNYRSFMdir(basedir,strtime)

        # logsNYRSFMdir = gettimestr.createNYRSFMdir(currentdir2, strtime)
        # csvfile = open("./../dataFile/%s"% AppLaunchTimeCSVFile,"wb",newline="",encoding="utf-8")  #  创建写入一个csv文件launchTime.csv,加入newline=""，解决python3写入csv出现空白
        # csvfile = open("./../dataFile/%s" % AppLaunchTimeCSVFile, "w", newline="", encoding="utf-8")
        csvfile = "%s/%s_%s" % (nyrsfmdir,strtime,AppMeminfoCSVFile)
        opencsvfile = open(csvfile, "w",newline="") #加入newline=""，解决python3写入csv出现空白行
        writercsv = csv.writer(opencsvfile)  #  写入文件
        writercsv.writerows(self.alldata)  # 写入数据,将字符串数据转换为字节，存储到CSV中
        opencsvfile.close()  #  关闭文件
        print("数据：%s" % self.alldata)
        print("数据保存路径：%s"% csvfile)

    def run(self,timestr):  #  运行
        self.RunMore()
        self.SaveDataToCSV(timestr)


if __name__ == "__main__":

    strtime = gettimestr.getTimeStr()
    controller = Controller()
    controller.run(strtime)
    # controller.TestProcessOnce()