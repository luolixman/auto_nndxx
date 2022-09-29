import requests
import re
import json

# 将抓包得来的cookie中的SSUUID粘贴到引号中间
SSUUID = "4D7B856EE2746A37F48E163A334DF9FA4B6CC5B3FB1CB46E9152214A83A1E67EC1F01FADDC00853F12D22BF6987DAAEAAAEBA21CA6F22FC68A5538BBB391DCF65E0F571ACAB3DF46046C2842BBBB8E7DD90795E1A6221B553701738681C2CEB13997BB550F8A4D818DB24DD40D333EB983E95021E79C1F00860E0072CED50CE8793160AC4CC9169E979CF95E1DC1EAFA"

# 以下内容无需更改

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; MI MIX 4 Build/S2.MBRJUN.0523; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3171 MMWEBSDK/20211202 Mobile Safari/537.36 MMWEBID/4381 MicroMessenger/8.0.18.2062(0x28001241) Process/toolsmp WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_TW ABI/arm64 ",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/tpg,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Encoding": "gzip, deflate",
	"Cookie": "SSUUID=" + SSUUID
}

def GetStudyID(): # 得到课程id
	url_get = "http://qndxx.bestcood.com/mp/nanning/my/index.html"
	response = requests.get(url_get, headers = headers)
	if ('<title>抱歉，出错了</title><meta charset="utf-8">' in response.text):
		return -1
	id = re.findall(r'(?<=\/mp\/nanning\/daxuexi\/detail_)\d+(?=\.html)', response.text)
	return id[0]

def Study(): # 发送post
	url_hit = "http://qndxx.bestcood.com/mp/nanning/DaXueXi/LearnHit.html"
	id = GetStudyID()
	if (id == -1): 
		return -1
	data = {"id": id}
	response = requests.post(url_hit, headers = headers, data = data)
	return int(json.loads(response.text)['code'])

code = Study()
if (code != 0):
	print("Error!")
else:
	print("Success!")
