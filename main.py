'''
写一下腾讯ocr接口的调用方法.
主要是理解网络请求的过程
'''


# 目前还没搞明白如何本地上传图片到腾讯的服务器.



'''
目前给的方法是,给一个图片的url,这点可以通过对象存储来实现.
具体可以看我的zhangbo2008 里面的minio镜像来搭建.

然后curl戏码命令,把imageurl 后面的地址改成自己需要的地址即可.



'''
tmp='''



curl 'https://cloud.tencent.com/capi/ajax/?action=delegate&regionId=1&serviceType=ocr&cmd=OcrDemo&version=3&uin=100009575712&csrfCode=1505491908' -H 'authority: cloud.tencent.com' -H 'accept: */*' -H 'sec-fetch-dest: empty' -H 'x-requested-with: XMLHttpRequest' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36' -H 'content-type: application/json; charset=UTF-8' -H 'origin: https://cloud.tencent.com' -H 'sec-fetch-site: same-origin' -H 'sec-fetch-mode: cors' -H 'referer: https://cloud.tencent.com/act/pro/AI?fromSource=gwzcw.3176272.3176272.3176272&utm_medium=cpc&utm_id=gwzcw.3176272.3176272.3176272' -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7' -H 'cookie: qcmainCSRFToken=S1-PGtqhVL; language=zh; qcloud_visitId=53d7899d84ad9a2e1c9df633331b984f; _ga=GA1.2.1110611498.1583290641; pgv_pvi=1755159552; pgv_si=s4287541248; qcloud_uid=2a3ecea255002525c55c2d485af13d51; pgv_info=ssid=s4072147865; ts_refer=www.baidu.com/link; pgv_pvid=4849237057; ts_uid=3493638520; _gcl_au=1.1.1134766353.1583290643; lastLoginType=wx; qcloud_from=gwzcw.3176272.3176272.3176272-1583290815474; qcact.sid=s%3Ad7Yh7u1mGC-rukzemWVIn5mx_yNCaiCQ.0n8sY7PNnBUIbV2m3%2B%2BpxyPuJiGGsYIXQdzrJQrUu%2F8; uin=o100009575712; tinyid=144115212993957686; skey=joMZyZ4IGvgJlJ-XnzjJ0gXJTsIvkkYZs7*rQh5CinU_; intl=1; refreshSession=1; appid=1258876080; moduleId=1258876080; systemTimeGap=93; ownerUin=O100009575712G; opc_xsrf=a0599a7c8cbceccad6bdb6b271e588d4%7C1583304730; nick=100009575712' --data-binary '{"data":{"Version":"2018-11-19","ToAction":"GeneralBasicOCR","ToModule":"ocr","Extra":"{\"ImageUrl\":\"https://www.cpnic.com/UploadFiles/img_3_1117402832_3851013605_26.jpg\"}"}}' --compressed



'''

# import subprocess,os
#
# # a=subprocess.call(tmp,shell=False)
# a=os.popen(tmp,shell=False)
#
# print(a)
#
# pyton 里面调用curl不好使,只能在liunx里面输入上tmp对应的字符串即可.
