# -*- coding: GBK -*-
import urllib2, json, datetime, base64

now_timeYMD = datetime.datetime.now().strftime('%Y-%m-%d')
now_timeHMS = datetime.datetime.now().strftime('%H:%M:%S')
timestamp = now_timeYMD + '%20' + now_timeHMS
ak = 'b45712e97bc4461bb229e4eeee6a0868'
weatherkey='7aa90c510ccd4d24b5d70f45ef626d4e'
deviceSN = '14a240428a87a0a2'
user_input = '测试内容。' + ' ' + now_timeYMD + ' ' + now_timeHMS
printcontent = base64.b64encode(user_input)
UserLocation= 'CN101190201'

def Print_Model():
    Bind_device = urllib2.urlopen(
        'http://open.memobird.cn/home/setuserbind?ak=' + ak + '&timestamp=' + timestamp + '&memobirdID=' + deviceSN + '&useridentifying=1')
    User_ID_response = Bind_device.read()
    Standard_json = json.loads(User_ID_response)
    userid = Standard_json['showapi_userid']

    Print_Paper = urllib2.urlopen(
        'http://open.memobird.cn/home/printpaper?ak=' + ak + '&timestamp=' + timestamp + '&printcontent=T:' + printcontent + '|P:Qk0OAgAAAAAAAD4AAAAoAAAAOgAAAMb///8BAAEAAAAAAAAAAADEDgAAxA4AAAIAAAACAAAAAAAA//////8A///////AAAP///////AAB///////+AAf///////+AB////////4AP///++/f/wB////719//gH////frv/+A////+7ff/8D////779//wP/////37//A////9dW//8D////6rV//wP////a1r//A////+1bf/8D////7/7//wP/////////A/////qr//8D////7/1//wP////aq7//A////3/+1/8D////1VX//wP///17v1f/A////67q+v8D///1d3ev/wP////a3XX/A///9X/73v8D///+1R7rfwP//7XvG17/A//+21u9978D//1v/vda/wP/+6qr2+9/A//1bfbtW78D/263Xb/2/wP/9arvaq2/A/3vV7Xff38D//f63vXV/wP23/93Xvt/A///f9vrV78D/33/dr39fwP19+/d11f/A//f/+77uv8D//9/t1bv/wP/e//b/bX/A//v//1Xf/8D//7/q7vX/wP////e7X//A//7/3W3v/8D////333//wP///9r1v//Af///717//4B///+76///gD///+1///8AH////////gAf///////+AAf///////gAA///////8AAA///////AAA==' + '&memobirdID=' + deviceSN + '&userID=' + str(
            userid))
    Print_Paper_response = Print_Paper.read()
    Print_ContentID_json = json.loads(Print_Paper_response)
    printcontentid = Print_ContentID_json['printcontentid']

    Get_Print_Status = urllib2.urlopen(
        'http://open.memobird.cn/home/getprintstatus?ak=' + ak + '&timestamp=' + timestamp + '&printcontentid=' + str(
            printcontentid))
    Print_Status_response = Get_Print_Status.read()
    Print_Status_json = json.loads(Print_Status_response)
    printstatus = Print_Status_json['printflag']
    print "用户的咕咕机编号为 %s , 输出文字的BASE64编码为 %s , 打印的纸条编号是 %s,打印结果为 %s " % (
        userid, printcontent, printcontentid, printstatus)
    print Standard_json
    print Print_ContentID_json
    print Print_Status_json
    print printcontent
    Bind_device.close()
    Print_Paper.close()
    Get_Print_Status.close()


def Get_Weather_Status():
    Get_Weather=urllib2.urlopen('https://free-api.heweather.com/v5/weather?city='+UserLocation+'&key='+weatherkey)
    Weather_Status_response=Get_Weather.read()
    Weather_Status_json=json.loads(Weather_Status_response)
    print Weather_Status_json

Print_Model()
Get_Weather_Status()
