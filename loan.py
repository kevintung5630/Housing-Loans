#https://www.ntsec.edu.tw/LiveSupply-Content.aspx?a=6829&fld=&key=&isd=1&icop=10&p=1&lsid=16140
money = 10000 * int(input("貸款總額/萬元"))
time = int(input("貸款期限/年"))
time = 12 * time + int(input("又/月"))
#moretime=int(input("寬限期限/年"))
way = input("(本息:0/本金:1)平均攤還")
month = float(input("年利率/%")) / 100
one = 0
onemoney = 0# 1每月應還本金 0剩多少錢(四捨五入產生的零頭)
print(" ")
print(" ")

if(way == "0"):
    one = money * ((1 + month / 12) ** time) * (month / 12 / ((1 + month / 12) ** time - 1))//1
    onemoney = (money * ((1 + month / 12) ** time) * (month / 12 / ((1 + month / 12) ** time - 1)))%1*time//1
    for i in range(1,time+1):
        print("本月利息:" + str((money * month / 12 + 0.5)//1) + "元" , end = '\t')        
        if(i <= onemoney):
            one += 1
        if(i%12 == 0):
            print("第" + str(i//12-1) + "年" + "12" + "月應付" + str(one) + "元" , end = '\t')
        else:
            print("第" + str(i//12) + "年" + str(i%12) + "月應付" + str(one) + "元" , end = '\t')
        print("月還本金:" + str(one - (money * month / 12 + 0.5)//1) + "元")
        if(i <= onemoney):
            one -= 1
        money = money * (1 + month / 12) - one
    money = 0    
elif(way == "1"):
    onemoney = int(money/time + 0.5)
    print("月還本金:" + str(onemoney) + "元")
    for i in range(1,time+1):
        one = int(onemoney + money * month / 12 + 0.5)
        print("本月利息:" + str(int(money * month / 12 + 0.5)) + "元" , end = '\t')
        money = money - onemoney
        if(i == time):
            one = one + money
            money = 0
        if(i%12 == 0):
            print("第" + str(i//12-1) + "年" + "12" + "月應付" + str(one) + "元" , end = '\t')
        else:
            print("第" + str(i//12) + "年" + str(i%12) + "月應付" + str(one) + "元" , end = '\t') 
        print("本金剩:" + str(money) + "元")
else:
    print ("錯誤的格式")

print ("貸款期限" + str(time//12) + "年" + str(time%12) + "月")
#print ("寬限期限" + str(moretime) + "年")
if(way == "0"):
    print ("本息平均攤還")
elif(way == "1"):
    print ("本金平均攤還")
print ("年利率" + str(month * 100) + "%")
