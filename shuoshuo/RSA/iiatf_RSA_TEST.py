import iiatf_RSA as iRSA

oridata = b'123456TESTQQQQ'

priKey = '''MIICXAIBAAKBgQDUrqmJYNpui84QJR/cdSjBDsLEqlNTpi0c9WlEo6uIuz7P4FFvbobY2P7MXKE4/qNQCJJB7GMf6LAjP3RE7WdgrgwSbFbppIO2IC6YmZcuYbA2lPJLeFolTMRVterY2vNTKb18oGR9kimqJPtQ0lrgTGRfhyn8HnVyZu+TQMqP6wIDAQABAoGAbMAu8o8ywgn8wSaqhwjlYOpST0uktgYn1UHrpOxn3s+YC6VxHqCOlT1H9Gl9Cu6xxU/MsabU/ND3l95vbntSOx90YTc4NOOjezRxy38obPaaGlNQM6E6R/eTYQfePbGIVlJvauTLJpKcVtBcN36SQe2+QcGfXFqkJ4ZdKoufzkECQQD1fBAz2SavG9r08wOzGUlUViciEXmts3KIEAnl44xMIAyVn4CKqaxxbm4QhREa07DElZqhtd9MRvRdPtt7AAnLAkEA3crlEIjaW+JC9OzSMsVGd9Peh/8trmba96XkNuOuMI5qk51rs2luzfH1kld+h1lYnVN9fito4qXkny+PqwFOYQJBAPCyk6Ry4AZEVr1kZhU+zvK9gqNZ5SfW0o7swvfA1Hhz2EMA4OWVFnsmHw9dmfbm5+TpF3RFwsukqsee8U86K18CQEDSVdRZSwhjvpH6zQxNn+TRpU42BFHeecy7TVHFhVlnpjpyXdHX1KyYNN+Kds50DHQevKStZ0AmoATuT5z5CsECQFGLa3X5nhpc7E5ZboUkNtmrguN43BE2aIdr0crbu56HhFEOZQ/vWxa/Jnu8o+RcsmNlNGcpf5oFTznmiz5eTWQ='''
pubkey = '''MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDUrqmJYNpui84QJR/cdSjBDsLEqlNTpi0c9WlEo6uIuz7P4FFvbobY2P7MXKE4/qNQCJJB7GMf6LAjP3RE7WdgrgwSbFbppIO2IC6YmZcuYbA2lPJLeFolTMRVterY2vNTKb18oGR9kimqJPtQ0lrgTGRfhyn8HnVyZu+TQMqP6wIDAQAB'''

#使用字符串型公私钥加密解密
vkey_s = iRSA.get_Vkey_fromStr(priKey)
pkey_s = iRSA.get_Pkey_fromStr(pubkey)
en_data = iRSA.pkcs1_Encrypt(oridata,pkey_s)
de_data = iRSA.pkcs1_Decrypt(en_data,vkey_s)
print('1.1-------使用字符串型公私钥加密解密--------\n原始数据：%s\n加密后数据：%s\n解密后数据：%s\n'%(oridata,en_data,de_data))
# #使用pem文件型公私钥加密解密
vkey_f = iRSA.get_Vkey_fromFile('Keys\cpvkey.pem')
pkey_f = iRSA.get_Pkey_fromFile('Keys\cppkey.pem')
en_data = iRSA.pkcs1_Encrypt(oridata,pkey_f)
de_data = iRSA.pkcs1_Decrypt(en_data,vkey_f)
print('1.2-------使用pem文件型公私钥加密解密--------\n原始数据：%s\n加密后数据：%s\n解密后数据：%s\n'%(oridata,en_data,de_data))

# #RSA_MD5加签验签
signature_s = iRSA.rsa_MD5sign(oridata,vkey_s)
isverify_s = iRSA.rsa_MD5verify(oridata,pkey_s,signature_s)
print('2.1-------使用字符串型私钥:RSA_MD5加签验签--------\n签名结果：%s\n验签结果%s\n'%(signature_s,isverify_s))

signature_f = iRSA.rsa_MD5sign(oridata,vkey_f)
isverify_f = iRSA.rsa_MD5verify(oridata,pkey_f,signature_f)
print('2.2-------使用pem文件型私钥:RSA_MD5加签验签--------\n签名结果：%s\n验签结果%s\n'%(signature_f,isverify_f))

# #RSA_SHA1加签验签
signature_s = iRSA.rsa_SHA1sign(oridata,vkey_s)
isverify_s = iRSA.rsa_SHA1verify(oridata,pkey_s,signature_s)
print('3.1-------使用字符串型私钥:RSA_SHA1加签验签--------\n签名结果：%s\n验签结果%s\n'%(signature_s,isverify_s))
signature_f = iRSA.rsa_SHA1sign(oridata,vkey_f)
signature_f = iRSA.rsa_SHA1verify(oridata,pkey_f,signature_f)
print('3.2-------使用pem文件型私钥:RSA_SHA1加签验签--------\n签名结果：%s\n验签结果%s\n'%(signature_s,isverify_s))
