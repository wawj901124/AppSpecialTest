import requests
import unittest
import ddt

dataout = (
        ("3.3.1","android"),
        ("3.3.1", "ios"),
        ("3.0.1", "android"),
        ("3.0.1", "ios"),
        ("3.0.2", "ios"),
)

@ddt.ddt    #使用ddt修饰测试类
class TestClass(unittest.TestCase):

    # @ddt.unpack
    @ddt.data("d3c1d53d0a8a378f","","!#$^","ASDFGTRGGF")
    def testGet(self,device_id):
        #header部分的配置
        headers = {
            'User-Agent':'hlj-android/3.3.1',
            'Host':'customer-api.helijia.com',
            'Connection':'Keep-Alive',
            'Accept-Encoding':'gzip'
        }

        #cookie部分的配置
        cookies = dict(
            beacon_id='MTAxLjI1MS4xOTuuMTE5LTE0QzZELTUzQkE4OTQ5QjUyNzctNjE',
            search_test='1',
            search_r='32'
        )

        #get请求的构造
        res = requests.get(
            "https://customer-api.helijia.com/app-customer/config/staticHost/get?version=3.3.1&city=110100&requestTime=1472980320170&deviceType=android&device_id="+device_id,
            headers=headers,
            cookies=cookies
        )

        print(res.text)
        print(res.status_code)
        self.assertTrue(u'http://img.cudn.static.helijia.com' in res.text)

    # @ddt.data(
    #     ("3.3.1","android"),
    #     ("3.3.1", "ios"),
    #     ("3.0.1", "android"),
    #     ("3.0.1", "ios"),
    # )   #使用data修饰测试方法
    @ddt.data(*dataout)    #分离@ddt.data（）中的数据
    @ddt.unpack   #使用unpack表示可以传入2个以上的参数
    def testPost(self,dataout):
        version, devicetype = dataout

        #body数据
        keyword={
            'version':version,
            'city':'1101000',
            'requestTime':'1472980321726',
            'deviceType':devicetype,
            'device_id':'d3c1d53d0a80321726',
            'w':''
        }

        #header部分的配置
        headers = {
            'User-Agent':'hlj-android/3.3.1',
            'Host':'customer-api.helijia.com',
            'Connection':'Keep-Alive',
            'Accept-Encoding':'gzip'
        }

        #cookie部分的配置
        cookies = dict(
            beacon_id='MTAxLjI1MS4xOTuuMTE5LTE0QzZELTUzQkE4OTQ5QjUyNzctNjE',
            search_test='1',
            search_r='32'
        )

        #get请求的构造
        res = requests.post(
            "https://customer-api.helijia.com/app-customer/transformers/1030/widgets",
            data=keyword,  # post数据
            headers=headers,
            cookies=cookies
        )

        print(res.text)
        print(res.status_code)
        self.assertTrue(u'今日上新' in res.text)

if __name__ == "__main__":
    print("1******************1")
    unittest.main()