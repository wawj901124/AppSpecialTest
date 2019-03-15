# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/10/12 11:30'
import uiautomator2 as u2


class WatcherFrame():
    def __init__(self,outdevice=None,outwatchername=None,outconditiontextname=None,outclicktextname=None):
        if outdevice==None:
            self.d = u2.connect_usb('127.0.0.1:62025')
        else:
            self.d = u2.connect_usb(outdevice)

        if outwatchername ==None:
            self.watchername = 'crash'
        else:
            self.watchername = outwatchername

        if outconditiontextname == None:
            self.conditiontextname = '很抱歉，“QRindo MCH”已停止运行。'
        else:
            self.conditiontextname = outconditiontextname

        if outclicktextname ==None:
            self.clicktextname = '确定'
        else:
            self.clicktextname = outclicktextname


    def new_create_watcher(self,outwatchername=None,outconditiontextname=None,outclicktextname=None):
        if outwatchername ==None:
            watchername = self.watchername
        else:
            watchername = outwatchername

        if outconditiontextname == None:
            conditiontextname = self.conditiontextname
        else:
            conditiontextname = outconditiontextname

        if outclicktextname ==None:
            clicktextname = self.clicktextname
        else:
            clicktextname = outclicktextname

        d = self.d
        d.watcher(watchername).when(text=conditiontextname).click(text=clicktextname)
        print("已经创建[%s]监视器--------------------\n" % watchername)
        print("监视的text信息为：%s.\n" % conditiontextname)
        print('监视要点击的控件的文本信息为：%s.\n'% clicktextname)

    def new_create_watcher_findbyid(self,outwatchername=None,outconditiontextname=None,outclickid=None):
        if outwatchername ==None:
            watchername = self.watchername
        else:
            watchername = outwatchername

        if outconditiontextname == None:
            conditiontextname = 'Scan to pay me'
        else:
            conditiontextname = outconditiontextname

        if outclickid ==None:
            clickid = None
        else:
            clickid = outclickid

        d = self.d
        d.watcher(watchername).when(text=conditiontextname).click(resourceId=clickid)
        print("已经创建[%s]监视器--------------------\n" % watchername)
        print("监视的text信息为：%s.\n" % conditiontextname)
        print('监视要点击的控件的文本信息为：%s.\n'% clickid)

    def get_all_watchers(self):
        d = self.d
        all_watchers = d.watchers
        if all_watchers ==[] :
            print('没有已创建的监视器----------------\n')
        else:
            print('创建的所有监视器如下:\n', all_watchers)
        return all_watchers

    def get_all_watchers_str(self):
        all_watchers = self.get_all_watchers()
        all_watchers_str = str(all_watchers)
        return all_watchers_str

    def start_watcher(self,outwatchername=None):
        if outwatchername == None:
            watchername =self.watchername
        else:
            watchername = outwatchername

        d = self.d
        all_watchers_str = self.get_all_watchers_str()
        if watchername in all_watchers_str:
            d.watcher(watchername).triggered
            print("已经启动【%s】监视器--------------------\n" % watchername)
        else:
            print("名字为【%s】监视器不存在！\n" % watchername)


    def start_all_watchers(self):
        all_watchers = self.get_all_watchers()
        if all_watchers != []:
            all_watchers.run()
            self.show_all_start_watchers()


    def show_all_watchers_list(self):
        all_watchers_list = []
        all_watchers = self.get_all_watchers_str()
        all_qutou = all_watchers.strip('[')
        all_quwei = all_qutou.strip(']')
        all_split = all_quwei.split(',')
        all_split_len = len(all_split)
        for i in range(0,all_split_len):
            all_watchers_list.append(all_split[i].strip("'").strip().strip("'"))
        #     print("all_split_%s:"% i,all_split[i].strip("'").strip().strip("'"))
        # print("all_watchers:",all_watchers)
        # print("all_watchers_type:",type(all_watchers))
        # print("all_quwei:",all_quwei)
        # print("all_split:",all_split)
        # print("all_split_len:",all_split_len)
        # print("all_watchers_list:",all_watchers_list)
        return all_watchers_list

    def show_all_start_watchers(self):
        all_watchers_list = self.show_all_watchers_list()
        for i in range(0,len(all_watchers_list)):
            print("已经启动【%s】监视器--------------------\n" % all_watchers_list[i])


    def close_all_watchers(self):
        all_watchers = self.get_all_watchers()
        if all_watchers != []:
            all_watchers.reset()
            self.show_all_close_watchers()

    def show_all_close_watchers(self):
        all_watchers_list = self.show_all_watchers_list()
        for i in range(0,len(all_watchers_list)):
            print("已经关闭【%s】监视器--------------------\n" % all_watchers_list[i])

    def delete_all_watchers(self):
        all_watchers = self.get_all_watchers()
        if all_watchers != []:
            all_watchers.remove()
            print('已经删除所有的监视器--------------------\n')


    def delete_watcher(self,outwatchername=None):
        if outwatchername == None:
            watchername =self.watchername
        else:
            watchername = outwatchername

        d = self.d
        all_watchers_str = self.get_all_watchers_str()
        if watchername in all_watchers_str:
            d.watcher(watchername).remove()
            print('已经删除名字为【%s】的监视器--------------------\n'% watchername)
        else:
            print("名字为【%s】监视器不存在！\n" % watchername)




# if __name__ == "__main__":
#     outwatchername = 'test'
#     outconditiontextname = 'test'
#     outclicktextname = 'test'
#     wf = WatcherFrame(outwatchername=outwatchername,outconditiontextname=outconditiontextname,outclicktextname=outclicktextname)
#     wf.new_create_watcher()
#     wf.start_watcher('test')
#     # wf.start_all_watchers()
#     # wf.close_all_watchers()
#     wf.delete_watcher('test1')
#     wf.get_all_watchers()
