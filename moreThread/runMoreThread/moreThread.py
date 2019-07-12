from threading import Thread
from multiprocessing import Process
import gevent


from main.run_all_test import RunAllTest
from monkey.myMonkey import *
from performanceTest.cpuOccupancy.cpuOccupancyPicture import Controller as cpuController
from performanceTest.traffic.trafficPicture import Controller as traController
from performanceTest.temperature.temperaturePicture import Controller as temController



threads = []
t0 = Thread(target=adbOrder_rand)
threads.append(t0)
t1 =  Thread(target=cpuController().run)
threads.append(t1)
t2 =  Thread(target=traController().run)
threads.append(t2)
t3 =  Thread(target=temController().run)
threads.append(t3)

for t in threads:
    # t.setDaemon(True)   #设置后台执行
    t.start()   #开始线程
    # t.join()
    print("退出线程")



# processlist = []



# if __name__ == "__main__":
#     # Thread(target=RunAllTest().run()).start()
#
#     Thread(target=cpuController().run()).start()
#     Thread(target=traController().run()).start()
#     Thread(target=temController().run()).start()

# if __name__ == "__main__":
#     Process(target=RunAllTest().run()).start()
#     Process(target=cpuController().run()).start()
#     Process(target=traController().run()).start()
#     Process(target=temController().run()).start()


# class RunUiautomatorTestCase(Thread):
#     def __init__(self):
#         # 线程实例化时立即启动
#         Thread.__init__(self)
#
#         self.start()  # 线程实例化时立即启动
#
#     def run(self):
#         runat = RunAllTest()
#         runat.run()
#
#
# class RunCpuController(Thread):
#     def __init__(self):
#         # 线程实例化时立即启动
#         Thread.__init__(self)
#
#         self.start()  # 线程实例化时立即启动
#
#     def run(self):
#         runcpucontroller = cpuController()
#         runcpucontroller.run()
#
#
# class RunTraController(Thread):
#     def __init__(self):
#         # 线程实例化时立即启动
#         Thread.__init__(self)
#
#         self.start()  # 线程实例化时立即启动
#
#     def run(self):
#         runtracontroller = traController()
#         runtracontroller.run()
#
#
# class RunTemController(Thread):
#
#     def __init__(self):
#         # 线程实例化时立即启动
#         Thread.__init__(self)
#
#         self.start()  # 线程实例化时立即启动
#
#     def run(self):
#         runtemcontroller = temController()
#         runtemcontroller.run()
#
#
# class RunAll(Thread):
#     def __init__(self):
#         self.runUiautomatorTestCase = RunUiautomatorTestCase()
#         self.runCpuController = RunCpuController()
#         self.runTraController = RunTraController()
#         self.runTraController = RunTraController()
#         self.threads = []
#
#     def run(self):
#         self.threads.append(self.runUiautomatorTestCase)
#         self.threads.append(self.runCpuController)
#         self.threads.append(self.runTraController)
#         self.threads.append(self.runTraController)
#
#         for t in self.threads:
#             t.start()
#             t.join()
#
#
# if __name__ == "__main__":
#     runall = RunAll()
#     runall.run()



