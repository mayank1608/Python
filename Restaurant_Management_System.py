from tkinter import*
import random
import time;

# Tk(screenName=None,  baseName=None,  className='Tk',  useTk=1)

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

txt_input = StringVar()
operator=""

#-----------------------------------------------------------------#
#						 	Top Frame
#-----------------------------------------------------------------#

Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)


#-----------------------------------------------------------------#
#						 	Left Frame
#-----------------------------------------------------------------#

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

#-----------------------------------------------------------------#
#						 	Right Frame
#-----------------------------------------------------------------#

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

#-----------------------------------------------------------------#
#						 	Time
#-----------------------------------------------------------------#

localtime = time.asctime(time.localtime(time.time()))

#-----------------------------------------------------------------#
#						 	Top Info
#-----------------------------------------------------------------#

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Management System", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1,column=0)


#-----------------------------------------------------------------#
#						 	Calculator
#-----------------------------------------------------------------#

def btnClick(number):
	global operator
	operator= operator + str(number)
	txt_input.set(operator)
	
def btnClearDisplay():
	global operator
	operator=""
	txt_input.set("")
	
def btnEqualsInput():
	global operator
	sumup = str(eval(operator))
	txt_input.set(sumup)
	operator=""	
	
txtDisplay=Entry(f2, font=('arial', 20, 'bold'), textvariable=txt_input, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtDisplay.grid(columnspan=4)

#---------------------- First row
btn7=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='7', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='8', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='9', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(9)).grid(row=2,column=2)


btnAdd=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='+', fg="Blue", bg="powder blue", bd=8, command=lambda:btnClick("+")).grid(row=2,column=3)

#---------------------- Second row

btn4=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='4', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='5', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='6', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(6)).grid(row=3,column=2)

btnSubtract=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='-', fg="Blue", bg="powder blue", bd=8, command=lambda:btnClick("-")).grid(row=3,column=3)

#---------------------- Third row

btn1=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='1', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='2', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='3', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(3)).grid(row=4,column=2)

btnMultiplyBtn=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='*', fg="Blue", bg="powder blue", bd=8, command=lambda:btnClick("*")).grid(row=4,column=3)

#---------------------- Fourth row

btn0=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='0', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='C', fg="Blue", bg="powder blue", bd=8, command=btnClearDisplay).grid(row=5,column=1)


btnEquals=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='=', fg="Blue", bg="powder blue", bd=8, command=btnEqualsInput).grid(row=5,column=2)

btnDivision=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='/', fg="Blue", bg="powder blue", bd=8, command=lambda:btnClick("/")).grid(row=5,column=3)

#btnDot=Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), text='.', fg="Black", bg="powder blue", bd=8, command=lambda:btnClick(".")).grid(row=5,column=3)

#-----------------------------------------------------------------#
#						 	Billing
#-----------------------------------------------------------------#
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()
Drinks = StringVar()

Cost = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

def Ref():
	x=random.randint(12908,50867)
	randonRef = str (x)
	rand.set(randonRef)
	
	CoFries = float(Fries.get()) * 40
	CoBurger = float(Burger.get()) * 50
	CoFilet = float(Filet.get()) * 60
	CoChicken_Burger = float(Chicken_Burger.get()) * 80
	CoCheese_Burger = float(Cheese_Burger.get()) * 70
	CoDrinks = float(Drinks.get()) * 20
	
	
	TotalCost = (CoFries + CoBurger + CoFilet + CoChicken_Burger + CoCheese_Burger + CoDrinks)
	TaxonMeal = ((CoFries + CoBurger + CoFilet + CoChicken_Burger + CoCheese_Burger + CoDrinks) * 0.2)
	ServiceonMeal = ((CoFries + CoBurger + CoFilet + CoChicken_Burger + CoCheese_Burger + CoDrinks)/99)	
	
	CostofMeal = "Rs", str('%.2f' %(CoFries + CoBurger + CoFilet + CoChicken_Burger + CoCheese_Burger + CoDrinks))	
	Service = "Rs", str('%.2f' % ServiceonMeal)
	TotalMealCost = "Rs", str('%.2f' % (TotalCost + TaxonMeal + ServiceonMeal))
	
	
	Cost.set(CostofMeal)
	Service_Charge.set(Service)
	Tax.set(TaxonMeal)
	SubTotal.set(CostofMeal)
	Total.set(TotalMealCost)
	
	
	
def qExit():
	root.destroy()
	
def Reset():
	rand.set("")
	Fries.set("")
	Burger.set("")
	Filet.set("")
	Chicken_Burger.set("")
	Cheese_Burger.set("")
	Drinks.set("")
	Cost.set("")
	Service_Charge.set("")
	Tax.set("")
	SubTotal.set("")
	Total.set("")



#------------------------------------------------First Row-----------------------------------------#

labelReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", fg="Steel Blue", bd=10, anchor='w')
labelReference.grid(row=0,column=0)
txtReference=Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtReference.grid(row=0,column=1)

#----------------------

labelFries = Label(f1, font=('arial', 16, 'bold'), text="Large Fries", fg="Steel Blue", bd=10, anchor='w')
labelFries.grid(row=1,column=0)
txtFries=Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtFries.grid(row=1,column=1)

#----------------------


labelBurger = Label(f1, font=('arial', 16, 'bold'), text="Burger Meal", fg="Steel Blue", bd=10, anchor='w')
labelBurger.grid(row=2,column=0)
txtBurger=Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtBurger.grid(row=2,column=1)

#----------------------


labelFilet = Label(f1, font=('arial', 16, 'bold'), text="Filet Meal", fg="Steel Blue", bd=10, anchor='w')
labelFilet.grid(row=3,column=0)
txtFilet=Entry(f1, font=('arial', 16, 'bold'), textvariable=Filet, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtFilet.grid(row=3,column=1)

#----------------------


labelChicken = Label(f1, font=('arial', 16, 'bold'), text="Chicken Meal", fg="Steel Blue", bd=10, anchor='w')
labelChicken.grid(row=4,column=0)
txtChicken=Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken_Burger, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtChicken.grid(row=4,column=1)

#----------------------

labelCheese = Label(f1, font=('arial', 16, 'bold'), text="Cheese Meal", fg="Steel Blue", bd=10, anchor='w')
labelCheese.grid(row=5,column=0)
txtCheese=Entry(f1, font=('arial', 16, 'bold'), textvariable=Cheese_Burger, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtCheese.grid(row=5,column=1)

#------------------------------------------------Second Row-----------------------------------------#

labelDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", fg="Steel Blue", bd=10, anchor='w')
labelDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtDrinks.grid(row=0,column=3)

#----------------------

labelCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", fg="Steel Blue", bd=10, anchor='w')
labelCost.grid(row=1,column=2)
txtCost=Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtCost.grid(row=1,column=3)


#----------------------

labelService = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", fg="Steel Blue", bd=10, anchor='w')
labelService.grid(row=2,column=2)
txtService=Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtService.grid(row=2,column=3)

#----------------------

labelTax = Label(f1, font=('arial', 16, 'bold'), text="Tax", fg="Steel Blue", bd=10, anchor='w')
labelTax.grid(row=3,column=2)
txtTax=Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtTax.grid(row=3,column=3)


#----------------------

labelSubTotal = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", fg="Steel Blue", bd=10, anchor='w')
labelSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtSubTotal.grid(row=4,column=3)


#----------------------

labelTotal = Label(f1, font=('arial', 16, 'bold'), text="Total", fg="Steel Blue", bd=10, anchor='w')
labelTotal.grid(row=5,column=2)
txtTotal=Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bg="powder blue", bd=10, insertwidth=4, justify='right')
txtTotal.grid(row=5,column=3)


#----------------------

btnTotal=Button(f1, padx=8, pady=8, font=('arial', 16, 'bold'), text='Total', width=10, fg="Black", bg="powder blue", bd=8, command= Ref).grid(row=7,column=1)

btnReset=Button(f1, padx=8, pady=8, font=('arial', 16, 'bold'), text='Reset', width=10, fg="Black", bg="powder blue", bd=8, command= Reset).grid(row=7,column=2)

btnExit=Button(f1, padx=8, pady=8, font=('arial', 16, 'bold'), text='Exit', width=10, fg="Black", bg="powder blue", bd=8, command= qExit).grid(row=7,column=3)


root.mainloop()
