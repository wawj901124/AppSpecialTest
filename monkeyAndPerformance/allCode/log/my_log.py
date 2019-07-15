import  logging   #导入logging
from datetime import datetime
import os
import ctypes
import threading

lock = threading.Lock()  # 生成锁对象，全局唯一

class MyLog(object):
    def __init__(self,context):
        lock.acquire()  # 获取锁。未获取到的线程会阻塞程序，直到获取到锁才会往下执行
        self.context = context
        self.logger = self.createLogger()
        self.log_name = self.createLogFile()
        self.consle = self.openConsoleOutputLog()    #打开控制台日志输出
        self.file_handle = self.openFileOutputLog()  #打开文件日志输出

    def createLogger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)  # 设置Logging等级为DEBUG
        return logger

    def openConsoleOutputLog(self):   #打开控制台输出日志
        #控制台输出日志
        consle = logging.StreamHandler()   #建立流处理
        self.logger.addHandler(consle)   #将日志放到流处理中
        return consle

    def getTimeStrN(self):
        now_time = datetime.now()
        timestrn = now_time.strftime('%Y')
        return timestrn

    def getTimeStrNY(self):
        now_time = datetime.now()
        timestrny = now_time.strftime('%Y%m')
        return timestrny

    def getTimeStrNYR(self):
        now_time = datetime.now()
        timestrnyr = now_time.strftime('%Y%m%d')
        return timestrnyr

    def createdir(self,filedir):
        if not os.path.exists(filedir):
            os.mkdir(filedir)   #创建目录

    def createLogFile(self):   #创建日志名称
        base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件的路径的父路径保存为base_dir
        logsdir = base_dir+"/"+"logs"
        self.createdir(logsdir)
        logsNdir = base_dir+"/"+"logs"+"/"+self.getTimeStrN()
        self.createdir(logsNdir)
        logsNYdir = base_dir+"/"+"logs"+"/"+self.getTimeStrN()+"/"+self.getTimeStrNY()
        self.createdir(logsNYdir)
        logsNYRdir = base_dir+"/"+"logs"+"/"+self.getTimeStrN()+"/"+self.getTimeStrNY()+"/"+self.getTimeStrNYR()
        self.createdir(logsNYRdir)
        log_dir = os.path.join(base_dir, "logs")  # 获取log下的logs路径，保存为log_dir(log目录)
        log_dir = os.path.join(log_dir, self.getTimeStrN())  # 获取log下的logs路径，保存为log_dir(log目录)
        log_dir = os.path.join(log_dir, self.getTimeStrNY())  # 获取log下的logs路径，保存为log_dir(log目录)
        log_dir = os.path.join(log_dir, self.getTimeStrNYR())  # 获取log下的logs路径，保存为log_dir(log目录)
        log_file = datetime.now().strftime("%Y-%m-%d-%H") + ".log"  # 用时间拼接成log文件名
        log_name = log_dir + "/" + log_file  # 拼接出整体的log名字
        # print(log_name)
        return log_name

    def openFileOutputLog(self):   #打开文件输出日志
        file_handle = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 定义日志输出文件路径

        # 设置日志输出格式
        # %(asctime)s  ：日志的创建时间;%(filename)s  :文件路径；%(funcName)s  ：功能函数；%(lineno)d ：代码行数；%(levelname)s：等级名字；%(message)s：log信息
        formatter = logging.Formatter(
            'Time:%(asctime)s; FileName:%(filename)s;-> FuncName:%(funcName)s;  LineNo.:%(lineno)d; LevelNo.:%(levelno)s;--->LevelName:%(levelname)s;----->LogMessage:%(message)s ')
        file_handle.setFormatter(formatter)  # 日志输出使用设置的格式
        self.logger.addHandler(file_handle)  # 将日志输出文件加入到日志中
        return file_handle

    def printLog(self):   #打印log
        # self.logger.debug(self.context)   #打印日志
        self.logger.info(self.context)  # 打印日志

    def printErrorLog(self):   #打印log
        # self.logger.debug(self.context)   #打印日志
        self.logger.error(self.context)  # 打印日志



    def closeConsoleOutputLog(self): #关闭控制台日志输出
        self.consle.close()  # 关闭流
        self.logger.removeHandler(self.consle)  # 将日志移出流

    def closeopenFileOutputLog(self):#关闭文件日志输出
        # 关闭文件输出日志
        self.file_handle.close()  # 关闭文件
        self.logger.removeHandler(self.file_handle)  # 将日志输出文件移出Handler

    def runMyLog(self):
        self.printLog()
        self.closeConsoleOutputLog()
        self.closeopenFileOutputLog()
        lock.release()  # 释放锁，归回锁，其他线程可以拿去用了

    def runErrorLog(self):
        self.printErrorLog()
        self.closeConsoleOutputLog()
        self.closeopenFileOutputLog()
        lock.release()  # 释放锁，归回锁，其他线程可以拿去用了


if __name__ == "__main__":
    userlog = MyLog("mylogtest")
    userlog.runMyLog()
    userlog = MyLog("mylogtest")
    userlog.runErrorLog()


