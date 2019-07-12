import time
import os

from monkeyAndPerformance.allCode.util.gettimestr import GetTimeStr

gettimestr = GetTimeStr()  #实例化GetTimeStr


#执行adb命令函数
#使用到的函数adbOrder_rand()，adbOrder_order()，turnHropf()和DumpRead()
def excuOrder(orderName):
    check = os.popen(orderName)
    c = check.read()
    gettimestr.outPutMyLog(c)
    return c

#读取指定文件的指定内容（针对MonkeyTestCaseName和PackageName文件）
#使用到的函数adbOrder_rand()，adbOrder_order()，turnHropf()，DumpRead()
def openFile(FileName):
    FName = open(FileName, 'r')
    values = FName.readlines()
    FName.close()
    #gettimestr.outPutMyLog values
    #gettimestr.outPutMyLog len(values)
    Name = values[0].split(':')[1].strip('\n')
    EventFrequency = values[1].split(':')[1].strip('\n')
    timeSpace = values[2].split(':')[1].strip('\n')
    deviceID = values[3].split(':')[1].strip('\n')
    seed = values[4].split(':')[1].strip('\n')
    return Name,EventFrequency,timeSpace,deviceID,seed

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
        gettimestr.outPutMyLog('Please check Exception keywords in the "%s"\n' % tfileException)
    except Exception as e:
        gettimestr.outPutMyLog(e)


# 运行无序monkey
# 使用到的函数 主函数
def adbOrder_rand(timestr):
    # packagename = raw_input(u"请输入要运行应用的正确的包名：")
    # EventFrequency = InputInt(u"请输入monkey运行的事件总次数(正整数)：")
    # timeSpace = InputInt(u"请输入monkey运行的各个事件的间隔时间（单位：毫秒）（正整数）：")

    currentdir = os.path.dirname(os.path.abspath(__file__))
    gettimestr.outPutMyLog(currentdir)

    ConfigFile = '%s/PackageName/PackageName.txt' % currentdir
    gettimestr.outPutMyLog(openFile(ConfigFile))
    packagename = openFile(ConfigFile)[0]
    EventFrequency = openFile(ConfigFile)[1]
    timeSpace = openFile(ConfigFile)[2]
    deviceID = openFile(ConfigFile)[3]
    seed = openFile(ConfigFile)[4]


    currentdir2 =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/"+"codeResult"
    logsNYRSFMdir = gettimestr.createNYRSFMdir(currentdir2,timestr)

    # strtime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    gettimestr.outPutMyLog(u"Monkey Log Name:%s_%s_monkey.log" % (packagename, timestr))
    # excuOrder("""adb -s %s shell monkey -p %s --throttle %s \
    #                 --ignore-crashes --monitor-native-crashes --ignore-security-exceptions \
    #                 --ignore-timeouts --ignore-native-crashes --pct-syskeys 10 --pct-nav \
    #                 20 --pct-majornav 20 --pct-touch 40 --pct-appswitch 10 -v -v -v %s >%s/%s_%s_monkey.log""" % (deviceID,
    # packagename, timeSpace, EventFrequency,logsNYRSFMdir,packagename, timestr))
    # cmdorder = """adb -s %s shell monkey -p %s -s %s --throttle %s -v -v -v %s >%s/%s_%s_monkey.log""" % (deviceID,
    # packagename, seed,timeSpace,EventFrequency,logsNYRSFMdir,packagename, timestr)

    cmdorder = """adb -s %s shell monkey -p %s -s %s --throttle %s \
                    --ignore-crashes --monitor-native-crashes --ignore-security-exceptions \
                    --ignore-timeouts --ignore-native-crashes --pct-syskeys 10 --pct-nav \
                    20 --pct-majornav 20 --pct-touch 40 --pct-appswitch 10 -v -v -v %s >%s/%s_%s_monkey.log""" \
               % (deviceID,packagename,seed,timeSpace, EventFrequency,logsNYRSFMdir,packagename, timestr)

    excuOrder(cmdorder)
    findException(r"%s/%s_%s_monkey.log" % (logsNYRSFMdir,packagename, timestr), "CRASH")
    findException(r"%s/%s_%s_monkey.log" % (logsNYRSFMdir,packagename, timestr), "Exception")
    gettimestr.outPutMyLog(u"Monkey finished!")

#杀死monkey进程
#使用到的函数 主函数
def killMonkey():
    monkeyP = os.popen('adb shell "ps |grep monkey"')
    monkeyPI = monkeyP.read()
    if monkeyPI[10:15] == '':
        gettimestr.outPutMyLog(u"No monkey Running！")
    else:
        monkeyPID = monkeyPI[10:15]
        os.popen('adb shell "kill -9 %s"' % monkeyPID)
        time.sleep(2)
        gettimestr.outPutMyLog(u"Kill monkey success！")


if __name__ == "__main__":
    strtime = gettimestr.getTimeStr()
    adbOrder_rand(strtime)
    # killMonkey()
