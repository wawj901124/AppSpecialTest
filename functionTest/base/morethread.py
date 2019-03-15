import datetime
import os
import threading


def execCmd(cmd):
    try:
        print("命令%s开始运行%s" % (cmd, datetime.datetime.now()))
        os.system(cmd)
        print("命令%s结束运行%s" % (cmd, datetime.datetime.now()))
    except Exception as e:
        print('%s\t 运行失败,失败原因\r\n%s' % (cmd, e))


if __name__ == '__main__':
    # 需要执行的命令列表
    cmds = ["D:/djangoworkon/uiautomator2/Scripts/python -m uiautomator2 init",
            "D:/djangoworkon/uiautomator2/Scripts/python -m weditor", ]

    # 线程池
    threads = []

    print("程序开始运行%s" % datetime.datetime.now())

    for cmd in cmds:
        th = threading.Thread(target=execCmd, args=(cmd,))
        th.start()
        threads.append(th)

    # 等待线程运行完毕
    for th in threads:
        th.join()

    print("程序结束运行%s" % datetime.datetime.now())