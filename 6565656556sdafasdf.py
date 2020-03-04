'''
https://cloud.tencent.com/act/pro/AI?fromSource=gwzcw.3176272.3176272.3176272&utm_medium=cpc&utm_id=gwzcw.3176272.3176272.3176272


下面对上面这个网站,实现ocr爬虫.



'''









# https://cloud.tencent.com/capi/ajax/?action=delegate&regionId=1&serviceType=ocr&cmd=OcrDemo&version=3&uin=100009575712&csrfCode=2042660485





'''
发送

curl 'https://cloud.tencent.com/capi/ajax/?action=delegate&regionId=1&serviceType=ocr&cmd=OcrDemo&version=3&uin=100009575712&csrfCode=2042660485' -H 'authority: cloud.tencent.com' -H 'accept: */*' -H 'sec-fetch-dest: empty' -H 'x-requested-with: XMLHttpRequest' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36' -H 'content-type: application/json; charset=UTF-8' -H 'origin: https://cloud.tencent.com' -H 'sec-fetch-site: same-origin' -H 'sec-fetch-mode: cors' -H 'referer: https://cloud.tencent.com/act/pro/AI?fromSource=gwzcw.3176272.3176272.3176272&utm_medium=cpc&utm_id=gwzcw.3176272.3176272.3176272' -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7' -H 'cookie: qcmainCSRFToken=S1-PGtqhVL; language=zh; qcloud_visitId=53d7899d84ad9a2e1c9df633331b984f; _ga=GA1.2.1110611498.1583290641; pgv_pvi=1755159552; pgv_si=s4287541248; qcloud_uid=2a3ecea255002525c55c2d485af13d51; pgv_info=ssid=s4072147865; ts_refer=www.baidu.com/link; pgv_pvid=4849237057; ts_uid=3493638520; _gcl_au=1.1.1134766353.1583290643; lastLoginType=wx; uin=o100009575712; tinyid=144115212993957686; skey=ekJpjrTPKdnbCbah-TNEasvK7wIKl6UDJMf*JB5Cqyo_; loginType=wx; intl=1; qcact.sid=s%3AF-l7BsPb7K04qsraGQOaF_hrlBxd7bcZ.%2FIlih2GxdcojnvzoyQcfE%2FFOMQEmUNyQvKHHLvm5vH4; qcloud_from=gwzcw.3176272.3176272.3176272-1583290815474; nick=100009575712' --data-binary '{"data":{"Version":"2018-11-19","ToAction":"GeneralBasicOCR","ToModule":"ocr","Extra":"{\"ImageUrl\":\"https://ocrdemo-temp-1254418846.cos.ap-guangzhou.myqcloud.com/1258876080-2.jpg\"}"}}' --compressed
















'''

