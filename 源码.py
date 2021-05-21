import random
from playsound import playsound
print("欢迎使用CC牌无广告无重复无45号抽号软件，五班特供版！")
while(True):
    a=[]
    b=input("输入起始数字：")
    c=input("输入结束数字：")
    d=input("输入抽取数量：")
    ia=int(b)
    ib=int(c)
    ic=int(d)
    a=range(ia,ib+1)
    while(True):
        b=random.sample(a,ic)
        if 45 and 9  not in b:
            break
    for value in b:
        print(value)
