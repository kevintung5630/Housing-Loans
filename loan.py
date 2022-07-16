one = 0
onemoney = 0# 1每月應還本金 0剩多少錢(四捨五入產生的零頭)
allmoremoney = 0#總利息

import tkinter as tk
window = tk.Tk()

def buttonClick():
    money = int(entryMoney.get())*10000
    time = int(entryTimeYear.get()) * 12 + int(entryTimeMonth.get())
    way = entryWay.get()
    month = float(entryMonth.get()) / 100
    one = 0
    onemoney = 0 # 1每月應還本金 0剩多少錢(四捨五入產生的零頭)
    allmoremoney = 0 #利息



    if(way == "本息平均攤還"):
        one = int(money * ((1 + month / 12) ** time) * (month / 12 / ((1 + month / 12) ** time - 1)))
        onemoney = int((money * ((1 + month / 12) ** time) * (month / 12 / ((1 + month / 12) ** time - 1)))%1*time)
        for i in range(1,time+1):
            print("本月利息:" + str((money * month / 12 + 0.5)//1) + "元" , end = '\t')
            allmoremoney = allmoremoney + int((money * month / 12 + 0.5))
            if(i <= onemoney):
                one += 1
            if(i%12 == 0):
                print("第" + str(i//12-1) + "年" + "12" + "月應付" + str(one) + "元" , end = '\t')
            else:
                print("第" + str(i//12) + "年" + str(i%12) + "月應付" + str(one) + "元" , end = '\t')
            print("月還本金:" + str(one - int((money * month / 12 + 0.5))) + "元")
            if(i <= onemoney):
                one -= 1
            money = money * (1 + month / 12) - one
        money = 0
    elif(way == "本金平均攤還"):
        onemoney = int(money/time + 0.5)
        print("月還本金:" + str(onemoney) + "元")
        for i in range(1,time+1):
            one = int(onemoney + money * month / 12 + 0.5)
            print("本月利息:" + str((money * month / 12 + 0.5) // 1) + "元" , end = '\t')
            allmoremoney = allmoremoney + int((money * month / 12 + 0.5))
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

    print("利息總共:" + str(allmoremoney) + "元")



    class Scrollbar_Example:
        def __init__(self):
            self.window = tk.Tk()

            self.scrollbar = tk.Scrollbar(self.window)
            self.scrollbar.pack(side="right", fill="y")

            self.listbox = tk.Listbox(self.window, yscrollcommand=self.scrollbar.set)
            for i in range(100):
                self.listbox.insert("end", str(i) + " 123 ")
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
labelTimeMonth = tk.Label(window, text = "又/月")
entryTimeMonth = tk.Entry(window)
labelWay = tk.Label(window, text = "(本息:/本金:)平均攤還")
button0 = tk.Button(window, text = "本息", command = buttonClick0)
button1 = tk.Button(window, text = "本金", command = buttonClick1)
entryWay = tk.Entry(window, text = "")
labelMonth = tk.Label(window, text = "年利率/%")
entryMonth = tk.Entry(window)
button = tk.Button(window, text = "試算", command = buttonClick)
labelEnd = tk.Label(window, text = "============================")

#預設填答案
entryMoney.insert(0, "100")
entryTimeYear.insert(0, "1")
entryTimeMonth.insert(0, "0")
entryWay.insert(0, "本息平均攤還")
entryMonth.insert(0, "1")

labelBegin.pack()
labelMoney.pack()
entryMoney.pack()
labelTimeYear.pack()
entryTimeYear.pack()
labelTimeMonth.pack()
entryTimeMonth.pack()
labelWay.pack()
button0.pack()
button1.pack()
entryWay.pack()
labelMonth.pack()
entryMonth.pack()
button.pack()
labelEnd.pack()
window.mainloop()
