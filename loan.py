#https://www.ntsec.edu.tw/LiveSupply-Content.aspx?a=6829&fld=&key=&isd=1&icop=10&p=1&lsid=16140

one = 0#每次還錢總額
onemoney = 0# 1每月應還本金 0剩多少錢(四捨五入產生的零頭)
allmoremoney = 0#總利息

import re#匯入字串表示程式庫

import tkinter as tk#匯入圖形化使用者面程式庫(名稱縮寫為tk)
window = tk.Tk()#創建視窗

def is_number(num):#定義副程式(判斷使用者打的字是不是數字)
    #pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    pattern = re.compile(r'^\s*[-+]?(\d*\.\d+|\d+)\s*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False

def is_space(num):#定義副程式(判斷使用者打的字是不是空白)
    pattern = re.compile(r'^\s*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False

def buttonClick():#定義副程式(按下按鈕(試算))
    if(is_space(entryMoreTime.get())):
        entryMoreTime.delete(0, tk.END)
        entryMoreTime.insert(0, "0")
    
    class Scrollbar_Example:
        def __init__(self):#定義副程式(卷軸視窗)
            self.window = tk.Tk()
            self.scrollbar = tk.Scrollbar(self.window)
            self.scrollbar.pack(side="right", fill="y")
            self.listbox = tk.Listbox(self.window, yscrollcommand=self.scrollbar.set)

            way = entryWay.get()
            if(way == "本息平均攤還" or way == "本金平均攤還"):
                if(is_number(entryMoney.get()) and is_number(entryTimeYear.get()) and is_number(entryMoreTime.get()) and is_number(entryMonth.get())):

                    money = int(entryMoney.get())*10000
                    money2 = entryMoney.get()
                    time = int(entryTimeYear.get()) * 12
                    moretime = int(entryMoreTime.get()) * 12
                    month = float(entryMonth.get()) / 100
                    one = 0 # 這月要付多少錢
                    onemoney = 0 # 本金:每月應還本金 本息:剩多少錢(四捨五入產生的零頭)
                    allmoremoney = 0 #利息



                    time = time - moretime
                    if(way == "本息平均攤還" or way == "本金平均攤還"):
                        for i in range(1,moretime+1):
                            self.listbox.insert("end", " ")
                            self.listbox.insert("end", "本月利息:" + str(int(money * month / 12 + 0.5)) + "元")
                            allmoremoney = allmoremoney + int((money * month / 12 + 0.5))
                            if(i%12 == 0):
                                self.listbox.insert("end", "第" + str(i//12-1) + "年" + "12" + "月應付" + str(int(money * month / 12 + 0.5)) + "元")
                            else:
                                self.listbox.insert("end", "第" + str(i//12) + "年" + str(i%12) + "月應付" + str(int(money * month / 12 + 0.5)) + "元")
                    if(way == "本息平均攤還"):#本息平均攤還
                        one = int(money * ((1 + month / 12) ** time) * (month / 12 / ((1 + month / 12) ** time - 1)))
                        onemoney = int((money * ((1 + month / 12) ** time) * (month / 12 / ((1 + month / 12) ** time - 1)))%1*time)
                        for i in range(1 + moretime , time + 1 + moretime):
                            self.listbox.insert("end", " ")
                            self.listbox.insert("end", "本月利息:" + str(int(money * month / 12 + 0.5)) + "元")
                            allmoremoney = allmoremoney + int((money * month / 12 + 0.5))
                            if(i <= onemoney + moretime):
                                one += 1
                            if(i%12 == 0):
                                self.listbox.insert("end", "第" + str(i//12-1) + "年" + "12" + "月應付" + str(one) + "元")
                            else:
                                self.listbox.insert("end", "第" + str(i//12) + "年" + str(i%12) + "月應付" + str(one) + "元")
                            self.listbox.insert("end", "月還本金:" + str(one - int((money * month / 12 + 0.5))) + "元")
                            if(i <= onemoney + moretime):
                                one -= 1
                            money = money * (1 + month / 12) - one
                        money = 0
                        self.listbox.insert("end", " ")
                    elif(way == "本金平均攤還"):#本金平均攤還
                        onemoney = int(money/time + 0.5)
                        for i in range(1 + moretime , time + 1 + moretime):
                            self.listbox.insert("end", " ")
                            one = int(onemoney + money * month / 12 + 0.5)
                            self.listbox.insert("end", "本月利息:" + str(int(money * month / 12 + 0.5)) + "元")
                            allmoremoney = allmoremoney + int((money * month / 12 + 0.5))
                            money = money - onemoney
                            if(i == time + moretime):
                                one = one + money
                                money = 0
                            if(i%12 == 0):
                                self.listbox.insert("end", "第" + str(i//12-1) + "年" + "12" + "月應付" + str(one) + "元")
                            else:
                                self.listbox.insert("end", "第" + str(i//12) + "年" + str(i%12) + "月應付" + str(one) + "元")
                            self.listbox.insert("end", "本金剩:" + str(money) + "元")
                        self.listbox.insert("end", " ")
                        self.listbox.insert("end", "月還本金:" + str(onemoney) + "元")   

                    self.listbox.insert("end", "利息總共:" + str(allmoremoney) + "元")
                    self.listbox.insert("end", "貸款總額" + money2 + "萬元")
                    self.listbox.insert("end", "貸款期限" + entryTimeYear.get() + "年")
                    self.listbox.insert("end", "寬限期" + entryMoreTime.get() + "年")
                    self.listbox.insert("end",entryWay.get())
                    self.listbox.insert("end", "年利率 " + entryMonth.get() + "%")
                    
                    money = int(entryMoney.get())*10000
                    time = int(entryTimeYear.get()) * 12
                    moretime = int(entryMoreTime.get()) * 12
                    way = entryWay.get()
                    month = float(entryMonth.get()) / 100

                    
                else:
                    self.listbox.insert("end", "錯誤的格式")
                    for i in range(20):
                        self.listbox.insert("end", " ")
            else:
                self.listbox.insert("end", "錯誤的格式")
                for i in range(20):
                        self.listbox.insert("end", " ")

            self.listbox.pack(side="left", fill="both")
            self.scrollbar.config(command=self.listbox.yview)
            self.window.mainloop()
            
    if __name__ == '__main__':
        app = Scrollbar_Example()

def buttonClick0():
    entryWay.delete(0, tk.END)
    entryWay.insert(0, "本息平均攤還") 
    
def buttonClick1():
    entryWay.delete(0, tk.END)
    entryWay.insert(0, "本金平均攤還")

labelBegin = tk.Label(window, text = "============================")
labelMoney = tk.Label(window, text = "貸款總額/萬元")
entryMoney = tk.Entry(window)
labelTimeYear = tk.Label(window, text = "貸款期限/年")
entryTimeYear = tk.Entry(window)
labelMoreTime = tk.Label(window, text = "寬限期/年")
entryMoreTime = tk.Entry(window)
labelWay = tk.Label(window, text = "(本息/本金)平均攤還")
button0 = tk.Button(window, text = "本息", command = buttonClick0)
button1 = tk.Button(window, text = "本金", command = buttonClick1)
entryWay = tk.Entry(window, text = "")
labelMonth = tk.Label(window, text = "年利率/%")
entryMonth = tk.Entry(window)
button = tk.Button(window, text = "試算", command = buttonClick)
labelEnd = tk.Label(window, text = "============================")

#預設填答案
entryMoney.insert(0, "1500")
entryTimeYear.insert(0, "30")
entryMoreTime.insert(0, "2")
entryWay.insert(0, "本息平均攤還")
entryMonth.insert(0, "2.25")

labelBegin.pack()
labelMoney.pack()
entryMoney.pack()
labelTimeYear.pack()
entryTimeYear.pack()
labelMoreTime.pack()
entryMoreTime.pack()
labelWay.pack()
button0.pack()
button1.pack()
entryWay.pack()
labelMonth.pack()
entryMonth.pack()
button.pack()
labelEnd.pack()
window.mainloop()
