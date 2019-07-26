import requests,json
from RSA.MD5withRSA_SignVerify20180321 import  IIATF_sign_verify
import string
#encoding = utf-8

# 获取sign值
def get_sign (data):
    signature = IIATF_sign_verify.rsa_MD5sign(data,r"D:\Users\Administrator\PycharmProjects\AppSpecialTest\shuoshuo\RSA\MD5withRSA_SignVerify20180321\my_private_rsa_key.pem")
    print("signature:%s" % signature)
    s = str(signature,encoding='utf-8')
    print(s)
    return s
    # return signature



#查询已上线状态的活动信息
def activity_serach():
    url = "http://samsung-daemon.halodigit.com/api/mkt2/act/qr"
    payload ={"mer": 10000,
        "data": '{}',
        "sign": '%s'% get_sign(b'{}'),
        }
        # body =json.dumps(payload)
    r=requests.post(url,json=payload)
    find=r.text
    print("查询已上线状态的活动信息返回值：%s"% find)
    return find
    # print(payload)
# activity_serach()

#加密数据处理
def bytype(data):
    x=str(data)
    end=x.replace(" ", "")    #去掉字符串中间的空格
    end1=end.replace("'", '"')   # 单元号变为双引号
    end1=bytes(end1, encoding='utf-8')
    print("end1:%s" % end1)
    return end1

#获取id 的方法
def get_value(number,value):
    find=activity_serach()
    print("find:%s" % find)
    # print(find)
    data =json.loads(find)
    print(data)
    print(type(data))
    ss = data['data']
    s1=eval(ss)
    activity_id=s1["coupons"][number]["activity_id"]
    seq=s1["coupons"][number]["seq"]
    if value== "activity_id":
        print("activity_id:%s" % activity_id)
        return activity_id

    else:
        return seq
        # print(seq)

# 上线状态的活动限制
def activity_limt():
    url ="http://samsung-daemon.halodigit.com/api/mkt2/act/limit"
    data ={"activity_id":get_value(0,"activity_id"),"seq":get_value(0,"seq")}
    x =bytype(data)
    xdata = str(x,encoding='utf-8')
    sign =get_sign(x)

    #注意：字节加密是一个字节一个字节加密，所以加密的内容要完全一模一样
    payload={
    "mer":10000,
    "data":"%s" % xdata,
    "sign":"%s" % sign
    }
    r = requests.post(url,json=payload)
    print(r.text)

activity_limt()

#领取赠券
# def coupon(inputid):
#     url="http://samsung-daemon.halodigit.com/api/mkt2/act/coupon_coll"
#     id=get_value(0,"activity_id)
#     payload={
#     "mer": 10000,
#     "data": {
#         "user_key": "bdkvlmrn7e",
#         "model": "samsung",
#         "imei": "11",
#         "mac": "11",
#         "app_pkg": "11",
#         "activity_id": "$s" %id
#     }
# }
#     ur


