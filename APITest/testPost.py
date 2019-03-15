import requests
import unittest
import json


class TestClass(unittest.TestCase):
    def testPost(self):

        #body数据
        keyword={
            'version':'3.3.1',
            'city':'1101000',
            'requestTime':'1472980321726',
            'deviceType':'android',
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