# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:44:59 2018
练习题4：
1.打印每天18点的天气信息，温度，程序，情况，气压，最高温度，最低温度
2.写出英文版的天气-天气情况，用户输入英文   application应用
3.打印温度折线图
    1----------
    2--------------------
    3-------
    4----------
4.获取所有的温度，并且排序（sorted([1,4,-1,8])##########使用此方法排序）
5.友情提示，根据温度提示穿衣，打伞，出门(可选)

全球5天天气
@author: Administrator
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
print('第一天下午6点的天气情况')
print('温度'+str(data['list'][1]['main']['temp']))
print('最低温度'+str(data['list'][1]['main']['temp_min']))
print('最高温度'+str(data['list'][1]['main']['temp_max']))
print('天气情况'+str(data['list'][1]['weather'][0]['description']))
print('第二天下午6点的天气情况')
print('温度'+str(data['list'][9]['main']['temp']))
print('最低温度'+str(data['list'][9]['main']['temp_min']))
print('最高温度'+str(data['list'][9]['main']['temp_max']))
print('天气情况'+str(data['list'][9]['weather'][0]['description']))
print('第三天下午6点的天气情况')
print('温度'+str(data['list'][17]['main']['temp']))
print('最低温度'+str(data['list'][17]['main']['temp_min']))
print('最高温度'+str(data['list'][17]['main']['temp_max']))
print('天气情况'+str(data['list'][17]['weather'][0]['description']))
print('第四天下午6点的天气情况')
print('温度'+str(data['list'][25]['main']['temp']))
print('最低温度'+str(data['list'][25]['main']['temp_min']))
print('最高温度'+str(data['list'][25]['main']['temp_max']))
print('天气情况'+str(data['list'][25]['weather'][0]['description']))
print('第五天下午6点的天气情况')
print('温度'+str(data['list'][33]['main']['temp']))
print('最低温度'+str(data['list'][33]['main']['temp_min']))
print('最高温度'+str(data['list'][33]['main']['temp_max']))
print('天气情况'+str(data['list'][33]['weather'][0]['description']))
def weather(a,b):
    print('第'+'a'+'天的天气情况为')
    print('温度为'+str(data['list'][b]['main']['temp'])+'最低温度为'+str(data['list'][b]['main']['temp_min'])+'最高温度'+str(data['list'][b]['main']['temp_max'])+'天气情况'+str(data['list'][b]['weather'][0]['description']))
weather(1,2)
weather(2,9)
weather(3,17)
weather(4,25)
weather(5,33)
print('温度折线图')
print('第一天temp'+'+'*int(data['list'][1]['main']['temp']))
print('第二天temp'+'+'*int(data['list'][9]['main']['temp']))
print('第三天temp'+'+'*int(data['list'][17]['main']['temp']))
print('第四天temp'+'+'*int(data['list'][25]['main']['temp']))
print('第五天temp'+'+'*int(data['list'][33]['main']['temp']))
print('这五天的温度从小到大的排序为')
m=data['list'][1]['main']['temp']
n=data['list'][9]['main']['temp']
x=data['list'][17]['main']['temp']
y=data['list'][25]['main']['temp']
z=data['list'][33]['main']['temp']
print(sorted([m,n,x,y,z]))


City=input('Please enter the name of the city you want to inquire')
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url.format(City)).read().decode('utf-8','ignore')
import json#将字符串转换为字典
main=data=json.loads(data)
data['list'][0]['weather'][0]['main']
print('The weather is the case'+str (data['list'][0]['weather'][0]['main']))









