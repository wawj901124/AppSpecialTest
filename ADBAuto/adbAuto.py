import os
import datetime

class ADBAUTO(object):
    # def __init__(self):
    #     self.devicename =

    # 使用到的函数adbOrder_rand()，adbOrder_order()，turnHropf()和DumpRead()
    def excuOrder(orderName):
        check = os.popen(orderName)
        c = check.read()
        print("执行命令：%s" % orderName)
        print("执行命令后返回的内容：%s" % c)
        return c

    def getTimeStr(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d%H%M%S')
        # print("当前时间：%s"% now_time)
        # print("时间串：%s"% timestr)
        return timestr

    def startADB(self):
        cmdorder = "adb start-server"
        self.excuOrder(cmdorder)

    def killADB(self):
        cmdorder = "adb kill-server"
        self.excuOrder(cmdorder)

    def ADBInstallApp(self,devicename,apppackagepath):
        cmdorder = "adb -s %s install %s  " % (devicename,apppackagepath)
        self.excuOrder(cmdorder)

    def ADBFuGaiInstallApp(self,devicename,apppackagepath):
        cmdorder = "adb -s %s install -r %s  " % (devicename,apppackagepath)
        self.excuOrder(cmdorder)

    def ADBUninstallApp(self,devicename,apppackagename):
        cmdorder = "adb -s %s uninstall %s  " % (devicename,apppackagename)
        self.excuOrder(cmdorder)

    def ADBPush(self,devicename,startpath,endpath):
        cmdorder = "adb -s %s push %s %s  " % (devicename,startpath,endpath)
        self.excuOrder(cmdorder)

    def ADBPull(self,devicename,startpath,endpath):
        cmdorder = "adb -s %s pull %s %s  " % (devicename,startpath,endpath)
        self.excuOrder(cmdorder)

    def ADBJMInstallApp(self,devicename,appstartpath,appendpath):
        self.ADBPush(devicename,appstartpath,appendpath)
        cmdorder = "adb -s %s shell pm install -f %s  " % (devicename,appendpath)
        self.excuOrder(cmdorder)

    def ADBStartApp(self,devicename,packagename,startactivity):
        cmdorder = "adb -s %s shell am start -W -S %s/%s " % (devicename,packagename,startactivity)
        self.excuOrder(cmdorder)

    def ADBStopApp(self,devicename,packagename):
        cmdorder = "adb -s %s shell am force-stop %s " % (devicename,packagename)
        self.excuOrder(cmdorder)

    #根据包名关键字查找APP安装包在手机中的位置(APP为手机中自带的APP)
    def ADBFKeyword(self,devicename,keyword):
        cmdorder = "adb -s %s shell pm list package -f %s " % (devicename,keyword)
        self.excuOrder(cmdorder)

    #根据包名关键字查找APP安装包在手机中的位置(APP为手机中非自带的APP)
    def ADBThressKeyword(self,devicename,keyword):
        cmdorder = "adb -s %s shell pm list package -3 %s " % (devicename,keyword)
        self.excuOrder(cmdorder)

    #根据包名关键字查找已安装的包i
    def ADBIKeyword(self,devicename,keyword):
        cmdorder = "adb -s %s shell pm list package -i %s " % (devicename,keyword)
        self.excuOrder(cmdorder)

    #adb截屏
    def ADBScreencap(self,devicename,screenname):
        cmdorder = "adb -s %s shell screencap  /data/local/tmp/%s_%s.png" % (devicename,self.getTimeStr(),screenname)
        self.excuOrder(cmdorder)

    #adb录屏
    def ADBScreenrecord(self,devicename,screenrecordname):
        cmdorder = "adb -s %s shell screenrecord  /data/local/tmp/%s_%s.mp4" % (devicename,self.getTimeStr(),screenrecordname)
        self.excuOrder(cmdorder)

    #抓取log
    def ADBLogcat(self,devicename):
        cmdorder = "adb -s %s logcat" % devicename
        self.excuOrder(cmdorder)

    #抓取log
    def ADBLogcatTwo(self,devicename):
        cmdorder = "adb -s %s shell logcat" % devicename
        self.excuOrder(cmdorder)

    #获取内存
    def ADBMeminfo(self,devicename,packagename):
        cmdorder = "adb -s %s shell dumpsys meminfo %s" % (devicename,packagename)   #获取内存中的Heapsize字段的内容，如果有突然下降，就说明可能存在内存泄漏
        self.excuOrder(cmdorder)

    #获取内存
    def ADBCpuinfo(self,devicename,packagename):
        cmdorder = "adb -s %s shell dumpsys cpuinfo |  findstr %s" % (devicename,packagename)   #Windows用findstr，liunx或者mac用grep
        self.excuOrder(cmdorder)









