# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/30 17:46'
import datetime


class GetTimeStr:
    def getTimeStr(self):
        now_time = datetime.datetime.now()
        timestr = now_time.strftime('%Y%m%d%H%M%S')
        print("当前时间：",now_time)
        print("时间串：",timestr)
        return timestr

    def getsplitstr(self,prestr):
        resultstr = prestr.split()
        amountstr = resultstr[1]
        # print("amountstr:",amountstr)
        amountstraplit = amountstr.split('.')
        # print("amountstraplit:",amountstraplit)
        amountstraplitzuhestr = ''.join(amountstraplit)
        # print("amountstraplitzuhestr:",amountstraplitzuhestr)
        return amountstraplitzuhestr



if __name__  == '__main__':
    gettimestr = GetTimeStr()
    gettimestr.getTimeStr()
