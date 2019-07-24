#!/usr/bin/env python3
# coding=utf-8
# Author: Luosu
# date: 201803
"""
基础知识：
https://blog.csdn.net/yowasa/article/details/72825866
http://blog.csdn.net/levilly/article/details/51786595
"""

from binascii import unhexlify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
import base64
from Crypto.Hash import SHA1,MD5
from Crypto.Signature import pkcs1_15

 
def create_Rsa_key(password=None):
    """
    创建RSA密钥,步骤说明：
    1、从 Crypto.PublicKey 包中导入 RSA，创建一个密码(此密码不是RSA秘钥对)
    2、生成 1024/2048 位的 RSA 密钥对(存储在私钥文件和公钥文件)
    3、调用 RSA 密钥实例的 exportKey 方法(传入"密码"、"使用的 PKCS 标准"、"加密方案"这三个参数)得到私钥。
    4、将私钥写入磁盘的文件。
    5、使用方法链调用 publickey 和 exportKey 方法生成公钥，写入磁盘上的文件。
    """
    key = RSA.generate(1024)
    # pkcs8加密算法生成的秘钥，北京业务平台无法解密，pkcs1加密算法生成的秘钥可以。
    # encrypted_key = key.exportKey(passphrase=password, pkcs=8,protection="scryptAndAES128-CBC")  
    encrypted_key = key.exportKey(pkcs=1)
    # print('encrypted_key:',encrypted_key)
    with open("Keys\my_private_rsa_key.pem", "wb") as f:
        f.write(encrypted_key)
    with open("Keys\my_rsa_public.pem", "wb") as f:
        f.write(key.publickey().exportKey())

def anyStrKey2pemKey_pkcs1(strKey):
    # print(len(strKey))
    if len(strKey) < 210 or len(strKey) > 826:
        print('strKey is not pkcs1_15 KEY')
        exit()
    elif len(strKey) > 600:
        return '-----BEGIN RSA PRIVATE KEY-----\n'+strKey+'\n-----END RSA PRIVATE KEY-----'
    else:
        return '-----BEGIN PUBLIC KEY-----\n'+strKey+'\n-----END PUBLIC KEY-----'

#通过字符串型私钥获取RSA私钥对象
def get_Vkey_fromStr(str_vkey,password=None):
    try:
        return RSA.import_key(anyStrKey2pemKey_pkcs1(str_vkey),passphrase=password)
    except Exception as e:
        raise e
#通过私钥文件获取RSA私钥对象
def get_Vkey_fromFile(filepath,password=None):
    try:
        return RSA.import_key(open(filepath).read(),passphrase=password)
    except FileNotFoundError:
        print("No such file or directory: \'%s\',Stop procces!"%(filepath))
        exit()
#通过字符串型公钥获取RSA公钥对象
def get_Pkey_fromStr(str_pkey):
    try:
        return RSA.import_key(anyStrKey2pemKey_pkcs1(str_pkey))
    except Exception as e:
        raise e
#通过公钥文件获取RSA公钥对象
def get_Pkey_fromFile(filepath):
    try:
        return RSA.import_key(open(filepath).read())
    except FileNotFoundError:
        print("No such file or directory: \'%s\',Stop procces!"%(filepath))
        exit()

#PKCS1标准的加密程序，参数padding目前无实际意义
def pkcs1_Encrypt(oridata,publickey,padding="RSA/ECB/PKCS1Padding"):
    #保证传入原始数据为转bytes[]型
    if type(oridata) != bytes:
        print("%s is a String, auto convert to bytes!"%(oridata))
        oridata = oridata.encode()
    # 加载公钥用于加密
    cipher_rsa = PKCS1_v1_5.new(publickey)
    # print(cipher_rsa.can_encrypt())
    #使用base64编码保存数据方便查看，同样解密需要base64解码
    en_data = base64.b64encode(cipher_rsa.encrypt(oridata))
    # print("加密数据信息：",type(en_data),'\n',len(en_data),'\n',en_data)
    return en_data

#PKCS1标准的解密程序
def pkcs1_Decrypt(en_data,privatekey,password=None):
    # 加载私钥用于解密
    # private_key = get_private_key(privatekey,password)
    cipher_rsa = PKCS1_v1_5.new(privatekey)
    de_data = cipher_rsa.decrypt(base64.b64decode(en_data), None)
    # print(de_data)
    return de_data

#SHA1加密算法的rsa签名函数，与rsa_MD5sign()基本没啥区别
def rsa_SHA1sign(oridata,privatekey,password=None):
    #读取私钥信息用于加签
    #oridata做“哈希”处理，RSA签名这么要求的
    hash_obj = SHA1.new(oridata)
    # print(pkcs1_15.new(private_key).can_sign())  #check wheather object of pkcs1_15 can be signed
    #base64编码打印可视化
    signature = base64.b64encode(pkcs1_15.new(privatekey).sign(hash_obj))
    return signature

#SHA1加密的数据签名的验签
def rsa_SHA1verify(oridata,publickey,signature):
    #公钥用于对签名的验签
    try:
        #因为签名被base64编码，所以这里先解码，再验签
        hash_obj = SHA1.new(oridata)
        pkcs1_15.new(publickey).verify(hash_obj,base64.b64decode(signature))
        # print('The [%s] is valid signature.'%signature)
        return True
    except (ValueError,TypeError):
        print('The [%s] is invalid signature.'%signature)

#MD5加密算法的rsa签名函数，MD5目的是保护签名之前的数据，即使被获取也无法使用
def rsa_MD5sign(oridata,privatekey,password=None):
    #【私钥】用于对数据加签
    hash_obj = MD5.new(oridata)
    # print(pkcs1_15.new(privatekey).can_sign())  #检查使用了秘钥的pkcs1_15对象能否被签名
    #base64编码的内容打印比较养眼
    signature = base64.b64encode(pkcs1_15.new(privatekey).sign(hash_obj))
    return signature

#MD5加密的数据签名的验签，与rsa_SHA1signverify()基本没啥区别
def rsa_MD5verify(oridata,publickey,signature):
    #读取公钥信息用于验签
    # public_key = RSA.importKey(open("Keys\my_rsa_public.pem").read())
    try:
        #因为签名被base64编码，所以这里先解码，再验签
        hash_obj = MD5.new(oridata)
        pkcs1_15.new(publickey).verify(hash_obj,base64.b64decode(signature))
        # print('The [%s] is valid signature.'%signature)
        return True
    except (ValueError,TypeError):
        print('The [%s] is invalid signature.'%signature)

def md5Data(message):
    #保证传入原始数据即使是String类型也可用
    if type(message) == str and type(message) != bytes:
        print("====>[%s]<==== is a String type data, IIATF1.0 auto convert it to bytes!"%(message))
        message = message.encode()
        hash_obj = MD5.new()
        hash_obj.update(message)
        md5data = hash_obj.hexdigest()
        print(type(md5data),md5data)
        return md5data
    else:
        return None
if __name__ == '__main__':
    pass