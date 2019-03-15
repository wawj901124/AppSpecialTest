import requests
import unittest


class TestClass(unittest.TestCase):
    def testGet(self):
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
            "https://customer-api.helijia.com/app-customer/config/staticHost/get?version=3.3.1&city=110100&requestTime=1472980320170&deviceType=android&device_id=d3c1d53d0a8a378f",
            headers=headers,
            cookies=cookies
        )

        print(res.text)
        print(res.status_code)
        self.assertTrue(u'http://img.cudn.static.helijia.com' in res.text)

if __name__ == "__main__":
    print("1******************1")
    unittest.main()