# This program prints Hello, world!
print('Hello, world!')







# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
   # Display the sum
   print('The sum of {0} and {1} is {2}'.format(num1, num2, add(num1,num2)))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
   
   
   
   

print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n")

lower = int(input("Enter lower number: "))
higher = int(input("Enter higher number: "))


i = 1
print("Even number below %d are" %higher)
while(i <= higher):
  if(i % 2 == 0):
    print(i)
  i = i+1
  
 
print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n")
  

print("Even number between %d and %d are" %(lower, higher)) 
for i in range(lower,higher):
	if(i % 2 == 0):
		print(i) 
 
for i in range(2,101,2):
  print(i) 
  
  
  
print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n") 
  

a = [1,2,3,4,5]
result=[]
for i in a:
  result.append(i*i)
print(result)
for i in result:
  print(i)
  
  

print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n")


a = [1,2,3,4,5]
result = [i*i for i in a]
print(result)
for i in result:
  print(i)




print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n")






def square(k):
  return(k*k)
  
a = [1,4,3,4,5]
result=[]
for i in a:
  result.append(square(i))
print(result)
for i in result:
  print(i)

print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n")


def square(k):
  return(k*k)
  
a = [1,5,6,4,5]
result=[]
result=map(square,a)
print(result)
for i in result:
  print(i)
  
  
  
print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n")


a = [1,10,5,8,15]
result=[]
result=map(lambda k:k*k , a)
print(result)
for i in result:
  print(i)
  

print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n")

 

eve_no=filter(lambda k:k%2==0, range(2,101))
print("Even Nos are")
for i in eve_no:
  print(i)
  
  
  
  
  
print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n")


  
import  functools
my_list = [20,5,15,10,1]

print(my_list)
print("\n")
sum_list = functools.reduce(lambda x,y:x+y, my_list)
print("sum of list is %d" %sum_list)
print("\n")
product=functools.reduce(lambda x,y:x * y , my_list )
print("Product of list is %d" %product)
print("\n")
print("Sum of list is %d" %sum(my_list))
print("\n")
max_val=functools.reduce(lambda x,y:x if(x>y) else y , my_list )
print("Maximum number in list is %d" %max_val)
print("\n")
print("Maximum number in list is %d" %max(my_list))
print("\n")
print("Minimum number in list is %d" %min(my_list))






print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n")








#from __future__ import print_function
for i in range(0,6):
  for j in range(0,i+1):
    print("* ", end=' ')
  print("\r")
  
  
print("\n")
print("------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------")
print("\n")



