import csv,os,time

from config.config import *
from monkeyAndPerformance.allCode.util.gettimestr import GetTimeStr

gettimestr = GetTimeStr()  #实例化GetTimeStr

class GetTopInfo(object):   #定义一个类，生成meminfo信息文件
    def __init__(self):
        self.second = RunMeminfoSecond  #  记录间隔获取内存的秒数

    #获取内容文件信息
    def GetMeminfo(self,timestr):  #轻易不要运行这个命令，尽量在cmd命令中使用，不要在脚本里运行，只能拔掉数据线
        basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + "/" + "codeResult"
        nyrsfmdir = gettimestr.createNYRSFMdir(basedir,timestr)
        cmd = 'adb shell top -d 1 > %s/%s_topinfo' % (nyrsfmdir,timestr)
        content = os.popen(cmd)
        print("运行命令")


if __name__ == "__main__":
    timestr = gettimestr.getTimeStr()
    topinfo = GetTopInfo()
    topinfo.GetMeminfo(timestr)
