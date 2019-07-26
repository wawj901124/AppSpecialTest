import requests,json
# from MD5withRSA_SignVerify20180321 import  IIATF_sign_verify
# coding=utf-8
url = "http://samsung-daemon.halodigit.com/api/mkt2/act/qr"
data = {}
payload ={
    "mer": "10000",
    "data": "%s" % data,
    "sign":"MrgAh6c/UrpgFAHUSc4i6YfbJi31SpVVv0oss8iIRyZBiF1MhFVt1Ft8KAuqDB98+0gPdcY1eNwcaNtFDUdU8Nq7nmJSJXpghCbjGObAhNAzRvCduGO/g2nS+lWZ/Pbgub60ppPovX50yVuTgt4P15Xdj3k6E0Z/UqBWQWWx+zs="
}
body =json.dumps(payload)

#请求形式一
r=requests.post(url=url,json=payload)
print(r.text)

#请求形式二
r=requests.post(url=url,data=body)
print(r.text)


# data = {"name": 123, "age": 45}
#
# print(data)
#
# data = {"name":123, "age":45}
#
# print(data)
# str1 = " w   32323d   tetrer "
# print(str)
# str2 = str.replace(" ","")
# print(str2)
#
# by = bytes(str2,encoding='utf-8')
# print("by:%s"% by)
# s = str(by)
# print(s)