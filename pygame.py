from tkinter import *
from threading import Timer

root = Tk()

money = 0
store_count = 1
store_profit = 1
store_price = pow(4, store_count)

def DisplayStoreInfo():
	myMoney = Label(root, text="Money $" + str(money))
	myStore = Label(root, text="Store Count = " + str(store_count))

def autoMoney():
	global store_count
	global money
	global myCurrentMoney
	money += store_count
	myCurrentMoney = Label(root, text="Current money: " + str(money) + "$", font=20, bd=1)
	myCurrentMoney.grid(row=1, columnspan=4)
	Timer(1, autoMoney).start()


autoMoney()

def BuyStore():
	global store_count
	global money
	global myCurrentMoney
	global myButton
	global myCurrentIncome
	global store_price
	global myTitle
	if money < store_price:
		return
	money -= pow(4, store_count)
	store_count += 1
	store_price = pow(4, store_count)

	myCurrentMoney = Label(root, text="Current money: " + str(money) + "$", font=20, bd=1)
	myCurrentMoney.grid(row=1, columnspan=4)
	myButton = Label(root, text="Lemonade Stand: " + str(store_count))
	myButton.grid(row=3, column=3)
	myCurrentIncome = Label(root, text="Current income per second: " + str(store_count) + "$", font=20).grid(row=2, columnspan=4)
	myTitle = Label(root, text="Store price: " + str(store_price), font=15, bd=1, relief="sunken").grid(row=0,
																										columnspan=4)

def ClickToGetMoney():
	global money
	global myCurrentMoney

	money += 1

	myCurrentMoney = Label(root, text="Current money: " + str(money) + "$", font=20, bd=1)
	myCurrentMoney.grid(row=1, columnspan=4)

clickMoney = Button(root, text="click to get money", command=ClickToGetMoney)
clickMoney.grid(row=3, column=1)

buyLemonade = Button(root, text="buy lemonade stand", command=BuyStore)
buyLemonade.grid(row=3, column=2)

myButton = Label(root, text="Lemonade Stand: " + str(store_count))
myButton.grid(row=3, column=3)

myCurrentMoney = Label(root, text="Current money: " + str(money) + "$", font=20, bd=1).grid(row=1, columnspan=4)
myCurrentIncome = Label(root, text="Current income per second: " + str(store_count) + "$", font=20).grid(row=2, columnspan=4)

myTitle = Label(root, text="Store price: " + str(store_price), font=15, bd=1, relief="sunken").grid(row=0, columnspan=4)

root.mainloop()
