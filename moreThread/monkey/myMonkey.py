import time
import os

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
    deviceID = values[3].split(':')[1].strip('\n')
    return Name,EventFrequency,timeSpace,deviceID

#将指定内容写入指定文件（写入内存信息和写入monkey日志报错信息）
#使用到的函数findException（）和 DumpRead()
def writeFile(FileName, content):
    FName = open(FileName, 'a')
    FName.write(content)
    FName.close()

# 查找指定文件里指定字符串的个数，并输出字符串所在行的内容
# 使用到的函数adbOrder_rand()，adbOrder_order()和PhoneToCP()
def findException(tfile, sstr):
    try:
        lines = open(tfile, 'r').readlines()
        flen = len(lines) - 1
        acount = 0
        fileException = "%s_%s" % (tfile, sstr)
        tfileException = "%s.txt" % fileException

        writeFile(tfileException, "%s keywords:\n" % fileException)
        for i in range(flen):
            if sstr in lines[i]:
                lineException = '\t%s\n' % lines[i]

                writeFile(tfileException, lineException)
                acount += 1

        writeFile(tfileException, "%s  frequency:%s" % (fileException, acount))
        print('Please check Exception keywords in the "%s"\n' % tfileException)
    except Exception as e:
        print(e)


# 运行无序monkey
# 使用到的函数 主函数
def adbOrder_rand():
    # packagename = raw_input(u"请输入要运行应用的正确的包名：")
    # EventFrequency = InputInt(u"请输入monkey运行的事件总次数(正整数)：")
    # timeSpace = InputInt(u"请输入monkey运行的各个事件的间隔时间（单位：毫秒）（正整数）：")

    currentdir = os.path.dirname(os.path.abspath(__file__))
    print(currentdir)

    ConfigFile = '%s/PackageName/PackageName.txt' % currentdir
    print(openFile(ConfigFile))
    packagename = openFile(ConfigFile)[0]
    EventFrequency = openFile(ConfigFile)[1]
    timeSpace = openFile(ConfigFile)[2]
    deviceID = openFile(ConfigFile)[3]

    # ZTime = (int(EventFrequency) * int(timeSpace))%1000

    # print u"monkey运行时长大约为（单位：秒）：%s"% ZTime

    strtime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    print(u"Monkey Log Name:%s_%s_monkey.log" % (packagename, strtime))
    excuOrder("""adb -s %s shell monkey -p %s --throttle %s \
                    --ignore-crashes --monitor-native-crashes --ignore-security-exceptions \
                    --ignore-timeouts --ignore-native-crashes --pct-syskeys 10 --pct-nav \
                    20 --pct-majornav 20 --pct-touch 40 --pct-appswitch 10 -v -v -v %s > %s/MonkeyLog/%s_%s_monkey.log""" % (deviceID,
    packagename, timeSpace, EventFrequency,currentdir, packagename, strtime))
    findException(r"%s/MonkeyLog/%s_%s_monkey.log" % (currentdir,packagename, strtime), "CRASH")
    findException(r"%s/MonkeyLog/%s_%s_monkey.log" % (currentdir,packagename, strtime), "Exception")
    print(u"Monkey finished!")

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


# adbOrder_rand()
# killMonkey()
