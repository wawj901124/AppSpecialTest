from RSA.MD5withRSA_SignVerify20180321.IIATF_sign_verify import rsa_MD5sign
message = "{}"
m = bytes(message,"utf-8")
sing = rsa_MD5sign(m,r"D:\Users\Administrator\PycharmProjects\AppSpecialTest\shuoshuo\RSA\MD5withRSA_SignVerify20180321\my_private_rsa_key.pem")
print(sing)
s = str(sing , encoding="utf-8")
print(s)
