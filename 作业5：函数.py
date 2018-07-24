# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:35:23 2018
练习五：
1.优化代码，用函数的方式修改练习4  输出每一天的天气（函数）
2.打印温度折线图，使用函数来优化（必须要有返回值）
3使用到函数，使用到list的一些功能
函数：做某件事的指令的集合
变量（生命周期）
语法1
def 函数名（）：
    指令集合
语法2     
def 函数名（a,b,c,e）：
    指令集合（a）
    指令集合（b,c,e）
语法3
def 函数名（a,b）：
    指令集合（a,b）
    return xxx
@author: Administrator
"""
a=3#全局变量，生命作用于整个环境
def calc():
    b=4####局部变量，内部变量，生命在缩进里面
    print(b)
calc()#调用函数
print(b)#无法打印，b变量生命周期在缩进里，外围调用不成
###函数语法2
#函数的参数说明快捷键：数遍在参数内+快捷键Ctrl i
def calc(a,b):
    '计算两个数之和，a是一个数,b也是一个数'
    print('a+b'+str(a+b))
    calc()
def calc(a,b,c):
    return a+b+c
print(calc(1,2,3))
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
#天气情况
def weather(a,b):
    print('第'+'a'+'天的天气情况为')
    print('温度为'+str(data['list'][b]['main']['temp'])+'最低温度为'+str(data['list'][b]['main']['temp_min'])+'最高温度'+str(data['list'][b]['main']['temp_max'])+'天气情况'+str(data['list'][b]['weather'][0]['description']))
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)
#打印温度折线图
def chart(a):
    data1=data['list'][a]['main']['temp']
    num=str('=')*int(data1)
    return num
print('这五天的温度折线图为')
print('1'+chart(2))
print('2'+chart(10))    
print('3'+chart(18))   
print('4'+chart(26))   
print('5'+chart(34))   
#列表使用函数
def ls(b):
    s=data['list'][b]['main']['temp']
    return s
m1=ls(2)
m2=ls(10)
m3=ls(18)
m4=ls(26)
m5=ls(34)
m=[m1,m2,m3,m4,m5]
print('温度的排序为：')
print(sorted(m))
    
#1.使用多选其一，完成天气的提醒，淘宝客户端
def information():
    for a in range(2,36,8):
        print('第{}天'.format(a//8+1)+':')
        print('天气'+data['list'][a]['weather'][0]['description'])
        print('温度'+str(data['list'][a]['main']['temp']))
        if data['list'][a]['main']['temp']>30:
            print('气温炎热，注意防晒！')
        elif data['list'][a]['main']['temp']>20:
            print('气温适中，适宜出行！')
        else:
            print('天气寒冷，注意添加新衣！')
information()




