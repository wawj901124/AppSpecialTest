from threading import Thread
from multiprocessing import Process

from main.run_all_test import RunAllTest
from performanceTest.cpuOccupancy.cpuOccupancyPicture import Controller as cpuController
from performanceTest.traffic.trafficPicture import Controller as traController
from performanceTest.temperature.temperaturePicture import Controller as temController

# threads = []


if __name__ == "__main__":
    # Thread(target=RunAllTest().run()).start()
    Thread(target=cpuController().run()).start()
    Thread(target=traController().run()).start()
    Thread(target=temController().run()).start()

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



