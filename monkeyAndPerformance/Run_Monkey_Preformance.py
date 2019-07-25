from threading import Thread

from monkeyAndPerformance.allCode.monkey.myMonkey import *   #导入monkey脚本
from monkeyAndPerformance.allCode.performanceTest.getTopinfo.topinfo import GetTopInfo   #导入获取Top内容脚本
from monkeyAndPerformance.allCode.performanceTest.cpuOccupancy.cpuOccupancy import Controller as cpuController   #导入获取Cpu内容脚本
from monkeyAndPerformance.allCode.performanceTest.meminfoSize.meminfoSize import Controller as memController  #导入获取Cpu内容脚本
from monkeyAndPerformance.allCode.performanceTest.fps.fps import Controller as fpsController  #导入获取fps内容脚本
from monkeyAndPerformance.allCode.performanceTest.power.power import Controller as powController   #导入获取power内容脚本
from monkeyAndPerformance.allCode.performanceTest.temperature.temperature import Controller as temController   #导入获取temperature内容脚本
from monkeyAndPerformance.allCode.performanceTest.traffic.traffic import Controller as traController  #导入获取traffic内容脚本
from monkeyAndPerformance.allCode.util.gettimestr import GetTimeStr  #导入GetTimeStr
from monkeyAndPerformance.allCode.performanceTest.meminfoHeapSize.meminfoHeapSize import Controller as memheapController  #导入获取Cpu内容脚本


if __name__ == "__main__":
    gettimestr = GetTimeStr()  #实例化GetTimeStr
    strtime = gettimestr.getTimeStr()
    threads = []
    t0 = Thread(target=adbOrder_rand,args=(strtime,))
    threads.append(t0)
    t1 =  Thread(target=GetTopInfo().GetMeminfo,args=(strtime,))
    threads.append(t1)
    t2 =  Thread(target=cpuController().run,args=(strtime,))
    threads.append(t2)
    t3 =  Thread(target=memController().run,args=(strtime,))
    threads.append(t3)
    t4 =  Thread(target=fpsController().run,args=(strtime,))
    threads.append(t4)
    t5 =  Thread(target=powController().run,args=(strtime,))
    threads.append(t5)
    t6 =  Thread(target=temController().run,args=(strtime,))
    threads.append(t6)
    t7 =  Thread(target=traController().run,args=(strtime,))
    threads.append(t7)
    t8 =  Thread(target=memheapController().run,args=(strtime,))
    threads.append(t8)
    for t in threads:
        # t.setDaemon(True)   #设置后台执行
        t.start()   #开始线程
        # t.join()
        gettimestr.outPutMyLog("启动线程：%s" % t.ident)
        # print("退出线程")





