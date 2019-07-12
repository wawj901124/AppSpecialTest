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
AppLaunchTimePictureFile = "launchTime.png"

#定义跑CPU的次数
RunCPUCount = 50
AppCPUOccupancyCSVFile = "cupOccupancy.csv"
AppCPUOccupancyPictureFile = "cupOccupancy.png"

#定义跑电量的次数
RunPowerCount = 50
AppPowerCSVFile = "power.csv"
AppPowerPictureFile = "power.png"

#定义跑电池温度的次数
RunTemperatureCount = 50
AppTemperatureCSVFile = "temperature.csv"
AppTemperaturePictureFile = "temperature.png"

#定义跑流量的次数
RunTrafficCount = 30
AppTrafficCSVFile = "traffic.csv"
AppTrafficPictureFile = "traffic.png"

#定义跑内存的次数
RunMeminfoCount = 30
RunMeminfoSecond = 1 # 定义刷新的秒数,每1秒刷新一次
AppMeminfoCSVFile = "meminfo.csv"
AppMeminfoPictureFile = "meminfo.png"


#top存储cpu和内容
AppTopCupMemCSVFile = "topcpumem.csv"
AppTopCupMemPictureFile = "topcpumem.png"
AppTopCupCSVFile = "topcpu.csv"
AppTopCupPictureFile = "topcpu.png"
AppTopMemCSVFile = "topmem.csv"
AppTopMemPictureFile = "topmem.png"

#运行fps次数
RunFpsCount = 50
AppFpsCSVFile = "fps.csv"
AppFpsPictureFile = "fps.png"



