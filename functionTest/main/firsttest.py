# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/10/8 11:19'
import uiautomator2 as u2
import time

# d = u2.connect('172.20.157.7')
# d = u2.connect_usb('810EBM32TZ4K')
d = u2.connect_usb('127.0.0.1:52025')
# d.adb_shell('am start -n com.example.hellworldtest/.MainActivity')
# # d(text=u"hellworldtest", description=u"hellworldtest", className="android.widget.TextView").click()
# time.sleep(3)
# d(description=u"aaaaaa", className="android.view.View").click()
# time.sleep(3)
# d(description=u"Link Blog", className="android.view.View").click()
# time.sleep(3)
num = 1
while True:

    try:
        d.adb_shell("am force-stop com.ahdi.qrindo.mydwallet")
        time.sleep(3)
        d.adb_shell('am start -n com.ahdi.qrindo.mydwallet/com.ahdi.wallet.ui.activities.LoginActivity')
        # d(text=u"My DISRUPTO").click()
        time.sleep(5)
        #
        # # d(resourceId="com.ahdi.qrindo.mydwallet:id/et_login_phone_number").send_keys("81122336666")
        # # d(resourceId="com.ahdi.qrindo.mydwallet:id/et_login_pwd").send_keys("abc123456")
        d(resourceId="com.ahdi.qrindo.mydwallet:id/et_login_phone_number").send_keys("81285610491")
        d(resourceId="com.ahdi.qrindo.mydwallet:id/et_login_pwd").send_keys("123456abc")
        d(resourceId="com.ahdi.qrindo.mydwallet:id/btn_login").click()
        time.sleep(3)

        d(resourceId="com.ahdi.qrindo.mydwallet:id/tv_me").click()
        time.sleep(3)

        d(resourceId="com.ahdi.qrindo.mydwallet:id/iv_item_arrow").click()
        time.sleep(3)

        d(text=u"Withdraw").click()
        time.sleep(5)

        d(resourceId="com.ahdi.qrindo.mydwallet:id/et_receive_amount").send_keys("0")
        # d(resourceId="com.ahdi.qrindo.mydwallet:id/et_receive_amount").send_keys("1")
        d.click(123, 926)   #点1
        # d.click(352,1223)   #点0


        d(text=u"Confirm").click()
        time.sleep(5)

        # d.click(614,917)
        # time.sleep(1)
        # d.click(614,917)
        # time.sleep(1)
        # d.click(614,917)
        # time.sleep(1)
        #
        # d.click(614,1041)
        # time.sleep(1)
        # d.click(614,1041)
        # time.sleep(1)
        # d.click(614,1041)
        # time.sleep(1)

        d.click(125,916)
        time.sleep(1)
        d.click(356,916)
        time.sleep(1)
        d.click(600,916)
        time.sleep(1)
        d.click(125,916)
        time.sleep(1)
        d.click(356,916)
        time.sleep(1)
        d.click(600,916)
        time.sleep(1)


        time.sleep(10)


        d(text=u"Done").click()
        time.sleep(5)
    except:
        print("异常%s次"% num)
        num = num +1

    finally:
        True






