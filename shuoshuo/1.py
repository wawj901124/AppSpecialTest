# from RSA.MD5withRSA_SignVerify20180321.IIATF_sign_verify import rsa_MD5sign
# message = "{}"
# m = bytes(message,"utf-8")
# sing = rsa_MD5sign(m,r"D:\Users\Administrator\PycharmProjects\AppSpecialTest\shuoshuo\RSA\MD5withRSA_SignVerify20180321\my_private_rsa_key.pem")
# print(sing)
# s = str(sing , encoding="utf-8")
# print(s)
import json

# b='''
# {'record': {'weight':20,'server':'100.1.7.9','maxconn':50},'backend': 'www.oldboy.org'
# }
# '''
# c=eval(b)# eval字符串转换成字典
# print(c)
# print(type(c))

def get_value():
    find= '''{"code":"0","data":"{\"activitys\":[{\"id\":1018252,\"name\":\"使用限制0\",\"begin_time\":1563865200000,\"end_time\":1564070400000,\"limit\":1,\"total\":2},{\"id\":1018401,\"name\":\"xs_T1\",\"begin_time\":1563962400000,\"end_time\":1564502400000,\"limit\":1,\"total\":10}],\"coupons\":[{\"activity_id\":1018252,\"seq\":1576,\"begin_time\":1563864900000,\"end_time\":1564156799000,\"amount\":\"3.00\",\"consume_times\":0,\"number\":0,\"limit\":1,\"remain_times\":0},{\"activity_id\":1018401,\"seq\":1592,\"begin_time\":1563960900000,\"end_time\":1564588799000,\"amount\":\"2.00\",\"consume_times\":0,\"number\":0,\"limit\":1,\"remain_times\":0}]}","sign":"cYR0T+fzW67mdgWGwxTgeSDXettX4UF/r4HWEebT+FpGa0kUori3e4SP73tDRPLGfu9gJves6boVdqZNuiPYqxxRXUk0HPjWX0UI+kgWOlr8Cpo0t7+DPOxCttyEMzkCcBQR3g4hD9R6RX5p07j41d8EvUySwtKHlpTWdAQSrUo\u003d"}'''
    find = '{"code":"0","data":"{\"activitys\":[{\"id\":1018252,\"name\":\"使用限制0\",\"begin_time\":1563865200000,\"end_time\":1564070400000,\"limit\":1,\"total\":2},{\"id\":1018401,\"name\":\"xs_T1\",\"begin_time\":1563962400000,\"end_time\":1564502400000,\"limit\":1,\"total\":10}],\"coupons\":[{\"activity_id\":1018252,\"seq\":1576,\"begin_time\":1563864900000,\"end_time\":1564156799000,\"amount\":\"3.00\",\"consume_times\":0,\"number\":0,\"limit\":1,\"remain_times\":0},{\"activity_id\":1018401,\"seq\":1592,\"begin_time\":1563960900000,\"end_time\":1564588799000,\"amount\":\"2.00\",\"consume_times\":0,\"number\":0,\"limit\":1,\"remain_times\":0}]}","sign":"cYR0T+fzW67mdgWGwxTgeSDXettX4UF/r4HWEebT+FpGa0kUori3e4SP73tDRPLGfu9gJves6boVdqZNuiPYqxxRXUk0HPjWX0UI+kgWOlr8Cpo0t7+DPOxCttyEMzkCcBQR3g4hD9R6RX5p07j41d8EvUySwtKHlpTWdAQSrUo\u003d"}'

    print("find:%s" % find)
    print(type(find))

    # data =eval(find)
    data = {'code': '0', 'data': '{"activitys":[{"id":1018252,"name":"使用限制0","begin_time":1563865200000,"end_time":1564070400000,"limit":1,"total":2},{"id":1018401,"name":"xs_T1","begin_time":1563962400000,"end_time":1564502400000,"limit":1,"total":10}],"coupons":[{"activity_id":1018252,"seq":1576,"begin_time":1563864900000,"end_time":1564156799000,"amount":"3.00","consume_times":0,"number":0,"limit":1,"remain_times":0},{"activity_id":1018401,"seq":1592,"begin_time":1563960900000,"end_time":1564588799000,"amount":"2.00","consume_times":0,"number":0,"limit":1,"remain_times":0}]}', 'sign': 'cYR0T+fzW67mdgWGwxTgeSDXettX4UF/r4HWEebT+FpGa0kUori3e4SP73tDRPLGfu9gJves6boVdqZNuiPYqxxRXUk0HPjWX0UI+kgWOlr8Cpo0t7+DPOxCttyEMzkCcBQR3g4hD9R6RX5p07j41d8EvUySwtKHlpTWdAQSrUo='}
    print("datatype:%s" % type(data))
    print("data:%s" % data)
    code = data['code']

    print("code:%s" % code)
    print("type(code):%s" % type(code))

    dd = data['data']
    print("dd: %s" % dd)
    print("type(dd) :%s" % type(dd))
    dd = eval(dd)
    print(type(dd))
    cou = dd['coupons']

    print("cou:%s" % cou)


    # print(data["data"]["coupons"][0]["activity_id"])

get_value()
