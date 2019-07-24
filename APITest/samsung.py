import requests,json
# from MD5withRSA_SignVerify20180321 import  IIATF_sign_verify
# coding=utf-8
url = "http://samsung-daemon.halodigit.com/api/mkt2/act/qr"
payload ={
    "mer": "10000",
    "data": "{}",
    "sign":"MrgAh6c/UrpgFAHUSc4i6YfbJi31SpVVv0oss8iIRyZBiF1MhFVt1Ft8KAuqDB98+0gPdcY1eNwcaNtFDUdU8Nq7nmJSJXpghCbjGObAhNAzRvCduGO/g2nS+lWZ/Pbgub60ppPovX50yVuTgt4P15Xdj3k6E0Z/UqBWQWWx+zs="
}
body =json.dumps(payload)
#print(body)
r=requests.post(url=url,json=payload)
print(r.text)

r=requests.post(url=url,data=body)
print(r.text)


