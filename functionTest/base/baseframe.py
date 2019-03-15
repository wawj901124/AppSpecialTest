# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/10/9 15:55'
import os
import uiautomator2 as u2
import time
from util.gettimestr import GetTimeStr   #导入获取时间串函数




class BaseFrame:
    def __init__(self,outdevice=None):
        if outdevice==None:
            # self.d = u2.connect('192.168.199.168')
            self.d = u2.connect_usb('810EBM32TZ4K')
        else:
            self.d = u2.connect_usb(outdevice)
        self.timeStr = GetTimeStr()  # 实例化

    def adbshell(self,order):
        d = self.d
        d.adb_shell(order)
        print('输入shell命令:',order,'。\n')


    def startapp(self,packagename):
        d = self.d
        d.app_start(packagename)
        print('启动包名为[%s]的应用---------'% packagename)
        # print('设备信息：', d.device_info)
        self.delaytime(3)

    def delaytime(self,dalaytime):
        dalaytime = int(dalaytime)
        time.sleep(dalaytime)
        print('等待%d秒...'% dalaytime)


    def findbyresourceId(self,resourceId):
        d = self.d
        try:
            ele = d(resourceId=resourceId)
            eletext = self.geteleinfo_text(ele)
            if eletext == "":
                print("定位到resourceId为[%s]的控件。" % resourceId)
            else:
                print("定位到text为[%s]的控件。" % eletext)
            return ele
        except Exception as e:
            self.getScreenshotError()
            self.printredword()
            print("出错原因：",e)
            self.printnormalword()
            self.delaytime(3)


    def findbyresourceId_and_input(self,resourceId,inputtext):
        ele = self.findbyresourceId(resourceId)
        self.ele_input(ele, inputtext)

    def findbyresourceId_and_click(self,resourceId,outpretoastmessage=None):
        ele = self.findbyresourceId(resourceId)
        toastmessage = self.ele_click_and_return_toastmessage(ele,outpretoastmessage)
        return toastmessage

    def findbyresourceId_and_return_enabledstatus(self,resourceId):
        ele = self.findbyresourceId(resourceId)
        eleinfo_enabled = self.geteleinfo_enabled(ele)
        return eleinfo_enabled

    def findbyresourceId_and_return_text(self,resourceId):
        ele = self.findbyresourceId(resourceId)
        eleinfo_text = self.geteleinfo_text(ele)
        return eleinfo_text

    def findbyresourceId_and_return_selectedstatus(self,resourceId):
        ele = self.findbyresourceId(resourceId)
        eleinfo_selected= self.geteleinfo_selected(ele)
        return eleinfo_selected


    def findbytext(self,text):
        d = self.d
        try:
            ele = d(text=text)
            eletext = self.geteleinfo_text(ele)
            if eletext == "":
                print("没有定位到控件。")
            else:
                print("定位到text为[%s]的控件。" % eletext)
            return ele
        except Exception as e:
            self.getScreenshotError()
            self.printredword()
            print("出错原因：",e)
            self.printnormalword()
            self.delaytime(3)

    def findbytext_and_input(self,text, inputtext):
        ele = self.findbytext(text)
        self.ele_input(ele,inputtext)

    def findbytext_and_click(self,text,outpretoastmessage=None):
        ele = self.findbytext(text)
        toastmessage = self.ele_click_and_return_toastmessage(ele,outpretoastmessage)
        return toastmessage

    def findbytext_and_return_enabledstatus(self,text):
        ele = self.findbytext(text)
        eleinfo_enabled = self.geteleinfo_enabled(ele)
        return eleinfo_enabled

    def findbytext_and_return_text(self,text):
        ele = self.findbytext(text)
        eleinfo_text = self.geteleinfo_text(ele)
        return eleinfo_text

    def findbytext_and_return_selectedstatus(self,text):
        ele = self.findbytext(text)
        eleinfo_selected= self.geteleinfo_selected(ele)
        return eleinfo_selected

    def ele_input(self,ele,inputtext):
        ele.clear_text()
        ele.send_keys(inputtext)
        print("输入:%s。" % inputtext)
        self.delaytime(1)

    def ele_click_and_return_toastmessage(self,ele,outpretoastmessage=None):
        ele.click()
        print("点击该控件。")
        if outpretoastmessage==None:
            self.delaytime(3)
            return None
        else:
            toastmessage = self.getToast()
            print("pretoastmessage:",outpretoastmessage)
            return toastmessage

    def geteleinfo_enabled(self,ele):
        value = 'enabled'
        eleinfo_enabled = self.geteleinfo_value(ele,value)
        print('该控件的enabled属性的值为：',eleinfo_enabled)
        return eleinfo_enabled

    def geteleinfo_text(self,ele):
        value = 'text'
        eleinfo_text = self.geteleinfo_value(ele,value)
        if eleinfo_text !='':
            print('该控件的text属性的值为：', eleinfo_text)
        return eleinfo_text

    def geteleinfo_selected(self,ele):
        value = 'selected'
        eleinfo_selected = self.geteleinfo_value(ele,value)
        if eleinfo_selected !='':
            print('该控件的selected属性的值为：', eleinfo_selected)
        return eleinfo_selected

    def geteleinfo_value(self,ele,value):
        eleinfo = ele.info
        # print('eleinfo:',eleinfo)
        eleinfo_value = eleinfo[value]
        return eleinfo_value


    def getToast(self):
        toastmessage = self.d.toast.get_message(5.0, default="")
        print("toastmessage:",toastmessage)
        return toastmessage

    def getdeviceinfo(self):
        deviceinfo = self.d.device_info
        print("deviceinfo:",deviceinfo)
        return deviceinfo

    def clickback(self):
        self.d.press("back")
        self.delaytime(1)

    def createwatcher(self):
        d = self.d
        d.watcher('crash').when(text='很抱歉，“QRindo MCH”已停止运行。').click(text="确定")
        d.watcher("crash").triggered
        print('d.watcher:',d.watcher)

    #打印红色文字
    def printredword(self):
        print('\033[1;31;0m')   #<!--1-高亮显示 31-前景色红色  47-背景色白色-->

    #打印默认文字
    def printnormalword(self):
        print('\033[0m')  # <!--采用终端默认设置，即取消颜色设置-->

    #打印绿色文字
    def printgreenword(self):
        print('\033[1;32;0m')  # <!--1-高亮显示 32-前景色绿色  40-背景色黑色-->

    #获取时间串
    def getTimeStr(self):
        tStr = self.timeStr.getTimeStr()
        return tStr

    #出错时，获取页面截图
    def getScreenshotError(self):
        d = self.d
        self.printredword()
        print("调用截取图片函数")
        tStr = self.getTimeStr()
        # path = "../screenshots/screenpicture_%s.png"% tStr
        path = '%s/screenshots/screenpicture_%s.png'%(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),tStr)
        self.printnormalword()
        d.screenshot(path)
        print("*****")
        print(path)
        print("*****")
        return path

    #正常，获取页面截图
    def getScreenshotNormal(self):
        d = self.d
        print("调用截取图片函数")
        tStr = self.getTimeStr()
        # path = "../screenshots/screenpicture_%s.png"% tStr
        path = '%s/screenshots/screenpicture_%s.png' % (str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), tStr)
        d.screenshot(path)
        print("*****")
        print(path)
        print("*****")
        return path


if __name__ == "__main__":
    bf = BaseFrame()
    bf.findbytext_and_click(outpretoastmessage='',text="Show QR")










