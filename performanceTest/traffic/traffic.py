import csv,os,time

from config.config import *


#控制类
class Controller(object):
    def __init__(self):
        self.counter = RunTrafficCount  #  定义测试的次数
        #定义收集数据的数组
        self.alldata = [("deviceid","appversion","timestamp", "traffic")]  #  要保存的数据，时间戳及流量

    #单次测试过程
    def TestProcessOnce(self):
        #执行获取进程的命令
        cmd = 'adb shell "ps | grep %s"' % AppPackageName # 获取进程
        content = os.popen(cmd)
        result = content.readlines()

        print("result:%s"% result)
        print("result.length:%s" % len(result))
        if len(result):
            #获取进程ID
            # pid = result[0].split(" ")[5]
            pid = result[0].split(" ")[3]
            print("result[0].split():%s" % result[0].split(" "))
            print("pid:%s"% pid)
            self.DeleyTime(3)

            #执行进程ID使用的流量
            cmd = 'adb shell cat /proc/%s/net/dev'% pid  # 获取流量   https://testerhome.com/topics/14310
            content = os.popen(cmd)
            traffic = content.readlines()
            print("traffic:%s"% traffic)
            #获取流量
            for line in traffic:
                print("line:%s" % line)
                if "wlan0" in line:
                    #将所有空行换成#
                    line = "#".join(line.split())
                    print("line##:%s"% line)
                    #按#号拆分,获取收到和发出的流量
                    receive = line.split("#")[1]
                    print("receive#:%s"%receive)
                    transmit = line.split("#")[9]
                    print("transmit##:%s"% transmit)

                # if "eth0" in line:
                #     #将所有空行换成#
                #     line = "#".join(line.split())
                #     #按#号拆分,获取收到和发出的流量
                #     receive = line.split("#")[1]
                #     transmit = line.split("#")[9]
                # elif "eth1" in line:
                #     # 将所有空行换成#
                #     line =  "#".join(line.split())
                #     # 按#号拆分,获取收到和发出的流量
                #     receive2 = line.split("#")[1]
                #     transmit2 = line.split("#")[9]

            #计算所有流量的之和
            # alltraffic = int(receive) + int(transmit) + int(receive2) + int(transmit2)
            alltraffic = int(receive) + int(transmit)
            #按KB计算流量值
            alltraffic = alltraffic/1024
            currenttime = self.GetCurrentTime()  #  获取当前时间
            #将获取到的数据存储到数组中
            self.alldata.append((TestDeviceID,AppVersion,currenttime,alltraffic))  #  写入数据到self.alldata
        else:
            print("没有获取到相应进程，请确定打开相应的app")

    #延时函数
    def DeleyTime(self,delaytime):
        delaytime = int(delaytime)
        time.sleep(delaytime)  # 等待5秒
        print("等待%s秒..."% delaytime)

     #多次执行测试过程
    def RunMore(self):
        #设置手机进入非充电状态
        cmd = 'adb shell dumpsys battery set status 1'
        os.popen(cmd)
        self.DeleyTime(3)
        print("循环开始时间：%s" % self.GetCurrentTime() )
        while self.counter>0:  #  如果次数大于0
            self.TestProcessOnce()  #  则执行一次测试过程
            self.counter = self.counter -1 #  测试次数减一
            self.DeleyTime(5)  # 间隔5秒取一次值
        print("循环结束时间：%s" % self.GetCurrentTime())

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
        csvfile = "./../dataFile/traffic/%s_%s" % (self.GetCurrentTimeString(),AppTrafficCSVFile)
        opencsvfile = open(csvfile, "w",newline="") #加入newline=""，解决python3写入csv出现空白行
        writercsv = csv.writer(opencsvfile)  #  写入文件
        writercsv.writerows(self.alldata)  # 写入数据,将字符串数据转换为字节，存储到CSV中
        opencsvfile.close()  #  关闭文件
        print("数据：%s" % self.alldata)
        print("数据保存路径：%s"% csvfile)
        print("流量消耗：最后一次的流量值减去第一次的流量值，就是本次操作消耗的流量值")

    def run(self):  #  运行
        self.RunMore()
        self.SaveDataToCSV()


if __name__ == "__main__":
    controller = Controller()
    controller.run()