# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/30 17:46'
import datetime
import os
from monkeyAndPerformance.allCode.log.my_log import MyLog


class GetTimeStr:
    def getTimeStr(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d%H%M%S')
        self.outPutMyLog("当前时间：%s"% now_time)
        self.outPutMyLog("时间串：%s"% timestr)
        # print("当前时间：",now_time)
        # print("时间串：",timestr)
        return timestr

    def getTimeStrN(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y')
        return timestr

    def getTimeStrNY(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m')
        self.outPutMyLog("当前时间：%s"% now_time)
        self.outPutMyLog("时间串年月：%s"% timestr)
        # print("当前时间：",now_time)
        # print("时间串：",timestr)
        return timestr

    def getTimeStrNYR(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d')
        return timestr

    def outPutMyLog(self,context):
        mylog = MyLog(context)
        mylog.runMyLog()


    def writeText(self,filename,var):
        with open(filename, 'w') as f:  # 打开test.txt   如果文件不存在，创建该文件。
            f.write(str(var))  # 把变量getid写入createactivityid.txt。这里var必须是str格式，如果不是，则可以转一下。
            self.outPutMyLog("将[%s]写入文件[%s]" % (var,filename))

    def readText(self,filename):
        with open(filename,"r+") as f1:
            for line in f1:
                sxhdmcinputtext =line
                self.outPutMyLog("将文件[%s]中第一行内容【%s】返回" % (filename,sxhdmcinputtext))
                return sxhdmcinputtext

    def createdir(self,filedir):
        if os.path.exists(filedir):
            self.outPutMyLog("已经存在目录：%s" % filedir)
        else:
            os.mkdir(filedir)
            self.outPutMyLog("已经创建目录：%s" % filedir)

    def createNYRSFMdir(self,basedir,timestr):
        self.outPutMyLog("基础目录为：%s"% basedir)
        n = self.getTimeStrN()
        ny = self.getTimeStrNY()
        nyr = self.getTimeStrNYR()

        logsNdir = basedir + "/" + n
        self.createdir(logsNdir)
        logsNYdir = basedir + "/" + n + "/" + ny
        self.createdir(logsNYdir)
        logsNYRdir = basedir + "/" + n + "/" + ny + "/" + nyr
        self.createdir(logsNYRdir)
        logsNYRSFMdir = basedir + "/" + n + "/" + ny + "/" + nyr + "/" + timestr
        self.createdir(logsNYRSFMdir)
        return logsNYRSFMdir



if __name__  == '__main__':
    gettimestr = GetTimeStr()
    gettimestr.writeText("1.txt",'1')
    gettimestr.readText("1.txt")
