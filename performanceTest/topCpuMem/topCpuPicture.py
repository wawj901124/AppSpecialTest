import csv,os,time

from config.config import *
from config.matpPicture import MatpPicture

class Meminfo(object):   #定义一个类，生成meminfo信息文件
    def __init__(self):
        self.second = RunMeminfoSecond  #  记录间隔获取内存的秒数

    #获取内容文件信息
    def GetMeminfo(self):  #轻易不要运行这个命令，尽量在cmd命令中使用，不要在脚本里运行，只能拔掉数据线
        cmd = 'adb shell top -d 1 > meminfo'
        content = os.popen(cmd)
        print("运行命令")



#控制类
class Controller(object):
    def __init__(self):
        #定义收集数据的数组
        self.alldata = [("deviceid","appversion","timestamp", "id","cpuoccupancy","vss","rss")]  #  要保存的数据，时间戳及流量
        self.cpuoccupancy=[]
        self.vss = []
        self.rss = []
        self.data = {}
        self.timestr = self.GetCurrentTimeString()

    #分析数据
    def AnalyzeData(self):
        content = self.ReadFile()   #获取要分析的文件
        i = 1
        for line in content:  #  遍历获取的文件
            if AppPackageName in line:   #获取对应应用的数据
                if "com.android.browser-2" not in line:
                    print("line:%s"% line)  #  打印数据
                    line = "#".join(line.split())  #空格替换成#号
                    print("line:%s" % line)  # 打印数据
                    cpuoccupancy = line.split("#")[2].strip("%")
                    vss = line.split("#")[5].strip("K")
                    rss = line.split("#")[6].strip("K")
                    currenttime = self.GetCurrentTime()  # 获取当前时间
                    #将获取到的数据存到数组中
                    self.alldata.append((TestDeviceID, AppVersion, currenttime, i,cpuoccupancy, vss, rss))  # 写入数据到self.alldata
                    self.cpuoccupancy.append(cpuoccupancy)
                    self.vss.append(vss)
                    self.rss.append(rss)
                    i = i + 1

    #延时函数
    def DeleyTime(self,delaytime):
        delaytime = int(delaytime)
        time.sleep(delaytime)  # 等待5秒
        print("等待%s秒..."% delaytime)



    #获取当前存储数据的时间戳
    def GetCurrentTime(self):
        currenttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  #  获取当前时间
        return currenttime  #  返回当前时间

    # 获取当前时间的字符串
    def GetCurrentTimeString(self):
        currenttime = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 获取当前时间
        return currenttime  # 返回当前时间

    #读取meminfo文件
    def ReadFile(self):
        mfile = open("./meminfo","r")   #打开文件meminfo
        content = mfile.readlines()   #  读取文件meminfo
        mfile.close()  #  关闭文件
        return content  #  返回获取的内容


    #存储数据到CSV时间
    def SaveDataToCSV(self):
        # csvfile = open("./../dataFile/%s"% AppLaunchTimeCSVFile,"wb",newline="",encoding="utf-8")  #  创建写入一个csv文件launchTime.csv,加入newline=""，解决python3写入csv出现空白
        # csvfile = open("./../dataFile/%s" % AppLaunchTimeCSVFile, "w", newline="", encoding="utf-8")
        csvfile = "./../dataFile/topcpumem/%s_%s" % (self.timestr,AppTopCupCSVFile)
        opencsvfile = open(csvfile, "w",newline="") #加入newline=""，解决python3写入csv出现空白行
        writercsv = csv.writer(opencsvfile)  #  写入文件
        writercsv.writerows(self.alldata)  # 写入数据,将字符串数据转换为字节，存储到CSV中
        opencsvfile.close()  #  关闭文件
        print("数据：%s" % self.alldata)
        print("数据保存路径：%s"% csvfile)
        print("内存变化为最后一次数据减去第一次数据")


    def GetData(self):
        self.data.update({'cpuoccupancy':self.cpuoccupancy})

    #存储图片
    def GetPicture(self):
        xlabel = '次数'
        ylabel = 'TopCpu占比'
        title = 'TopCpu占比统计'
        picturefile = "./../dataFile/topcpumem/%s_%s" % (self.timestr,AppTopCupPictureFile)
        matppicture = MatpPicture()
        matppicture.GetLineChart(self.data, xlabel, ylabel, title, savefilename=picturefile)
        print("数据：%s" % self.data)
        print("数据统计图片保存路径：%s"% picturefile)

    def run(self):  #  运行
        self.AnalyzeData()
        self.SaveDataToCSV()
        self.GetData()
        self.GetPicture()


if __name__ == "__main__":
    controller = Controller()
    controller.run()
