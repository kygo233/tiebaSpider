# -*- coding: GBK -*-
def dict2list(dic:dict):
    ''' 将字典转化为列表 '''
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst

f = open('C:/Users/ys/Desktop/tb1.txt', encoding='UTF-8')
str1=f.read() 
s=eval(str1)
list1=sorted(dict2list(s), key=lambda x:x[1], reverse=True)
result=[]
tmp="{value:num, name:'tb'}"
for n in range(0,20):
    tb=list1[n]
    count=str(tb[1])
    result.append(tmp.replace("num",count ).replace("tb", tb[0]))   
f.close()
print(",".join(result))