import time

import uiautomation as uia

import pandas as pd
namedirect={}
from pandas.core.reshape import encoding
def get_name(a):
    ChatName=str(a)
    wechat=uia.WindowControl(Name="微信",ClassName="WeChatMainWndForPC")
    wechat.SetActive()
    wechat.ButtonControl(Name="聊天").Click() #将定位会话
    time.sleep(0.5)
    wechat.ListItemControl(Name=ChatName).Click()

    more = wechat.ButtonControl(Name="聊天信息")
    time.sleep(0.5)
    more.Click()
    time.sleep(0.5)
    try:
        more_cheatp=wechat.ButtonControl(Name="查看更多")
        if more_cheatp.Exists():
            time.sleep(0.5)
            more_cheatp.Click()
    finally:
        number=wechat.ListControl(Name="聊天成员")
        people=number.GetChildren()
        for nName in people:
            if nName.Name!="添加":
                namedirect[nName.Name]=" "
def path_excel(csvname,path):
    df=pd.DataFrame(list(namedirect.keys()), columns=["姓名"])
    df.to_csv(path+r"/"+csvname+".csv",encoding="utf-8-sig",index=False)



