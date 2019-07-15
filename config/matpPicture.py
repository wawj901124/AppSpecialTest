import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   #用来正常显示中文标签

import threading


lock = threading.Lock()  # 生成锁对象，全局唯一


class MatpPicture(object):

    #画折现图
    def GetLineChart(self,data,xlabel,ylabel,title,savefilename):
        lock.acquire()  # 获取锁。未获取到的线程会阻塞程序，直到获取到锁才会往下执行
        #遍历数据
        for key,value in data.items():
            print(len(value))
            x_data = [i for i in range(len(value))]
            print("x_data:%s" % x_data)
            y_data = value
            plt.plot(x_data ,y_data,'o-',label=key,linewidth=1,ms=1)   #x轴为x_data，y轴为y_data，标签为key,linewidth线宽为1
        plt.xlabel(xlabel)   #x轴标签
        plt.ylabel(ylabel,fontsize=10)   #y轴标签
        plt.title(title)   #统计表标题

        # plt.gcf().autofmt_xdate()  # 自动适应刻度线密度，包括x轴，y轴
        # plt.tick_params(axis='both',labelsize=8)
        # plt.axis([0, 1000, 0, 10000])
        plt.legend()   #画图
        # plt.gcf().autofmt_xdate()  # 自动适应刻度线密度，包括x轴，y轴
        # plt.show()   #显示
        plt.savefig(savefilename,dpi=300)  # 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
                                            #  指定dpi=200，图片尺寸为 1200*800
                                            # 指定dpi=300，图片尺寸为 1800*1200
        lock.release()  # 释放锁，归回锁，其他线程可以拿去用了


if __name__ == "__main__":
    x_data = range(0, 10, 1)
    y_hebei = [10, 45, 33.2, 60, 30, 20, 100, 1000, 80, 900]
    y_shanxi = [100, 4, 33.2, 6, 35, 20, 10, 100, 8, 90]
    data = {'elapsedtimecold': ['1165', '1158', '1165', '1158'], 'elapsedtimehot': ['69', '75', '69', '75']}
    xlabel='次数'
    ylabel='启动时间'
    title='冷热启动时间统计'
    savefilename="1.png"
    matppicture = MatpPicture()
    matppicture.GetLineChart(data,xlabel,ylabel,title,savefilename)
    # matppicture.GetLineChart(data =data)



