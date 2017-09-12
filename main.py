# -*- coding: utf-8 -*-
import urllib2,json,datetime,base64

now_timeYMD=datetime.datetime.now().strftime('%Y-%m-%d')
now_timeHMS=datetime.datetime.now().strftime('%H:M:%S')
timestamp=now_timeYMD+'%20'+now_timeHMS
ak='b45712e97bc4461bb229e4eeee6a0868'
deviceSN='14a240428a87a0a2'
user_input='Use Python to Develop MEMOBIRD API'
printcontent=base64.b64encode(user_input)

Bind_device=urllib2.urlopen('http://open.memobird.cn/home/setuserbind?ak='+ ak +'&timestamp='+ timestamp +'&memobirdID='+ deviceSN +'&useridentifying=1')
User_ID_response=Bind_device.read()
Standard_json=json.loads(User_ID_response)
userid=Standard_json['showapi_userid']

Print_paper=urllib2.urlopen('http://open.memobird.cn/home/printpaper?ak='+ ak + '&timestamp='+ timestamp +'&printcontent=T:'+ printcontent +'&memobirdID='+ deviceSN +'&userID='+ str(userid))
Print_Paper_response=Print_paper.read()
Print_Status_json=json.loads(Print_Paper_response)
printstatus=Print_Status_json['result']

print "用户的咕咕机编号为 %s , 打印结果为 %s , 输出的文字的Base64编码为 %s" % (userid,printstatus,printcontent)
Bind_device.close()
