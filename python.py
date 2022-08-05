import json

import requests;
import hashlib;
import time;
import datetime;

def login(account,password):#登录获取key
    URL="http://floor.huluxia.com/account/login/ANDROID/4.1.7"
    data={
        "device_code":"%5Bd%5D0b2e7f02-92c5-48de-a119-b5536304c752",
        "account": account,
        "password":password,
        "sign":"0C75BDDC32F07903F9F71C01C9406140",
        "login_type":2
    }
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "PostmanRuntime/7.28.4",

    }
    res=requests.post(URL,headers=header,data=data)
    if (len(json.loads(res.text).get("msg")))==0:
        return json.loads(res.text).get("_key")
    else:
        return json.loads(res.text).get("msg")

def passwordMd5(password):#密码加密
    m = hashlib.md5()
    m.update(str(password).encode("utf-8"))
    return m.hexdigest()

def sign(_key,cat_id):#执行签到
    URL="http://floor.huluxia.com/user/signin/ANDROID/4.0"
    data={
        "device_code":"%5Bd%5D0b2e7f02-92c5-48de-a119-b5536304c752",
        "_key": _key,
        "cat_id":cat_id
    }
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "PostmanRuntime/7.28.4",
    }
    res=requests.post(URL,headers=header,data=data)
    if len(json.loads(res.text).get('msg'))==0:
        return "签到成功！"
    else:
        return "签到失败！"

with open('./config.json','r',encoding='utf8')as fp:#获取账号密码
    json_data = json.load(fp)
    user=json_data.get("user")
    cat_id={1, 2, 3}
    for n in range(len(json_data['user'])):
        _key=login(json_data['user'][n]['account'],passwordMd5(json_data['user'][n]['password']))
        if _key=="账号或密码错误":
            print("=========账号"+str(n+1)+"===========")
            print("账号或密码错误")
            print(datetime.datetime.now())
            print("========================")
        else:
            print("=========账号"+str(n+1)+"===========")
            for n in set(cat_id):
                print(sign(_key,n))
                time.sleep(json_data.get("signtime")/1000)#延迟时间
                print(datetime.datetime.now())
            print("========================")
    print("所有账号签到完毕")
    print(datetime.datetime.now())
