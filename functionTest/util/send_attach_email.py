# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/24 10:42'
import smtplib   #导入smtplib，用来发送邮件和连接服务器
from email.mime.text import MIMEText   #导入MIMEText，用来组织邮件格式内容

from email.mime.multipart import MIMEMultipart   #添加附件用
from email.mime.application import MIMEApplication   #添加附件用

class SendEmail:
    globals() ['send_user'] = "xiangkaizheng@iapppay.com"  #构建全局变量发送者
    globals() ['email_host'] = "mail.iapppay.com"    #构建全局变量邮件服务器的email_host（smpt）
    globals() ['password'] = "iapppay002"    #构建全局变量邮件服务器的password，邮箱服务器发送者的登录密码

    def send_mail(self,user_list,sub,content,filenamepath):   #收件人，主题，内容
         user = "Mushishi" +"<"+send_user+">"   #构建发送者
         # message = MIMEText(content, _subtype='plain',_charset='utf-8')   #构建内容，格式，编码

         message = MIMEMultipart()   #Multipart就是多个部分
         message.attach(MIMEText(content, _subtype='plain', _charset='utf-8')) #构建正文内容，格式，编码
         message['Subject'] = sub   #定义邮件的主题
         message['From'] = user   #定义邮件发送者
         message['To'] = ";".join(user_list)   #以分号为分隔符将收件人分割开来

        #附件内容：
         htmlpart = MIMEApplication(open(filenamepath, 'rb').read())
         htmlpart.add_header('Content-Disposition', 'attachment', filename=filenamepath)
         message.attach(htmlpart)

         server = smtplib.SMTP()   #构建一个邮件服务器
         server.connect(email_host)   #连接到邮箱服务器
         server.login(send_user,password)   #登录邮箱
         server.sendmail(user,user_list,message.as_string())   #发送邮件，发送者user,接收者user_list,发送内容message，需要用as_string()转义成字符串发送
         server.close()   #关闭服务器

    def send_main(self,pass_list,fail_list,filenamepath):
        pass_num = float(len(pass_list))   #转换为浮点类型
        fail_num = float(len(fail_list))   #转换为浮点类型
        count_num = pass_num + fail_num
        #90%,百分比
        pass_result = "%.2f%%" %(pass_num/count_num*100)   #%.2f,浮点型数据小数点后保留两位，%%，转义百分号
        fail_result = "%.2f%%" % (fail_num/count_num*100)   #失败率
        user_list = ['xiangkaizheng@iapppay.com']
        sub = "web测试报告"
        content = "此次一共执行用例个数为%s个，成功个数为%s个，成功的列表行数有：%s，失败个数为%s个，失败的列表行数有：%s,成功率为%s,失败率为的%s." %(count_num,pass_num,pass_list,fail_num,fail_list,pass_result,fail_result)
        self.send_mail(user_list,sub,content,filenamepath)   #调用本类发送邮件函数
        # print("邮件已发送")


if __name__ == '__main__':
    sen = SendEmail()   #实例化
    sen.send_main([2,3,4],[5,6,7],'../report/01_report.html')
    print("邮件已发送")