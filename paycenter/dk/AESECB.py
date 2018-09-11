# coding=utf-8

# Created by slowchen on 2018/1/10 13:48.

import base64
import re
# from crypto.Cipher import AES
from Crypto.Cipher import AES

class AESECB:
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_ECB
        self.bs = 16  # block size
        self.PADDING = lambda s: s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def encrypt(self, text):
        generator = AES.new(self.key, self.mode)  # ECB模式无需向量iv
        crypt = generator.encrypt(self.PADDING(text))
        crypted_str = base64.b64encode(crypt)
        result = crypted_str.decode()
        return result

    def decrypt(self, text):
        generator = AES.new(self.key, self.mode)  # ECB模式无需向量iv
        text += (len(text) % 4) * '='
        decrpyt_bytes = base64.b64decode(text)
        meg = generator.decrypt(decrpyt_bytes)
        # 去除解码后的非法字符
        try:
            result = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f\n\r\t]').sub('', meg.decode())
        except Exception:
            result = '解码失败，请重试!'
        return result


if __name__ == '__main__':
    aes = AESECB('this is aes key!')
    print(aes.encrypt('pythonaes123456'))
    print(aes.decrypt('bvN4eERKQBOSXu5EpZ+rBw=='))
    print(aes.decrypt('yzm34N/bEY8kVJNeS93Gv1svJI77YPjaK1+mW+/A4FY='))  # python is very good