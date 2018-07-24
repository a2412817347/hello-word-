# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:34:55 2018
练习6
1.显示4个商品，然后打印分割线，只要第一页36个商品信息
2.列出36个商品
3.获取所有的商品的价格，并且排序（从高到低）
4.按照销量排序
5.商品过滤，只要15天包退或者包邮的商品信息，显示。
@author: Administrator
"""
url='https://s.taobao.com/search?q=%E6%89%93%E5%8D%B0%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
#显示四个商品，然后打印分割线，只要第一页36个商品信息
#data字典-》mods—字典—》itemlist字典-》data字典-》auctions列表->0 index->title变量
#data字典-》mods—字典—》itemlist字典-》data字典-》auctions列表->0 index->view_price变量
#data字典-》mods—字典—》itemlist字典-》data字典-》auctions列表->0 index->view_sales变量
#data字典-》mods—字典—》itemlist字典-》data字典-》auctions列表->0 index->item_loc变量
for i in range(0,4):
     print('第{}件商品'.format(i+1))
     print(data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
     print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
     print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
     print(data['mods']['itemlist']['data']['auctions'][i]['nick'])
     print(' ')
print(str('-')*20)


for i in range(0,36):
     print('第{}件商品'.format(i+1))
     print(data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
     print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
     print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
     print(data['mods']['itemlist']['data']['auctions'][i]['nick'])
     print(' ')
print(str('-')*20)







ls=[]
def price():
    for i in range(0,36):
        m=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
        ls.append(m)
    return ls
price()
n=sorted(ls)
print('商品价格从高到低为')
x=list(reversed(n))
print(x)






ls=[]
def sales():
    for i in range(0,36):
        m=str(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
        d=int(m[0:-3])
        ls.append(d)
    return ls
sales()
n=sorted(ls)
print('商品销量从高到低为')
x=list(reversed(n))
print(x)



def free():
    for i in range(0,36):
        if float (data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0.00:
            print('第{}件商品包邮'.format(i+1))
            print('商品名称为'+data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
            print('商品的售价为'+data['mods']['itemlist']['data']['auctions'][i]['view_price'])
            print('销量为'+data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
            print('店名为'+data['mods']['itemlist']['data']['auctions'][i]['nick'])
            print(' ')
            print(str('-')*20) 
free()
     
    
     
     

    

