# -*- coding: utf-8 -*-
import os
import time
from localRunMonkey.MonkeyTestCase import *
from localRunMonkey.MonkeyTestCaseName import *
from localRunMonkey.PackageName import *

#--------------------------------------二级调用函数-----------------------------
#执行adb命令函数
#使用到的函数adbOrder_rand()，adbOrder_order()，turnHropf()和DumpRead()
def excuOrder(orderName):
    check = os.popen(orderName)
    c = check.read()
    print(c)
    return c


#读取指定文件的指定内容（针对MonkeyTestCaseName和PackageName文件）
#使用到的函数adbOrder_rand()，adbOrder_order()，turnHropf()，DumpRead()
def openFile(FileName):
    FName = open(FileName, 'r')
    values = FName.readlines()
    FName.close()
    #print values
    #print len(values)
    Name = values[0].split(':')[1].strip('\n')
    EventFrequency = values[1].split(':')[1].strip('\n')
    timeSpace = values[2].split(':')[1].strip('\n')
    return Name,EventFrequency,timeSpace

#将指定内容写入指定文件（写入内存信息和写入monkey日志报错信息）
#使用到的函数findException（）和 DumpRead()
def writeFile(FileName, content):
    FName = open(FileName, 'a')
    FName.write(content)
    FName.close()

#查找指定文件里指定字符串的个数，并输出字符串所在行的内容
#使用到的函数adbOrder_rand()，adbOrder_order()和PhoneToCP()
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

#-----------------------------------------一级调用函数----------------------------
#运行无序monkey
#使用到的函数 主函数
def adbOrder_rand():
    #packagename = raw_input(u"请输入要运行应用的正确的包名：")
    #EventFrequency = InputInt(u"请输入monkey运行的事件总次数(正整数)：")
    #timeSpace = InputInt(u"请输入monkey运行的各个事件的间隔时间（单位：毫秒）（正整数）：")

    ConfigFile = './PackageName/PackageName.txt'
    
    packagename = openFile(ConfigFile)[0]
    EventFrequency = openFile(ConfigFile)[1]
    timeSpace = openFile(ConfigFile)[2]
    
    #ZTime = (int(EventFrequency) * int(timeSpace))%1000
    
    #print u"monkey运行时长大约为（单位：秒）：%s"% ZTime 
    while(True):
        print(u"""Options:\n\ta:Run monkey,log in the PC;\
                \n\tb:Run monkey,log in the Phone""")
        flag = input(u"Please input option:")
        if flag == 'a':
            strtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            print(u"Monkey Log Name:%s_%s_monkey.log" % (packagename,strtime))
            excuOrder("""adb shell monkey -p %s --throttle %s \
                            --ignore-crashes --monitor-native-crashes --ignore-security-exceptions \
                            --ignore-timeouts --ignore-native-crashes --pct-syskeys 10 --pct-nav \
                            20 --pct-majornav 20 --pct-touch 40 --pct-appswitch 10 -v -v -v %s > ./MonkeyLog/%s_%s_monkey.log""" % (packagename,timeSpace,EventFrequency,packagename,strtime) )
            findException("./MonkeyLog/%s_%s_monkey.log"%(packagename,strtime),"CRASH" )
            findException("./MonkeyLog/%s_%s_monkey.log"%(packagename,strtime),"Exception" )
            print(u"Monkey finished!")
            break
        elif flag == 'b':
            strtime2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            logName = '%s_%s_monkey.log'%(packagename,strtime2)
            open(r"logname.txt",'w').write(logName)
            print(u"Monkey Log Name:%s" % logName)
            excuOrder('adb shell "monkey -p %s --throttle %s --ignore-crashes --monitor-native-crashes \
                             --ignore-security-exceptions --ignore-timeouts --ignore-native-crashes --pct-syskeys\
                             10 --pct-nav 20 --pct-majornav 20 --pct-touch 40 --pct-appswitch 10 -v -v -v %s\
                             > /sdcard/%s&"'%(packagename,timeSpace,EventFrequency,logName))
            
            print(u"Monkey finished!")
            break 
        else:
            print(u"Please input the right option:a or b.")
            continue

#运行monkeyAPI脚本
#使用到的函数 主函数
def adbOrder_order():
    #Filename = str(raw_input(u"请输入要运行的monkey脚本文件名："))
    #EventFrequency = InputInt(u"请输入运行monkey脚本文件的总次数(正整数)：")
    #timeSpace = InputInt(u"请输入monkey运行的各个事件的间隔时间（单位：毫秒）（正整数）：")
    ConfigFile = './MonkeyTestCaseName/MonkeyTestCaseName.txt'
    
    Filename = openFile(ConfigFile)[0]
    EventFrequency = openFile(ConfigFile)[1]
    timeSpace = openFile(ConfigFile)[2]
    
    excuOrder("adb push ./MonkeyTestCase/%s.txt /sdcard/%s.txt" % (Filename,Filename))
    
    while(True):
        print(u"""Options:\n\ta:Run monkey,log in the PC;\
                \n\tb:Run monkey,log in the Phone""")
        flag = input(u"Please input option:")
        if flag == 'a':
            strtime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            print(u"Monkey Log Name:%s_%s_monkey.log" % (Filename,strtime))
            excuOrder("""adb shell monkey -f /sdcard/%s.txt --throttle %s --ignore-crashes --monitor-native-crashes \
                             --ignore-security-exceptions --ignore-timeouts --ignore-native-crashes \
                             -v -v -v %s > ./MonkeyLog/%s_%s_monkey.log""" % (Filename,timeSpace,EventFrequency,Filename,strtime) )
            findException("./MonkeyLog/%s_%s_monkey.log"%(Filename,strtime),"CRASH" )
            findException("./MonkeyLog/%s_%s_monkey.log"%(Filename,strtime),"Exception" )
            print(u"Monkey finished!")
            break
        elif flag == 'b':
            strtime2 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            logName = '%s_%s_monkey.log'%(Filename,strtime2)
            open(r"logname.txt",'w').write(logName)
            print(u"Monkey Log Name:%s" % logName)
            excuOrder('adb shell "monkey -f /sdcard/%s.txt --throttle %s --ignore-crashes --monitor-native-crashes \
                             --ignore-security-exceptions --ignore-timeouts --ignore-native-crashes \
                      -v -v -v %s > /sdcard/%s&"'%(Filename,timeSpace,EventFrequency,logName))
            print(u"Monkey finished!")
            break 
        else:
            print(u"Please input the right option:a or b.")
            continue

#将手机端最近一次运行的monkey日志输出到PC端
#使用到的函数 主函数
def PhoneToCP():
    logo = os.path.isfile('logname.txt')
    if(logo):
        Logname_file = open('logname.txt','r')
        Lognames = Logname_file.readlines()
        Logname_file.close()
        for Logname in Lognames:
            adbpush = os.popen("adb pull /sdcard/%s ./MonkeyLog/%s" % (Logname,Logname) )
            time.sleep(5)
            print(u"Pull %s success!" % Logname)
            findException("./MonkeyLog/%s" % Logname ,"CRASH" )
            findException("./MonkeyLog/%s" % Logname ,"Exception")
    else:
        print('logname.txt is not exist!')

#杀死monkey进程
#使用到的函数 主函数
def killMonkey():
    monkeyP = os.popen('adb shell "ps |grep monkey"')
    monkeyPI = monkeyP.read()
    if monkeyPI[10:15] == '':
        print(u"No monkey Running！")
    else:
        monkeyPID = monkeyPI[10:15]
        os.popen('adb shell "kill -9 %s"' % monkeyPID)
        time.sleep(2)
        print(u"Kill monkey success！")


#生成Hropf文件（针对内存泄漏给MAT查看使用）
#使用到的函数 主函数
def turnHropf():
    ConfigFile = './PackageName/PackageName.txt'
    packagename = openFile(ConfigFile)[0]
    strtime4 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    PreName = '%s_%s' % (packagename,strtime4)
    excuOrder("adb shell am dumpheap %s  sdcard/%s_j0.hrpof" % (packagename,PreName))
    excuOrder("adb pull sdcard/%s_j0.hrpof ./hrpof/%s_hrpof/%s_j0.hrpof" % (PreName,PreName,PreName))
    excuOrder("hprof-conv ./hrpof/%s_hrpof/%s_j0.hrpof  ./hrpof/%s_hrpof/%s_0.hprof"% (PreName,PreName,PreName,PreName))
    print(u"Build hrpof file sucess!")

#输出跑monkey时，实时所占的内存信息
#使用到的函数 主函数
def DumpRead():
    ConfigFile = './PackageName/PackageName.txt'
    packagename2 = openFile(ConfigFile)[0]
    strtime3 = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    c1 = excuOrder('adb shell dumpsys meminfo %s |findstr "Pss"' % packagename2)
    writeFile('.\Meminfo\%s_%s_meminfo.txt'%(packagename2,strtime3), c1)
    while True:
        c2 = excuOrder('adb shell dumpsys meminfo %s |findstr "TOTAL"' % packagename2)
        writeFile('.\Meminfo\%s_%s_meminfo.txt'%(packagename2,strtime3), c2)
        time.sleep(1)

#----------------------------------主执行程序------------------------------------
#主函数（主执行程序）
while(True):
    print("please run again, if no responsing!")
    device = os.popen("adb devices")
    deviceName = device.read()
    if(deviceName[-8:-2] == 'device'):
        print("device:")
        print(deviceName)
        while(True):
            print(u"""Run Options:\n\t1:Run rand monkey ;\
                    \n\t2:Run order monkey;\
                    \n\t3:Pull monkey Log from phone into PC;\
                    \n\t4:kill monkey;\
                    \n\t5:build hrpof file;\
                    \n\t6:dumpsys meminfo.""")
            Runflag = input(u"Please input run option:")
            if Runflag == '1':
                adbOrder_rand()
                break
            elif Runflag == '2':
                adbOrder_order()
                break
            elif Runflag == '3':
                PhoneToCP()
                break
            elif Runflag == '4':
                killMonkey()
                break
            elif Runflag == '5':
                turnHropf()
                break
            elif Runflag == '6':
                DumpRead()
                break
            else:
                print(u"Please input the right run option:1,2,3 or 4.")
                continue
        break
        
    else:
        print(deviceName)
        print("No device!")
        break
#暂停间隙
end = input("Please Press the Enter key to exit!")





