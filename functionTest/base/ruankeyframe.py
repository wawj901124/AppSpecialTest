import uiautomator2 as u2
import time

from project.yinniqianbaoshanghu.gloablconfig.globalconfig import GlobalConfig

class RuanKeyFrame():
    def __init__(self,outdevice=None):
        if outdevice==None:
            self.d = u2.connect_usb('810EBM32TZ4K')
        else:
            self.d = u2.connect_usb(outdevice)



    def delaytime(self, dalaytime):
        dalaytime = int(dalaytime)
        time.sleep(dalaytime)
        print('等待%d秒...' % dalaytime)

    def getdevicesHandW(self):
        screen = []
        devinfo = self.d.device_info
        dis = devinfo.get('display')
        screen_width = dis.get('width')
        screen_heigth = dis.get('height')
        screen.append(screen_width)
        screen.append(screen_heigth)
        print('deviceinfo:',devinfo)
        print('dis:',dis)
        print('screen_width:',screen_width)
        print('screen_heigth:',screen_heigth)
        print('screen:',screen)
        return screen

    def inputnum(self,numstr):
        d = self.d
        one_location_x = int('190')
        one_location_y = int('1364')
        two_location_x = int('545')
        two_location_y = int('1364')
        three_location_x = int('904')
        three_location_y = int('1364')
        four_location_x = int('190')
        four_location_y = int('1512')
        five_location_x = int('545')
        five_location_y = int('1512')
        six_location_x = int('904')
        six_location_y = int('1512')
        seven_location_x = int('190')
        seven_location_y = int('1678')
        eight_location_x = int('545')
        eight_location_y = int('1678')
        nine_location_x = int('904')
        nine_location_y = int('1678')
        zero_location_x = int('545')
        zero_location_y = int('1830')

        exportnum = []
        for i in numstr:
            if i == '1':
                d.click(one_location_x,one_location_y)
            elif i == '2':
                d.click(two_location_x,two_location_y)
            elif i == '3':
                d.click(three_location_x,three_location_y)
            elif i == '4':
                d.click(four_location_x, four_location_y)
            elif i == '5':
                d.click(five_location_x, five_location_y)
            elif i == '6':
                d.click(six_location_x, six_location_y)
            elif i == '7':
                d.click(seven_location_x, seven_location_y)
            elif i == '8':
                d.click(eight_location_x, eight_location_y)
            elif i == '9':
                d.click(nine_location_x, nine_location_y)
            elif i == '0':
                d.click(zero_location_x, zero_location_y)
            else:
                print("%s不是数字，不会输出！"% i)
                continue
            print('点击数字%s...' % i)
            self.delaytime(1)
            exportnum.append(i)
        exportnumstr = ''.join(exportnum)
        print("要输出的字符串为%s,实际只输出数字的字符串为%s" % (numstr,exportnumstr))








if __name__ == '__main__':
    ruan = RuanKeyFrame(GlobalConfig.globaldevice)
    ruan.inputnum('12345ty678')
