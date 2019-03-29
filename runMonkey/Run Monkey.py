#!/usr/bin/env python

import wx
import os
import sys
import time

from threading import Thread


#创建一个空文件
def createFile(FileName):
    FName = open(FileName, 'w')
    FName.close()


#执行adb命令函数
#使用到的线程：RunMonkeyThread()，KillMonkeyThread()，ExportLogThread()
def excuOrder(orderName):
    c = os.system(orderName)

#读取指定文件的指定内容
#使用到的函数getDevices() ,KillMonkeyThread()
def openFile(FileName):
    if(os.path.exists(FileName)):
        FName = open(FileName, 'r')
        fileContent = FName.readlines()
        FName.close()
        return fileContent
    else:
        return []

#删除列表中指定的元素
#使用的到函数getDevices()
def delElem(delStr,delList):
    for i in delList:
        if delStr in delList:
            delList.remove(delStr)


#判断输入的内容是否为数字字符0～9
def CheckInput(inputString):
    mother = "0123456789"
    for j in inputString:
        if j not in mother:
            return None
            
    return inputString
    
            

#获取设备列表
def getDevices():
    while(True):
        
        deviceList = []
        deviceListRE = []
        deviceListLong=0
        deviceListThird = []
        deviceListThirdLong = 0
        
        print ("please run again, if no responsing!")
        orderName = "adb devices > device.txt"
        excuOrder(orderName)
        time.sleep(2)
        
        deviceList=openFile("device.txt")
        
        
        deviceListLong=len(deviceList)   #获取列表deviceList长度
        
        if(deviceListLong > 0):
            for i in range(deviceListLong):
                deviceListThird.append(deviceList[i].strip())

                
        delElem("* daemon not running. starting it now on port 5037 *",deviceListThird)
        delElem("* daemon started successfully *",deviceListThird)
        delElem("List of devices attached",deviceListThird)
        delElem("adb server is out of date.  killing...",deviceListThird)
        delElem("",deviceListThird)   #删除deviceListThird列表中的""元素

        deviceListThirdLong = len(deviceListThird)
       

        if(deviceListThirdLong > 0):
            for i in range(deviceListThirdLong):
                #将deviceList列表中的元素通过空格分隔后赋值给deviceListRE
                deviceListRE.append(deviceListThird[i].split("\t")[0])
                deviceListRE.append(deviceListThird[i].split("\t")[1].strip())

            deviceListRE=list(set(deviceListRE))    #列表去重，无法保持原有顺序

            delElem("device",deviceListRE)   #删除deviceListRE列表中"device\n"元素
            delElem("offline",deviceListRE)   #删除deviceListRE列表中"offline\n"元素
            #print(deviceListRE)
            return deviceListRE
        else:
            return ["No Devices!"]

#获取应用列表
def getPackages(deviceName):
    while(True):
        
        packageList=[]
        packageListRE=[]
        packageListLong=0
        
        #获取monkey进程
        orderName2 = 'adb -s %s shell "touch /sdcard/PackageName.txt"' % deviceName  #生成PackageName.txt文件
        excuOrder(orderName2)
        orderName3 = 'adb -s %s shell "pm list packages >/sdcard/PackageName.txt"' % deviceName  #将monkey进程信息放入PackageName.txt文件
        excuOrder(orderName3)
        time.sleep(2)
        orderName4 = 'adb -s %s pull /sdcard/PackageName.txt .' % deviceName  #将PackageName.txt文件到处到当前文件夹
        excuOrder(orderName4)
        time.sleep(2)
        packageList = openFile("PackageName.txt")

        #print(packageList)
                
        packageListLong=len(packageList)   #获取列表packageList长度
        
        for i in range(packageListLong):
            #将packageList列表中的元素通过冒号分隔后赋值给 packageListRE
            packageListRE.append(packageList[i].split(":")[0])
            packageListRE.append(packageList[i].split(":")[1].strip())

        packageListRE=list(set(packageListRE))    #列表去重，无法保持原有顺序

        delElem("package",packageListRE)   #删除packageListRE列表中package元素

                
        return packageListRE

#获取monkeyPID列表
def getMonkeyPID(deviceName):
    MonkeyPIDList = []
    #获取monkey进程
    orderName2 = 'adb -s %s shell "touch /sdcard/MonkeyPID.txt"' % deviceName  #生成MonkeyPID.txt文件
    excuOrder(orderName2)
    orderName3 = 'adb -s %s shell "ps|grep monkey >/sdcard/MonkeyPID.txt"' % deviceName  #将monkey进程信息放入MonkeyPID.txt文件
    excuOrder(orderName3)
    orderName4 = 'adb -s %s pull /sdcard/MonkeyPID.txt .' % deviceName  #将MonkeyPID.txt文件到处到当前文件夹
    excuOrder(orderName4)
    MonkeyPIDS = openFile("MonkeyPID.txt")
    if(len(MonkeyPIDS)>0):   #如果存在monkey进程，则提示跑monkey的进程
        MonkeyPIDSLong = len(MonkeyPIDS)
        for i in range(MonkeyPIDSLong):
            #将self.MonkeyPID列表中的元素通过空格分隔后赋值给self.MonkeyPIDRE列表
            MonkeyPID = MonkeyPIDS[i].split(" ")
            delElem("",MonkeyPID)   #删除self.MonkeyPID列表中所有空""项
            
            MonkeyPIDList.append(MonkeyPID[1])
            
    
    return MonkeyPIDList


    
#将指定内容写入指定文件（写入monkey日志报错信息）
#使用到的函数:findException()
def writeFile(FileName, content):
    FName = open(FileName, 'a')
    FName.write(content)
    FName.close()

#查找指定文件里指定字符串的个数，并输出字符串所在行的内容
#使用到的线程:ExportLogThread()
def findException(tfile,sstr):
    try:
        lines=open(tfile,'r').readlines()
        flen=len(lines)-1
        acount = 0
        fileException = "%s_%s" % (tfile,sstr)
        tfileException = "%s.txt" % fileException
        
        writeFile(tfileException,"%s keywords:\n" % fileException)
        for i in range(flen):
            if sstr in lines[i]:
                lineException = '\t%s\n'% lines[i]

                writeFile(tfileException,lineException)
                acount+= 1

        writeFile(tfileException,"%s  frequency:%s" % (fileException,acount))
        print('Please check Exception keywords in the "%s"\n' % tfileException)
    except Exception as e:
        print(e)

#判断变量输入内容是否为空
#使用到的线程：RunMonkeyThread()
def CheckNone(checkText,discription):
    if(checkText == None):
        print(discription)


class RunMonkeyThread(Thread):


    def __init__(self):
        #线程实例化是立即启动
        Thread.__init__(self)
        self.logNameST = logNameST
        self.MonkeyRunState = MonkeyRunStateText
        self.RunMonkeyButton = button1
        self.start()
        
    def run(self):
        
        self.RunMonkeyButton.Enable(False)
        self.RunMonkeyButton.SetLabel("Waiting...")
        self.DeviceName=DeviceDiaplay.GetStringSelection()
        self.packageName=packageText.GetValue()
        self.MonkeyTime=MTText.GetValue()
        self.MonkeyCount=MCText.GetValue()


        #获取monkey进程
        self.MonkeyPIDList= []
        self.MonkeyPIDList = getMonkeyPID(self.DeviceName)
        self.MonkeyPIDListLong = len(self.MonkeyPIDList)



        if(self.DeviceName == "" or self.DeviceName =="No Devices!"):
            self.logNameST.SetLabel("")
            self.MonkeyRunState.SetLabel("Not running: Please select the device!")
        elif(self.packageName == ""):
            self.logNameST.SetLabel("")
            self.MonkeyRunState.SetLabel("Not running: Please input the packageName!")
        elif(self.packageName not in getPackages(self.DeviceName)):
            self.logNameST.SetLabel("")
            self.MonkeyRunState.SetLabel("Not running: packageName is not exit!")
        elif(self.MonkeyTime == ""):
            self.logNameST.SetLabel("")
            self.MonkeyRunState.SetLabel("Not running: Please input the MonkeyTime!")
        elif(CheckInput(self.MonkeyTime) != self.MonkeyTime):
            self.logNameST.SetLabel("")
            self.MonkeyRunState.SetLabel("Not running: MonkeyTime must be a positive integer!")
        elif(self.MonkeyCount == ""):
            self.logNameST.SetLabel("")
            self.MonkeyRunState.SetLabel("Not running: Please input the MonkeyCount!")
        elif(CheckInput(self.MonkeyCount) != self.MonkeyCount):
            self.logNameST.SetLabel("")
            self.MonkeyRunState.SetLabel("Not running: MonkeyCount must be a positive integer!")
        elif(self.MonkeyPIDListLong == 0):
            print("Start running monkey ...\n")
            self.strTime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            self.logName = '%s_%s_monkey.log'%(self.packageName,self.strTime)
            open(r"logname.txt",'w').write(self.logName)
            self.MonkeyRunState.SetLabel("Starting monkey ...")
            self.logNameST.SetLabel("%s" % self.logName)
            self.orderName1='adb -s %s shell "monkey -p %s --throttle %s --ignore-crashes --monitor-native-crashes \
                             --ignore-security-exceptions --ignore-timeouts --ignore-native-crashes --pct-syskeys\
                             0 --pct-nav 20 --pct-majornav 20 --pct-touch 40 --pct-appswitch 10 -v -v -v %s\
                             > /sdcard/%s&" '% (self.DeviceName,self.packageName,self.MonkeyTime,self.MonkeyCount,self.logName)
            excuOrder(self.orderName1)
            time.sleep(2)
                
        else:
            for i in range(self.MonkeyPIDListLong):
                self.MonkeyRunState.SetLabel("Monkey PID: %s is running..." % self.MonkeyPIDList[i])
                time.sleep(2)

        print("****************************")
                
        self.RunMonkeyButton.Enable(True)
        self.RunMonkeyButton.SetLabel("Run Monkey")
        print("---------------------------------------")

class KillMonkeyThread(Thread):

    
    def __init__(self):
        #线程实例化时立即启动
        Thread.__init__(self)
        self.MonkeyRunState = MonkeyRunStateText
        
        self.start()
        
    def run(self):
        self.DeviceName=DeviceDiaplay.GetStringSelection()
        self.MonkeyPID=[]
        self.MonkeyPIDList = []
        
        if(self.DeviceName == "" or self.DeviceName =="No Devices!"):
            self.MonkeyRunState.SetLabel("Kill failed: Please select the device!")
        else:
            #杀死进程的两种命令
            #1. ps|grep monkey |awk '{print $2}' |xargs kill -9
            #2. PID=`ps |grep monkey|awk '{print $2}'`;kill -9 $PID;
            #self.orderName2 = 'adb shell "ps|grep monkey |awk \'{print $2}\' |xargs kill -9"'
            self.MonkeyPIDList =  getMonkeyPID(self.DeviceName)
            self.MonkeyPIDListLong = len(self.MonkeyPIDList)
            if(self.MonkeyPIDListLong > 0):
                for i in range(self.MonkeyPIDListLong):
                    self.orderName5 = 'adb -s %s shell "kill -9 %s"' % (self.DeviceName,self.MonkeyPIDList[i])  #杀死monkey进程
                    excuOrder(self.orderName5)
                    self.MonkeyRunState.SetLabel("Monkey PID: %s has been killed" % self.MonkeyPIDList[i])
                    
                self.MonkeyRunState.SetLabel("Monkey has been killed.")
            else:
                self.MonkeyRunState.SetLabel("No monkey is running!")
            

class ExportLogThread(Thread):

    
    def __init__(self):
        #线程实例化时立即启动
        Thread.__init__(self)
        self.MonkeyRunState = MonkeyRunStateText
        self.start()
        
    def run(self):
        self.DeviceName=DeviceDiaplay.GetStringSelection()
        if(self.DeviceName == "" or self.DeviceName =="No Devices!"):
            self.MonkeyRunState.SetLabel("Export failed: Please select the device!")

        else:
            self.logo = os.path.isfile('logname.txt')
            self.LogNameList = []
            self.MonkeyRunState.SetLabel("Exporting...")  
            if(self.logo):
                self.Logname_file = open('logname.txt','r')
                self.Lognames = self.Logname_file.readlines()
                self.Logname_file.close()
                for self.Logname in self.Lognames:
                    self.LogNameList = self.Logname.split("_")
        
                    self.LogFileName = self.LogNameList[0] + "_" + self.LogNameList[1]
                
                    self.orderName4 = "adb -s %s pull /sdcard/%s ./MonkeyLog_%s/%s" % (self.DeviceName,self.Logname,self.LogFileName,self.Logname)
                    excuOrder(self.orderName4)

                    time.sleep(5)
                    print (u"Pull %s success!" % self.Logname)
                    findException("./MonkeyLog_%s/%s" % (self.LogFileName,self.Logname) ,"CRASH" )
                    findException("./MonkeyLog_%s/%s" % (self.LogFileName,self.Logname) ,"Exception")
                
                    self.orderName5 = "adb -s %s pull /data/anr/traces.txt ./MonkeyLog_%s/traces.txt" % (self.DeviceName,self.LogFileName)
                    excuOrder(self.orderName5)
                
                self.MonkeyRunState.SetLabel("Export Complete.")   
            else:
                self.MonkeyRunState.SetLabel("Export failed: No monkey has been run!")

#计算事件进程
class EventProgressThread(Thread):


    def __init__(self):
        #线程实例化时立即启动
        Thread.__init__(self)
        self.RunMonkeyButton = button1
        self.MonkeyAllEventGauge = MonkeyAllEventGauge
        self.MonkeyRunEventPercent = MonkeyRunEventPercentText
        
        self.start()
        
    def run(self):
        self.Gaugecount = MonkeyPctTouchSlider.GetValue() + \
                         MonkeyPctMotionSlider.GetValue()+ \
                         MonkeyPctTrackBallSlider.GetValue()+  \
                         MonkeyPctNavSlider.GetValue()+  \
                         MonkeyPctMajorNavSlider.GetValue()+ \
                         MonkeyPctSysKeysSlider.GetValue()+  \
                         MonkeyPctAppSwitchSlider.GetValue()+  \
                         MonkeyPctAnyEventSlider.GetValue()
        
        #print("%%%%%%%%%%%%%%%",self.RunMonkeyButton.GetLabel())
        
        if(self.Gaugecount == 100 and self.RunMonkeyButton.GetLabel() =="Run Monkey") :
            self.RunMonkeyButton.Enable(True)
            MonkeyPctTouchSlider.Enable(False)
            MonkeyPctMotionSlider.Enable(False)
            MonkeyPctTrackBallSlider.Enable(False)
            MonkeyPctNavSlider.Enable(False)
            MonkeyPctMajorNavSlider.Enable(False)
            MonkeyPctSysKeysSlider.Enable(False)
            MonkeyPctAppSwitchSlider.Enable(False)
            MonkeyPctAnyEventSlider.Enable(False)

        else:
            self.RunMonkeyButton.Enable(False)
            MonkeyPctTouchSlider.Enable(True)
            MonkeyPctMotionSlider.Enable(True)
            MonkeyPctTrackBallSlider.Enable(True)
            MonkeyPctNavSlider.Enable(True)
            MonkeyPctMajorNavSlider.Enable(True)
            MonkeyPctSysKeysSlider.Enable(True)
            MonkeyPctAppSwitchSlider.Enable(True)
            MonkeyPctAnyEventSlider.Enable(True)

        self.MonkeyRunEventPercent.SetLabel("The Event Percent is %s." % self.Gaugecount)
        self.MonkeyAllEventGauge.SetValue(self.Gaugecount)


        
class InsertFrame(wx.Frame):


    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="Run monkey",
                          pos=wx.DefaultPosition,
	size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,
                            name="frame")
        
        

        panel = wx.Panel(self,-1)   #创建画板


        #设备列表
        DeviceLabel = wx.StaticText(panel, -1, "Devices List:")
        global DeviceDiaplay
        DeviceDiaplay = wx.ComboBox(panel, -1, "",
                                    size=(268,-1),choices=getDevices())
        #应用包名
        PackageLabel = wx.StaticText(panel, -1, "Package name:")
        global packageText
        packageText = wx.TextCtrl(panel, -1, "com.iapppay.pay.v4",
                                size=(268,-1))
        packageText.SetInsertionPoint(0)

        #monkey事件之间的间隔时间（ms）
        MTLabel = wx.StaticText(panel, -1, "Monkey time:")
        global MTText
        MTText = wx.TextCtrl(panel, -1, "360",
                                size=(268,-1))

        #monkey事件总次数
        MCLabel = wx.StaticText(panel, -1, "Monkey count:")
        global MCText
        MCText = wx.TextCtrl(panel, -1, "1000",
                                size=(268,-1))


        global button1
        #点击按钮运行monkey
        button1 = wx.Button(panel,label="Run Monkey")   #将按钮添加到画板
        button1.Enable(False)
        

        #杀死monkey
        button2 = wx.Button(panel,label="Kill Monkey")   #将按钮添加到画板

        #导出日志
        button3 = wx.Button(panel,label="Export Log")   #将按钮添加到画板

        #导出日志
        button4 = wx.Button(panel,label="Reset Percent")   #将按钮添加到画板

        #日志名字：
        MonkeyLogName = wx.StaticText(panel, -1, "Monkey logName:")
        global logNameST
        logNameST = wx.TextCtrl(panel,-1,"",
                                size=(268,-1))

        #状态显示：
        MonkeyRunStateName = wx.StaticText(panel, -1, "State display:")
        global MonkeyRunStateText
        MonkeyRunStateText = wx.TextCtrl(panel,-1,"",
                                size=(268,-1))
        #时间百分比状态显示：
        MonkeyEventPercentName = wx.StaticText(panel, -1, "Event percent:")
        global MonkeyRunEventPercentText
        MonkeyRunEventPercentText = wx.TextCtrl(panel,-1,"",
                                size=(268,-1))
        

        #monkey事件
        #触摸事件（点击事件）
        MonkeyPctTouchLabel = wx.StaticText(panel, -1, "Monkey PctTouch:")
        global MonkeyPctTouchSlider
        MonkeyPctTouchSlider = wx.Slider(panel,-1, 0, 0, 100, pos=(10,10),
                                         size =(268, -1),
                                         style = wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

        #monkey事件
        #动作事件（手势）
        MonkeyPctMotionLabel = wx.StaticText(panel, -1, "Monkey PctMotion:")
        global MonkeyPctMotionSlider
        MonkeyPctMotionSlider = wx.Slider(panel,-1, 0, 0, 100, pos=(10,10),
                                         size =(268, -1),
                                         style = wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

        #monkey事件
        #轨迹球事件（轨迹球）
        MonkeyPctTrackBallLabel = wx.StaticText(panel, -1, "Monkey PctTrackBall:")
        global MonkeyPctTrackBallSlider
        MonkeyPctTrackBallSlider = wx.Slider(panel,-1, 0, 0, 100, pos=(10,10),
                                         size =(268, -1),
                                         style = wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

        #monkey事件
        #基本导航事件（来自方向输入设备上的上，下，左，右事件）
        MonkeyPctNavLabel = wx.StaticText(panel, -1, "Monkey PctNav:")
        global MonkeyPctNavSlider
        MonkeyPctNavSlider = wx.Slider(panel,-1, 0, 0, 100, pos=(10,10),
                                         size =(268, -1),
                                         style = wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

        #monkey事件
        #主要导航事件（指引发图形界面的一些动作，如s-way键盘中间按键，返回按键，菜单按键等）
        MonkeyPctMajorNavLabel = wx.StaticText(panel, -1, "Monkey PctMajorNav:")
        global MonkeyPctMajorNavSlider
        MonkeyPctMajorNavSlider = wx.Slider(panel,-1, 0, 0, 100, pos=(10,10),
                                         size =(268, -1),
                                         style = wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

        #monkey事件
        #系统按键事件（系统使用的保留按键，如HOME键，
        #BACK键，拨号键（即Start Call）,挂断键（End Call）及音量键（即Volume Controls）等）
        MonkeyPctSysKeysLabel = wx.StaticText(panel, -1, "Monkey PctSysKeys:")
        global MonkeyPctSysKeysSlider
        MonkeyPctSysKeysSlider = wx.Slider(panel,-1, 0, 0, 100, pos=(10,10),
                                         size =(268, -1),
                                         style = wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

        #monkey事件
        #应用启动事件
        MonkeyPctAppSwitchLabel = wx.StaticText(panel, -1, "Monkey PctAppSwitch:")
        global MonkeyPctAppSwitchSlider
        MonkeyPctAppSwitchSlider = wx.Slider(panel,-1, 0, 0, 100, pos=(10,10),
                                         size =(268, -1),
                                         style = wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

        #monkey事件
        #其他类型事件
        MonkeyPctAnyEventLabel = wx.StaticText(panel, -1, "Monkey PctAnyEvent:")
        global MonkeyPctAnyEventSlider
        MonkeyPctAnyEventSlider = wx.Slider(panel,-1, 0, 0, 100, pos=(10,10),
                                         size =(268, -1),
                                         style = wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)

        #monkey事件
        #总事件显示
        MonkeyAllEventLabel = wx.StaticText(panel, -1, "Event Percent:")
        global MonkeyAllEventGauge
        MonkeyAllEventGauge = wx.Gauge(panel,-1, 100, pos=(10,10),
                                         size =(268, -1),
                                         style = wx.GA_HORIZONTAL)


        
        #绑定按钮的单击事件
        self.Bind(wx.EVT_BUTTON, self.runMonkey, button1)
        self.Bind(wx.EVT_BUTTON, self.killMonkey, button2)
        self.Bind(wx.EVT_BUTTON, self.exportLog, button3)
        self.Bind(wx.EVT_BUTTON, self.resetProcess, button4)
        #绑定窗口的关闭事件
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        #绑定进度条事件
        self.Bind(wx.EVT_IDLE,self.OnIdle)


        sizer = wx.FlexGridSizer(cols=1, hgap=1, vgap=1)   #设置总sizer

        sizerSon1 = wx.FlexGridSizer(cols=2, hgap=1, vgap=1)   #设置第一个子sizer
        sizerSon1.AddMany([DeviceLabel,DeviceDiaplay,PackageLabel,packageText,MTLabel,
                       MTText,MCLabel,MCText,MonkeyLogName,logNameST,MonkeyRunStateName,
                           MonkeyRunStateText,MonkeyEventPercentName,
                           MonkeyRunEventPercentText,
                           MonkeyPctTouchLabel,MonkeyPctTouchSlider,
                           MonkeyPctMotionLabel,MonkeyPctMotionSlider,
                           MonkeyPctTrackBallLabel, MonkeyPctTrackBallSlider,
                           MonkeyPctNavLabel, MonkeyPctNavSlider,
                           MonkeyPctMajorNavLabel, MonkeyPctMajorNavSlider,
                           MonkeyPctSysKeysLabel, MonkeyPctSysKeysSlider,
                           MonkeyPctAppSwitchLabel, MonkeyPctAppSwitchSlider,
                           MonkeyPctAnyEventLabel, MonkeyPctAnyEventSlider
                           ])

        sizerSon2 = wx.FlexGridSizer(cols=3, hgap=4, vgap=4)   #设置第二个字sizer
        sizerSon2.AddMany([MonkeyAllEventLabel,MonkeyAllEventGauge,button4,button1,button2,button3])


        sizer.AddMany([sizerSon1,sizerSon2])
        panel.SetSizer(sizer)


    def runMonkey(self, event):
        RunMonkeyThread()

    def killMonkey(self,event):
        KillMonkeyThread()

    def exportLog(self,event):
        ExportLogThread()

    def resetProcess(self,event):
        MonkeyPctTouchSlider.SetValue(0)
        MonkeyPctMotionSlider.SetValue(0)
        MonkeyPctTrackBallSlider.SetValue(0)
        MonkeyPctNavSlider.SetValue(0)
        MonkeyPctMajorNavSlider.SetValue(0)
        MonkeyPctSysKeysSlider.SetValue(0)
        MonkeyPctAppSwitchSlider.SetValue(0)
        MonkeyPctAnyEventSlider.SetValue(0)
        MonkeyPctTouchSlider.Enable(True)
        MonkeyPctMotionSlider.Enable(True)
        MonkeyPctTrackBallSlider.Enable(True)
        MonkeyPctNavSlider.Enable(True)
        MonkeyPctMajorNavSlider.Enable(True)
        MonkeyPctSysKeysSlider.Enable(True)
        MonkeyPctAppSwitchSlider.Enable(True)
        MonkeyPctAnyEventSlider.Enable(True)
        
        

    def OnIdle(self,event):
        #EventProgressThread()
        Gaugecount = MonkeyPctTouchSlider.GetValue() + \
                         MonkeyPctMotionSlider.GetValue()+ \
                         MonkeyPctTrackBallSlider.GetValue()+  \
                         MonkeyPctNavSlider.GetValue()+  \
                         MonkeyPctMajorNavSlider.GetValue()+ \
                         MonkeyPctSysKeysSlider.GetValue()+  \
                         MonkeyPctAppSwitchSlider.GetValue()+  \
                         MonkeyPctAnyEventSlider.GetValue()

        if (Gaugecount == 100 and button1.GetLabel() =="Run Monkey"):
            button1.Enable(True)
            MonkeyPctTouchSlider.Enable(False)
            MonkeyPctMotionSlider.Enable(False)
            MonkeyPctTrackBallSlider.Enable(False)
            MonkeyPctNavSlider.Enable(False)
            MonkeyPctMajorNavSlider.Enable(False)
            MonkeyPctSysKeysSlider.Enable(False)
            MonkeyPctAppSwitchSlider.Enable(False)
            MonkeyPctAnyEventSlider.Enable(False)
        else:
            button1.Enable(False)
            MonkeyPctTouchSlider.Enable(True)
            MonkeyPctMotionSlider.Enable(True)
            MonkeyPctTrackBallSlider.Enable(True)
            MonkeyPctNavSlider.Enable(True)
            MonkeyPctMajorNavSlider.Enable(True)
            MonkeyPctSysKeysSlider.Enable(True)
            MonkeyPctAppSwitchSlider.Enable(True)
            MonkeyPctAnyEventSlider.Enable(True)

        MonkeyRunEventPercentText.SetLabel("The Event Percent is %s." % Gaugecount)
        MonkeyAllEventGauge.SetValue(Gaugecount)


    def OnCloseMe(self, event):
        self.Close(True)
    
    def OnCloseWindow(self,event):
        self.Destroy()


class App(wx.App):


    def __init__(self,redirect=True, filename=None):
        wx.App.__init__(self,redirect,filename)


    def OnInit(self):
        print("Program Startup:")
        self.frame = InsertFrame(parent=None,id=-1)   #创建框架
        self.frame.Show()
        self.SetTopWindow(self.frame)
        #print(sys.stderr)   #输出到stderr
        return True


    def OnExit(self):
        print("Program running complete.")
        return True

        

if __name__=="__main__":
    app = App(redirect=False)   #1.文本重定向从这开始
    app.MainLoop()
    
