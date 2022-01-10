from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
#访问类型为POST,发送两个参数：params==>encText，encSecKey==>encSecKey，且参数被加密过了
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }

data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "40",
    "rid": "A_PL_0_5200022097",
    "threadId": "A_PL_0_5200022097",
}


e = '010001'   #通过 console 执行：bsP6J(["流泪", "强"])
#f 通过 console 执行： bsP6J(Xk6e.md)
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'   #通过 console 执行：bsP6J(["爱心", "女孩", "惊恐", "大笑"])
i = "rwnUoddFqiiEaEg4"    # i 固定之后 获取到的encSecKey 就是固定的


def get_encSecKey():
    return "c4e12fa75d464206b88ccc4141ce3de4de5c17ca8fef63acd9bd8d4ae4b4d86b4ab77af260a79e06a17e08355dec635fa4674741fc0333efa740cf331a2f469973fe93fa4279dd9d66bb5e98cbb77f2c831b514355685c0d0f27f6114b5d8b88b24f592422e88d18bdc03adc54cc0b48b0904d3495774519a47fea2e54d67bfd"
def get_params(data):
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second

def to_16(data):
    pad = 16 - len(data)%16
    data += chr(pad) * pad
    return data

def enc_params(data,key):   #加密过程
    IV = '0102030405060708'
    data = to_16(data)  #AES加密：数据需要是bytes ,否则报错：TypeError: a bytes-like object is required, not 'NoneType'
    aes = AES.new(key=key.encode('utf-8'),IV = IV.encode('utf-8'),mode=AES.MODE_CBC)
    data = aes.encrypt(data.encode('utf-8'))   #加密后的数据,AES加密的内容长度必须是16的倍数,报错如下：ValueError: Input strings must be a multiple of 16 in length
    return str(b64encode(data),'utf-8')  # data:不能用utf-8 进行识别，需要使用b64encode 进行转换

#追踪加密过程，通过如下代码进行了加密，并且重新对data进行了赋值
# var bVj0x = window.asrsea(JSON.stringify(i9b), bsP6J(["流泪", "强"]), bsP6J(Xk6e.md), bsP6J(["爱心", "女孩", "惊恐", "大笑"]));
# e9f.data = j9a.cq9h({
#                 params: bVj0x.encText,
#                 encSecKey: bVj0x.encSecKey
#             })


#加密过程，通过window.asrsea 进行加密，window.asrsea=d
'''
# !function() {
#     function a(a) {  # 变量a=16
#         var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
#         for (d = 0; a > d; d += 1)    #循环16次
#             e = Math.random() * b.length,   #获取一个随机数
#             e = Math.floor(e),  #随机数取整
#             c += b.charAt(e);    #在b中随机抽取一个字符并放入c中，
#         return c    # c = 一个16位的随机字符串
#     }
#     function b(a, b) {    #a:数据     b:0CoJUm6Qyw8W8jud
#         var c = CryptoJS.enc.Utf8.parse(b)      # 加密的秘钥
#           , d = CryptoJS.enc.Utf8.parse("0102030405060708")
#           , e = CryptoJS.enc.Utf8.parse(a)
#           , f = CryptoJS.AES.encrypt(e, c, {      # AES 加密   c:加密的秘钥
#             iv: d,      #加密偏移量
#             mode: CryptoJS.mode.CBC     #加密模式为 CBC
#         });
#         return f.toString()
#     }
#     function c(a, b, c) {
#         var d, e;
#         return setMaxDigits(131),
#         d = new RSAKeyPair(b,"",c),
#         e = encryptedString(d, a)
#     }
#     function d(d, e, f, g) {   # d:数据   e:bsP6J(["流泪", "强"])   f:bsP6J(Xk6e.md)==>很长的字符串   g:bsP6J(["爱心", "女孩", "惊恐", "大笑"])==>0CoJUm6Qyw8W8jud
#         var h = {}
#           , i = a(16);     #i = 获取到一个16位的随机字符串
#         return h.encText = b(d, g),     #d:数据   g:加密秘钥
#         h.encText = b(h.encText, i),     # i:加密秘钥
#         h.encSecKey = c(i, e, f),   #获取encSecKey，e和f都是固定的，当i 固定之后，获取到的 encSecKey 就是固定的
#         h
#     }
#     function e(a, b, d, e) {
#         var f = {};
#         return f.encText = c(a + e, b, d),
#         f
#     }
#     window.asrsea = d,
'''

resp = requests.post(url,data={"params" : get_params(json.dumps(data)),"encSecKey" : get_encSecKey()},headers=headers)
resp.encoding='utf-8'
resp.close()

pl_dic = resp.json()["data"]["comments"]
for user in pl_dic:
    print(user['commentId'],'\t',user['content'])