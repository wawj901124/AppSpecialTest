import sys

from util.gettimestr import GetTimeStr
from util.send_attach_email import SendEmail

class PrintLog:


    def printLog(self,fun):
        print('---------------------------')
        stdout_backup = sys.stdout
        gettime = GetTimeStr()
        timestr = gettime.getTimeStr()
        # define the log file that receives your log info
        logpath = "../log/%s_message.txt" % timestr
        log_file = open(logpath, "w", encoding="utf-8")
        print("Now all print info will be written to message.log")
        # redirect print output to log file
        sys.stdout = log_file

        print('----------开始打印日志-----------------\n')

        # any command line that you will execute
        fun
        print('\n----------日志打印结束-----------------')
        log_file.close()
        # restore the output to initial pattern
        sys.stdout = stdout_backup
        print("Now this will be presented on screen")
        # 发送log至邮箱
        send_e = SendEmail()
        send_e.send_main([1], [2], logpath)