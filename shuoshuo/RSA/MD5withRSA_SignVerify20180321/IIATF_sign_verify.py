#!/usr/bin/env python3
# coding=utf-8
# Author: Luosu20180321

# ===================================================================
# 说明：20180321确认Java程序使用security-0.0.1-SNAPSHOT.jar进
# 行MD5withRSA签名数据与Python版签名结果signature是一致的,且相互
# 之间可以相互验签成功
# Java版 pkcs8 产生私钥，MD5获取被签名数据特征值，RSA秘钥长度1024
# 同目录的2个秘钥文件，是大宝坑给的签名示例代码中的密钥对
# ===================================================================
from binascii import unhexlify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
import base64
from Crypto.Hash import SHA1,MD5
from Crypto.Signature import pkcs1_15

def create_rsa_key(password="123456"):
    """
    创建RSA密钥,步骤说明：
    1、从 Crypto.PublicKey 包中导入 RSA，创建一个密码(此密码不是RSA秘钥对)
    2、生成 1024/2048 位的 RSA 密钥对(存储在私钥文件和公钥文件)
    3、调用 RSA 密钥实例的 exportKey 方法(传入"密码"、"使用的 PKCS 标准"、"加密方案"这三个参数)得到私钥。
    4、将私钥写入磁盘的文件。
    5、使用方法链调用 publickey 和 exportKey 方法生成公钥，写入磁盘上的文件。
    """
    key = RSA.generate(1024)
    encrypted_key = key.exportKey(passphrase=password, pkcs=8,protection="scryptAndAES128-CBC")
    # encrypted_key = key.exportKey(pkcs=1)
    print('encrypted_key:',encrypted_key)
    with open("my_private_rsa_key.pem", "wb") as f:
        f.write(encrypted_key)
    with open("my_rsa_public.pem", "wb") as f:
        f.write(key.publickey().exportKey())

def get_private_key(filepath,password="123456"):
    return RSA.import_key(open(filepath).read(),passphrase=password)

def get_public_key(filepath):
    return RSA.importKey(open(filepath).read())

def rsa_MD5sign(message,privatekey_filepath,password="123456"):
    #读取私钥信息用于加签
    private_key = get_private_key(privatekey_filepath)
    hash_obj = MD5.new(message)
    # print(pkcs1_15.new(private_key).can_sign())  #check wheather object of pkcs1_15 can be signed
    #base64编码打印可视化
    signature = base64.b64encode(pkcs1_15.new(private_key).sign(hash_obj))
    return signature

def rsa_MD5signverify(message,signature,publickey_filepath):
    #读取公钥信息用于验签
    public_key = get_public_key(publickey_filepath)
    #message做“哈希”处理，RSA签名这么要求的
    hash_obj = MD5.new(message)
    try:
        #因为签名被base64编码，所以这里先解码，再验签
        pkcs1_15.new(public_key).verify(hash_obj,base64.b64decode(signature))
        print('The signature is valid.')
        return True
    except (ValueError,TypeError):
        print('The signature is invalid.')


if __name__ == '__main__':
    private_key = """-----BEGIN ENCRYPTED PRIVATE KEY-----
MIICXAIBAAKBgQDUrqmJYNpui84QJR/cdSjBDsLEqlNTpi0c9WlEo6uIuz7P4FFvbobY2P7MXKE4/qNQCJJB7GMf6LAjP3RE7WdgrgwSbFbppIO2IC6YmZcuYbA2lPJLeFolTMRVterY2vNTKb18oGR9kimqJPtQ0lrgTGRfhyn8HnVyZu+TQMqP6wIDAQABAoGAbMAu8o8ywgn8wSaqhwjlYOpST0uktgYn1UHrpOxn3s+YC6VxHqCOlT1H9Gl9Cu6xxU/MsabU/ND3l95vbntSOx90YTc4NOOjezRxy38obPaaGlNQM6E6R/eTYQfePbGIVlJvauTLJpKcVtBcN36SQe2+QcGfXFqkJ4ZdKoufzkECQQD1fBAz2SavG9r08wOzGUlUViciEXmts3KIEAnl44xMIAyVn4CKqaxxbm4QhREa07DElZqhtd9MRvRdPtt7AAnLAkEA3crlEIjaW+JC9OzSMsVGd9Peh/8trmba96XkNuOuMI5qk51rs2luzfH1kld+h1lYnVN9fito4qXkny+PqwFOYQJBAPCyk6Ry4AZEVr1kZhU+zvK9gqNZ5SfW0o7swvfA1Hhz2EMA4OWVFnsmHw9dmfbm5+TpF3RFwsukqsee8U86K18CQEDSVdRZSwhjvpH6zQxNn+TRpU42BFHeecy7TVHFhVlnpjpyXdHX1KyYNN+Kds50DHQevKStZ0AmoATuT5z5CsECQFGLa3X5nhpc7E5ZboUkNtmrguN43BE2aIdr0crbu56HhFEOZQ/vWxa/Jnu8o+RcsmNlNGcpf5oFTznmiz5eTWQ=
-----END ENCRYPTED PRIVATE KEY-----""" 
    public_key =  """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDUrqmJYNpui84QJR/cdSjBDsLEqlNTpi0c9WlEo6uIuz7P4FFvbobY2P7MXKE4/qNQCJJB7GMf6LAjP3RE7WdgrgwSbFbppIO2IC6YmZcuYbA2lPJLeFolTMRVterY2vNTKb18oGR9kimqJPtQ0lrgTGRfhyn8HnVyZu+TQMqP6wIDAQAB
-----END PUBLIC KEY-----"""
    message = b'123456'
    print(type(message))
    privatekey_filepath = "my_private_rsa_key.pem"
    publickey_filepath = "my_rsa_public.pem"

    # create_rsa_key()
    signature = rsa_MD5sign(message,privatekey_filepath)
    print('signature:',signature)
    # signature是java程序使用相同公钥对字符串"123456"的MD5withRSA签名结果
    # signature='n6iuYyfl4vVvOWSVCAlLpK/1ZWscRIYn2Gaql6DcozkXgtfn2r3CnWQPMB4gt+GW2HT7G7ML+B0wMpRPMWwo9VHh5EJzghTiMkRqgjoOAfDNC0gg7fvZVW4XwUv9NdRDh9ij2DO4PmwvQG6JV7mMp1+y6ox89r0MA2w9O5oKaeY='
    print(rsa_MD5signverify(message,signature,publickey_filepath))
