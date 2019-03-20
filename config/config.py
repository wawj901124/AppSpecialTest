import time

TestDeviceID = "810EBM32TZ4K"
AppVersion = "V1.0.0"

#BCAsdk配置
# AppPackageName = 'com.ahdi.pay.demo'
# AppLaunchActivity = '.DemoMainActivity'

#浏览器app配置
# AppPackageName = 'com.android.browser'
# AppLaunchActivity = '.BrowserActivity'

#Qrindo钱包配置
AppPackageName = 'com.ahdi.qrindo.wallet'
AppLaunchActivity = 'com.ahdi.wallet.ui.activities.SplashActivity'
# AppLaunchActivity = 'com.ahdi.wallet.ui.activities.LoginActivity'

AppLaunchCountCold = 2
AppLaunchTimeCSVFile = "launchTime.csv"

#定义跑CPU的次数
RunCPUCount = 50
AppCPUOccupancyCSVFile = "cupOccupancy.csv"

#定义跑电量的次数
RunPowerCount = 50
AppPowerCSVFile = "power.csv"

#定义跑流量的次数
RunTrafficCount = 50
AppTrafficCSVFile = "traffic.csv"

#定义跑内存的次数
RunMeminfoCount = 2
RunMeminfoSecond = 1 # 定义刷新的秒数,每1秒刷新一次
AppMeminfoCSVFile = "meminfo.csv"


#top存储cpu和内容
AppTopCupMemCSVFile = "topcpumem.csv"



