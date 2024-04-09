# ALL PYTHON PRACTICALS:

# printing the messages 

print("hello")
print("welcome")

# adding the 2 numbers .

num=45
print("this number is :" , num)
num=10
num1=20
result = num+num1
print(result)

#  adding decimal numbers .

num=10.20
num1=20.30
result = num+num1

#  adding two strings .

name="ram"
name1="reetu"
result=name+name1
print(result)

#  adding the 2 numbers by taking the user input .

num=input("enter the 1st number :")
num1=input("enter the 2nd number : ")
reult=num+num1
print(result)

# printing a single word.

print("hello")

#  if else condition example .

if 10%2==0:
    print("even number")

if 11%2==0:
    print("even number")

else:
    print("odd number") 

if 11%2==0: 
    print("even number")
else:
    print("odd number")

#  if  else condition by taking the user input .
    
num=int(input("enter the number to check :"))
if num%2==0:
    print("even number")
else:
    print("odd number") 

# if else condition example .
    
per=int(input("enter the percentage :"))
if per>60:
    height=int(input("enter te height : "))
    if(height>=5):
        print("eligible for training ")
    else:
        print("not eligible for training")
else:
    print("not qualified")

#  if elif else condition example . 
    
per=int(input("enter the percentage :"))
if per>=90:
    print("a+ grade")
elif per>=70 and per<90:
    print("a+ grade")
elif per>60 and per<70:
    print("b+ grade")
elif per>=45 and per<60:
    print("b grade")
elif per>=34 and per<45:
    print("c grade")
else:
    print ("fail") 

#  if elif else condition example . 
    
per=int(input("enter the per :"))
if per>=100:
    print("invalid")
elif per>=70 and per<90:
    print("a+ grade")
elif per>60 and per<70:
    print("b+ grade")
elif per>=45 and per<60:
    print("b grade")
elif per>=34 and per<45:
    print("c grade")
else:
    print ("fail") 


#  if elif else condition example . 

# Write a programs for discount available in super market
    
amount=int(input("enter the amount :"))
if amount>=65000:
    print("25% discount")
elif amount>=50000 and amount <65000:
    print("20% discount")
elif amount>=89000 and amount<4500000:
    print("10% discount")
else:
    print("no discount") 

#  if condition with operator example .

# Write a programs to find out the no of notes present on given amount 
    
depositamt=int(input("enter the amount :"))
if depositamt%2000==0 or depositamt%500 or depositamt%200 or depositamt%100:
    notes_2000 = depositamt/2000
    notes_500 = depositamt/500
    notes_200 = depositamt/200
    notes_100 = depositamt/100
    print("2000 notes :",notes_2000)
    print("500 notes :",notes_500)
    print("200 notes :",notes_200)
    print("100 notes :",notes_100)  

#  if elif else condition example .
    
per = int(input("enter the percentage : "))
if per>=90 and per<=100:
    print("a+ grade")
elif per>0 and per<35:
    print("pass")
else:
    print("invalid percentage") 

# for condition example .
    
num=int(input("enter a number :"))
for i in range(1,11):
    result=num*i
    print(num,"x",i,"=",result) 

#  if else condition example .
    
amount=int(input("enter a amount : "))
if amount%100==0:
    print("valid amount")
    if amount>=2000:
        nonotes = int(amount//2000)
        print("2000 no notes : ", nonotes)
    if amount>=500:
        nonotes=int(amount/500)
    amount=amount%500

    print("500 no notes :",nonotes)
else:
    print("invalid amount") 

# for condition example . 
    
num=int(input("enter a number :"))
for i in range(1,num):
    print(i)

    num=range()
    print(num)

# range function example . 
# example 1 : 

num=range(5)
print(num)

num=range(5)
print(num)

# example 2: 

for i in range (0,10):
    print(i)

num=range(5) 

#  printing reverse order .
# example 1 : 

num=range(5)
print(num)
for i in range (10,0,-1):
    print(i)

# example 2:

for i in range (0,5):
    print(i)

# example 3 : 

for i in range(1,11):
    if i%2==0:
        print(i) 
# example 4:

for i in range(1,11):
    if i%2==0:
        print(i)

# example 5:

for i in range(0,5):
    print("hello")

#  enter multiplication table of given number .
    
num=int(input("enter a number :"))
for i in range(1,10):
    result=num*i
    print(num,"x",i,"=", result) 

#  giving the format of the multiplication tbale to be displayed .
    
table=int(input("enter a number :"))
for i in range (1,11):
    print(table,"x",i,"=",table*i) 

#  if else condition example .
    
num=int(input("enter a number :"))
if num%2==0:
    print("even number")
else:
    print("odd number")

#  printing the multiplication table in the given format.
    
for i in range (1,11):
    print(f"multiplication table for {i}:")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}") 

#  displaying stars in ***** order .
        
num_times=5
print("*"*5)

# displaying stars in ************************* order .

num=25
print("*"*25) 

#  displying the sum of numbers in a given range by incrementing 1.

sum=0
for i in range(1,6):
    sum=sum+1
    print("the sum is :",sum) 

# write a program to find out the factorial and input given by user .

num=int(input("enter a number : "))
factorial = 1

if num<0:
    print("factorial of negative number is not possible")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*1
print("the factorial of ",num,"is",factorial)

# adding the 2 numbers .

a=10
b=20
b=b-a
a=a+b
print(a,b) 

# adding 2 numbers without using 3rd variable .

a=100
b=200
b=a-b
a=a-b
print(a,b)

result=1
for i in range(5,1,-1):
    result=result*1
print(result)  

# find the squares from 1 to 5 .

num=0
for i in range(1,6):
    num=i*1
    print(num) 

# swapping a and b using 3rd variable.

a=100
b=250
c=b
b=a
a=c
print(a)
print(b) 

# swapping a and b values without using 3rd variable.
# format of swapping without using 3rd variable.
# the formuls or format is given below:

# b=b-a 10-7=3
# a=a+b 7+3=10
# b=a-b 10-3=7
# print(a)
# print(b) 

# find the sum from 1 to 5.

sum=0
for i in range(1,6):
    sum=sum+i
print("the sum is :", sum)

#  count function example .

num=int(input("enter a number :"))
count=0
for i in range(1,num):
    if i%7==0:
        count=count+1
print(count) 

# while loop example.

# while condition()
# print()

num=1
while num<11:
    print(num)
    num=num+1  

# write a python program to find numbers whic are divisible by 7 and multiplies of 5 between 1500 and 2700 bot include .

for i in range(15000,2700):
    if i%7==0:
        print(i) 

# write a python program to guess a number between 1 to 9. 
            
num=0
for i in range(1,9):
    num=i*1
    print(num)  
    
# write a python program that iterates the integers from 1 to 50 , for multiplies of 3 print "fizz".print

for i in range(1,51):
    if i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    elif i%3==0 and i%5==0:
        print("fizz buzz") 

# find the given number is prime or not?
        
if num>1:
    for i in range (2,num+1):
      for j in range(2,num+1):
         if i%j==0:
             break
      if i==j:
         print("prime number")
    else:
         print("not prime") 

# swap 2 numbers without using 3rd variable.

a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b) 

# write a python program to find numbers between 100 and 400 both included  where each digit or number is the even number .
# the number obtained ahould be printed in the comma seperated sequence.
         
for i in range (100,400):
    if i%2==0:
        print(i)  

# calculate the sum from 1 to given number .
     
sum=0
for i in range(1,6):
    sum=sum+i
    print("the sum is :",sum)  
    
for i in range(1,4):
    for j in range(1,5):
        print("1",end="")
    print()    

#  displaying 5 rows of stars in the below order .
# * 
# * *
# * * *
# * * * *
# * * * * *

rows = 5
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r" ) 

# write a python program to find numbers between 100 and 400 both included  where each digit or number is the even number .
# the number obtained ahould be printed in the comma seperated sequence.

for i in range(100,400):
    d1=i%10
    temp1=int(i/10)
    d2=temp1%10
    temp2=int(temp1/10)
    if d1 ==0 or d1==2 or d1==4 or d1==6 or d1==8:
        if d2==0 or d2==2 or d2==4 or d2==6 or d2==8:
            if temp2==0 or temp2==2 or temp2==4 or temp2==6 or temp2==8:
                print(i,end=" ")  

#  displaying the blank space.

for i in range(5,1,-1):
    for j in range(1,i,-1):
        print(j,end=" ")
    print()  

# displaying the numbers in reverse order.

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()   

#  displaying the number in aranged order .
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 - in this order 

for i in range(1,4):
    for j in range(1,5):
        print(j,end=" ")
    print() 

#  1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5  - display the numbers in this order .

for i in range(1,5):
    for j in range(1,6):
        print(j,end=" ")
    print()  

# displaying the stars in arranged order .
#  * * * * * 
# * * * * *
# * * * * *
# * * * * *
    
for i in range(1,5):
    for j in range(1,6):
        print("*",end=" ") 
    print()  

# displaying the number as 123 , 12 , 1
#  123
# 12
# 1
    
for i in range(3,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()  

#  displaying the numbers in 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()  

#  displaying the numbers as 
# 1 2 
# 1 2
# 1 2
# 1 2
# 1 2

for i in range(5,0,-1):
    for j in range(1,2+1):
        print(j,end=" ")
    print()   

#  displaying the numbers of stars by enetring number .

num=int(input("enter number :"))
for i in range(num):
    for j in range(num):
        if i==0 and j==0:
            print("*" , end=" ")
        else:
            print("",end=" ")

    for k in range(num):
        if i==0 and k==num-1:
            print("*" , end=" ")
        else:
            print("",end=" ")

    for i in range(num):
        for j in range(num):
            if i==num-1 and j==0:
             print("*" , end=" ")
        else:
            print("",end=" ")

    for k in range(num):
        if i==num-1 and k==num-1:
            print("*" , end=" ")
        else:
            print("",end=" ")
    print()  

#  using for if elif condition .

for i in range(1,6):
    for j in range(1,6):
        if i==1 and j==1:
            print("*", end=" ")
        elif i==1 and j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        print()  

# reverse the given string .

name = input("enter a number : ")
for i in name [::-1]:
    print(i,end=" ") 

# take email id from a user to check special characters are present or not.
    
    email_id = input("enter email id : ")
    if("@" in email_id):
        print("email id is valid")
    else:
        print("email id is not valid")  

# find vowels in ow many times they are in the given list .

name = input("enter name : ")
vowel=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in name:
    if i in vowel:
        count+=1
print(count)  

#  using append method 

list=[656,58,26,58,58,88,58]
print(len(list)) 

list=[]
l=int(input("enter the no of elements : "))
for i in range(1):
    num=int(input("enter the elements :"))
    list.append(num)
print(list) 

# take input from user , only even number should be appended.

list=[]
length=int(input("enter the number of elements : "))
for i in range(length):
    num=int(input("enter the element : "))
    if num%2==0:
        list.append(num)
print(list)  

# take input from user , duplicate elements should not be added .

list=[]
length=int(input("enter the number of elements : "))
for i in range(length):
    num=int(input("enter the element : "))
    if num not in list:
        list.appenf(num)
print(list) 

# displaying the set.

set={45,58,55,258,555}
print(set) 

# printing the items of dictionary.

dic={"id":1009,"name":"ankita"}
print(dic["id"]) 

# taking multiple values and printing the items of dictionary .

dic={"id":1009,"name":"ankita","desig":"data scientist"}
print(dic["desig"])  

# displaying dictionary in list .

list=[{"id":1009,"name":"ankita","desig":"data scientist"}]
print(list)
for key in dic.items():
    print()  

# find out the area of circle.
    
rad=float(input("enter the radius : "))
def areaof_circle(rad):
    a=3.14*rad*rad
    areaof_circle(rad)
    print(areaof_circle(rad))  

# find out the area of rectangle.
    
def area(length , breadth):
        return length*breadth
length=int(input("enter the length of rectangle in cms : "))
breadth=int(input("enter the breadth of rectangle in cms : "))

result=area(length , breadth)
print(result)  

# constructing a class.

class employee:
    def __init__(self):
        print("constructor")
emp=employee()   

#  displaying the numbers in 
# 1 2 3 
# 1 2
# 1  in this order 

for i in range(3,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 

# displaying the stars in 
# 1  
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15 
# order 

count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()  

# length method is used to print the length of the string .
# length always starts from 1 
# index always starts from 0.

# displaying length of msg.

msg=("ankita mishra")
print(len(msg)) 

# print numbers from 1 to 10 using function.

def loop(num):
    if num<=10:
        print(num)
        loop(num+1)
    loop(1) 

# adding 2 numbers .
    
def add (num1,num2):
        return num1+num2
result=add(10,20)
print(result)  

# displaying the numbers printing in loops.

def loop(*num):
    for i in num:
        print(i)
loop(1,2,3,4)
loop(1,2)
loop(1,2,3)

# pass the list in loop , single * star is used .

def loop(*num):
    for i in num:
        print(i)
list=[5,5,2,85,5,5]
loop(*list) 

# pass the dictionary in loop , double ** star is used .

def loop(**karg):
    for i,j in karg.items():
        print(i,j)
    dic={"id":1009,"name":"ankita","desig":"data scientist"}
    loop(**dic)  

# list comprehension 

list=[]
n=5
i=1
count=2
sum=0
list=[]
str1=""
for i in range(1,n+1):
    str1=str1+str(count)
    list.append(str1)
listsum=0
for i in range(len(list)):
    print(list[i],"+",end=" ")
    listsum=listsum+int(list[i])
print("=",listsum)   

# displaying the sentence in arranged order .

msg="india is my country"
msg=msg.split("n-1")
for i in msg:
    print(i)  

#  displaying the senetnce in reverse order .
    
msg="india is my country"
msg=msg.split(" ")
for i in msg[::-1]:
    print(i,end=" ") 

# joining both te arranged order and the reverse order sentence.
    
msg="india is my country"
new_line= " ".join(msg.split()[::-1])
print(new_line) 

# creating parent class

class person:
    def persondata(self):
        print("person name : sam")

    def persondata(self):
        print("person age : 28")  

# creating child class
        
class employee(person):
    def employeesalarydetails(self):
        print("employee salary : 45000")
emp=employee()
emp.persondata()
emp.personagedetails()
emp.employeesalarydetails()  

#  using filter method .

num=[52,85,885,889,588,58,5,48,22,15,6]
def even(n):
    return n%2==0

new_list=list(filter(even, num))
print(new_list)

new_list=list(filter(lambda x:x%2==0 , num))
print(new_list)

new_list=list(map(lambda x:x%2==0 , num))
print(new_list) 

# reduce method .

# method 1 : 

import functools
list=[57,58,258,6]
sum=functools.reduce(lambda x,y:x+y,list)
print(sum) 

# method 2 : 

from functools import reduce
list=[57,58,258,6]
sum=functools.reduce(lambda x,y:x+y,list)
print(sum) 

# both the above methods will give the same answer 

# displaying country my is india - in this order 

msg="india is my country"
msg1=msg.split(" ")
msg1.reverse()
for i in msg1 :
    print(i) 

#  file handling 
    
    file =open(r"path of the file from to be copied")
    data=file.read()
    file =open(r"path of the file where to be copied")
    data=file.write(data)
    file.close() 
    
# discount example : 

purchase_Amt= float(input("enter Amount: "))
if purchase_Amt>=150:
    if purchase_Amt>=450:
        discount=0.2
        if purchase_Amt>=1500:
            discount=0.3
    else:
        discount=0.1
    discounted_Amt=purchase_Amt
    (purchase_Amt*discount)
    print("apply doiscount : ",discount*100)
    print("dicounted Amt : ",discounted_Amt)
    print("wavier : ",purchase_Amt*discount)
else:
    print("No dicount applied for purchases below 150") 

# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
# (ans):

for i in range (1500,2701):
            if i%7==0 or i%5==0:
               print(i)

# Write a Python program to guess a number between 1 and 9.
# (ans):
               
num=int(input("enter no. : "))
for i in range(1,10):
       if num==i:
          print(num,"true")
          break
       else:
           print(num,"false")

# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
# For numbers that are multiples of three and five, print "FizzBuzz".
# (ans):
           
for num in range (1,51):
          if num%3==0 and num%5==0:
             print("FizzBuzz")

          elif num%3==0:
             print("Fizz")
  
          elif num%5==0:
             print("Buzz")

          else:
             print(num,"= not divisible by 3 and 5 ")
   

# find the given number is prime or not?
# (ans):
num = int(input("Enter the no. : "))
if  num>1:
           for i in range (2,num):
             if num%i==0:
               print(num, "= is not a prime no. ")
               break
           else:
             print(num,"= ia a prime no. ")
             else:
         print("It is not a prime no. ")
        
         
     
# swap 2 number without using thied variable?
# (ans):
   
a=23
b=45
a=b+a 
b=a-b 
a=a-b 
print(a,b)


# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number (ans):
for num in range(100,401):
       all_even_digits=all(int(digits)%2==0 for digits in str(num))
       if all_even_digits:
         print(num,"- are even digits ")
         
# The numbers obtained should be printed in a comma-separated sequence.

# calculate sum from 1 to given number (ans):?

number= int(input("enter given no. "))
num=0
for i in range(1,number+1):
      num=  num+i
      print(num)

#  by using for condition .

for i in range(100,401):
    if i%2==0:
        print(i) 

# by using single if else condition .

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 and j == 1 or i == 1 and j == 5 or i == 5 and j == 1 or i == 5 and j == 5:
            print("*", end=" ")
        else:
            print(" ", end="")
    print() 

# Enter only Even Items

list=[]
l=int(input("Enter the no of elements:"))
for i in range(l):
    item=int(input("Enter the Nos:"))
    if item%2==0:
        list.append(item)
print(list)

# Enter only Unique Items

list1=[]
l=int(input("Enter the no of elements:"))
for i in range(l):
    item=int(input("Enter the Nos:"))
    if item not in list1:
        list1.append(item)
    else:
        print(" Item no", i, "already exists")
print(list1) 

# print list having only even no.

list=[]
l=int(input("enter the size of list: "))
for i in range(l):
    numbers=int(input("enter the number: "))
    if numbers%2==0:
        list.append(numbers)
        print(list)
print(list)

# print list having no duplicate values

list1=[]
l1=int(input("enter the size of list: "))
for i in range(l1):
    num1=int(input("enter the numbers: "))
    if num1 not in list1:
        list1.append(num1)
        print(list1)
print(list1)

# to find area of circle.

rad=float(input("enter the radius: "))
def areaof_Circle():
    A=3.14*rad*rad
    print("Area of circle = ", A)
areaof_Circle()

# to find area of rectangle.

l=float(input("enter the length of rectangle: "))
b=float(input("enter the breadth of rectangle: "))
def areaof_rectangle():
    A2=l*b
    print("Area of rectangle = ", A2)
areaof_rectangle()

# to fetch address from telephone directory
# telephone_directory={"8652529551":"kk" ,"8828521322": "ghansoli","9594502700":"mulund","9833217353":"Vashi","8652657202":"bhandup"}
# print(dic)

def get_addressBy_telephone(telephone):
    address=telephone_directory.get(telephone)
    print(address)
telephone=input("enter the telephone no ")
print("the address for ",telephone, "is")
address=get_addressBy_telephone(telephone) 

# to fetch updated address from telephone directory
# telephone_directory={"8652529551":"kk" ,"8828521322": "ghansoli","9594502700":"mulund","9833217353":"Vashi","8652657202":"bhandup"}

telephone_directory={"8652529551":"kk" ,"8828521322": "ghansoli","9594502700":"mulund","9833217353":"Vashi","8652657202":"bhandup"}
def get_addressBy_telephone(telephone):
    address=telephone_directory.get(telephone)
    print(address)
    def updated_address_by_telephone(telephone,new_address):
       new_address=telephone_directory.get(telephone)
       print(new_address)
       if telephone in telephone_directory:
          print("address for ",telephone, "updated successfuly")
       else:
          print("telephone not found in directory",telephone)
    if telephone not in telephone_directory:
       print("No telephone found in directory or invalid number")
    else:
       new_address=input("enter new address ")
       print("updated address for", telephone, "is" , new_address, "in telephone directory")

telephone=input("enter the telephone no ")
get_addressBy_telephone(telephone)

#  creating a list in dictionary .

student_list=[{"id":101,"Name":"Vaibhav","Course":"Data Science"},{"id":102,"Name":"Dipali","Course":"python"},{"id":103,"Name":"Divit","Course":"Java"},
      {"id":104,"Name":"Sangram","Course":"Tester"},{"id":105,"Name":"Vidya","Course":"ML Engineer"}]
for student in student_list:
    course=student["Course"]
    if course in ["Java" , "python"]:
        print(student , course)

#  print 1 to 10 without using loop.
        
def print_numbers(n):
    if n<=10:
        print(n)
        print_numbers(n+1)
print_numbers(n=1) 

# Find the factorial of number using lambda function

num=int(input("enter the number: "))
fact=lambda num: 1 if num==0 else num*fact(num-1)
print(fact(num))

#  write a program to calculate a sum of series upto n term, for example if n=5 the series will become  2+22+222+2222+22222 = 24690

n=5
series_sum=0
term=2
for i in range(1,n+1):
    
    series_sum+=term
    term=term*10+2
      
print("2+22+222+2222+22222 = ",series_sum)

n=int(input("Enter the no: "))
Sum=2*((10*(n+1))-10-9*n)/81
print(Sum) 

# reapeated charters and number of occurance.

string="aa bbbb c dd eeeee"
string=string.lower()
chars={}
count=0
for char in string:
    if char not in chars:
        chars[char]=1
    else:
        chars[char]+=1
for char in chars:
    count=string.count(char)

    if count>1:

        print(char,count) 

# What will be the output of the following Python code?

x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)

# [‘ab’, ‘cd’]

# What will be the output of the following Python code?

x = ['ab', 'cd']
for i in x:
    x.append(i.upper())
print(x)

# none of the mentioned


#  What will be the output of the following Python code?

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
 
    i + = 1

# error

#  What will be the output of the following Python code?

i = 1
while True:
    if i%0O7 == 0:
        break
    print(i)
    i += 1

# 1 2 3 4 5 6

#  What will be the output of the following Python code?

i = 5
while True:
    if i%0O11 == 0:
        break
    print(i)
    i += 1

# 5 6 7 8

#  What will be the output of the following Python code?

i = 5
while True:
    if i%0O9 == 0:
        break
    print(i)
    i += 1

# error

#  What will be the output of the following Python code?

i = 1
while True:
    if i%2 == 0:
        break
    print(i)
    i += 2

#  1 3 5 7 9 11 …

#  What will be the output of the following Python code?

i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2

# 2 4

#  What will be the output of the following Python code?

i = 1
while False:
    if i%2 == 0:
        break
    print(i)
    i += 2

# none of the mentioned

#  What will be the output of the following Python code?

True = False
while True:
    print(True)
    break

# none of the mentioned

# creating the class.

class Employee:
    def empdata(self):
        print("employee method")
emp=Employee()
emp.empdata() 

#  using print function .

print("hello")

# printing hello world

str='hello world'
print(str) 

# displaying length of the list.

list=[58,56,215]
print(len[list]) 

list[85,25,597]
print(len[list]) 

#print('hello world')

# print is a function in python , print is used to print the data we want to be displayed.

# using time function .

import time

time.sleep(2)
print('2 seconds have assed since this program ran') 

# creating tuple.

tuple=(43,25,87,48) 
for i in tuple:
    print(i) 

# defining function .
    
def fun():
    def game():
     print("this is game")
     game()
     fun() 

#  creating class.
     
class person:
    def persondate(self):
        print("person name:ramesh")
    def presonagedetail(self):
        print("age : 23")
class employee(person):
    def employeesalarydetails(self):
        print("employee salary:10000")
emp=employee()
emp.persondate()

# using print function.

print("hello")
print("welcome")
num=45
print("this number is : " ,num)

# printing multiple factors by taking user input.

print("hello")
print("welcome")
num=45
print("tis number is:" ,num)
num=10
num1= 20
result = num+num1
print (result)
num=10.20
num1=20.30
result=num+num1
name="ram"
name1="reetu"
result=name+name1
print(result)

name=input("enter the name : ")
print(name)

num=input("enter the first number")
num1=input("enter te second number : ")
result=num+num1
print(result)

num=input("enter the first number")
num1=input("enter te second number : ")
result=int(num)+int(num1)
print(result)

num=10.50
num1=10
result = num+num1
print(result)

#  taking the multiple variables.

num1=input("enter the first number")
num2=input("enter te second number : ")
result=int(num1)+int(num2)
print(result)

print("hello")

# if else condition .

if 10%2==0:
    print("even number")

if 11%2==0:
    print("even number")

    if 11%2==0:
        print("even number")
    else:
        print("odd number") 

# if else condition .

num=int(input("enter the number to check :"))

if num%2==0:
    print("even number")
else:
    print("odd number")

# if else condition : 

num=int(input("enter te account number to check"))

if num>8:
    print("account number")
else:
    print("the account number is less than 8 digits") 

# if else condition :
    
if num>99999 and num<10000000:
    print("login")
else:
    print("invalid account number")

# if else condition by taking the user input .

per=(input("enter the percentage :"))
if per>=60:
    height=int(input("enter te height :"))
    if(height>=5):
        print("eligible for training")
    else:
        print("not eligible for training")
else:
    print("not qualified")

print("hello")

#  if else condition by taking the user input .

per=(input("enter the percentage :"))
if per>=60:
    height=int(input("enter te height :"))
    if(height>=5):
        print("eligible for training")
    else:
        print("not eligible for training")
else:
    print("not qualified")

# if else elif condition .

    per=int(input("enter the percentage :"))
if per>=60:
    height=int(input("enter te height :"))
    if(height>=5):
        print("eligible for training")
    else:
        print("not eligible for training")
else:
    print("not qualified")

# if elif else condition :

    per=int(input("Enter the percentage:"))
    if per>=90:
        print("A+ Grade")
    elif per>=70 and per<90:
        print("a grade")
    elif per>=60 and per<=70:
        print("b+ grade")
    elif per>=45 and per<=60:
        print("b grade")
    elif per>=35 and per<=45:
        print("b grade")
    else:
        print("fail")
    
# notes example : 

amount=int(input("enter the amount :"))
if amount%100==0:
    print("valid amount")
    if amount>=2000:
        noNotes=int(amount//2000)
        amount=amount%2000
        print("2000 no notes  : " , noNotes)
if amount>=500:
    noNotes=int(amount/500)
    amount=amount%500
    print("500 no notes : " , noNotes)
if amount>=200:
   noNotes=int(amount/200)
   amount=int(amount%200)
   print("200 no notes : " , noNotes)
if amount>=100:
    noNotes=int(amount/100)
    amount=int(amount%100)
    print("100 no notes : " , noNotes)
else:
    print("invalid amount")

# using range function : 

num=int(input("enter the number : "))
for i in range(1,num):
        print(i)
        num=range()
        print(num)

# printing range of 5 : 
# example 1 : 

num=range(5)
print(num)

# example 2 : 

num=range(5)
print(num)
for i in range(0,10):
    print(i)

# example 3 : 

num=range(5)
print(num)
# (0,10,2) - means it will print from 1to 10 with the increament of 2.
for i in range(0,10,2):
    print(i)

# example 4 : 

num=range(5)
print(num)
# it will print in the reverse order from 10 to 0.
for i in range(10,0,-1):
    print(i)

# example 5 : 

for i in range(0,5):
    print(i)

# example 6 : 

for i in range(0,5):
    print("Hello")

# example 7 : 

for i in range(1,11):
    if i%2==0:
        print(i)
# example 8 :

for i in range(1,11):
    if i%2==0:
        print(i)
#  example 9 :

for i in range(0,5):
    print("Hello")

# displaying multiplication table : 

# example 1 : 

num=int(input("enter the number : "))
for i in range(1,10):
    result=num*i
    print(num,"x",i,"=",result)

# example 2 :

table=int(input("enter the number"))
for i in range(1,11):
    print(table,"x",i,"=",table*i)

# printing range :

# example 1 :

# write a program to print 
# 1234
# 1234
# 1234 - in this order 
    
for i in range(1,4):
    for j in range(1,5):
        print(j , end="")
    print() 

# example 2 :
# write a program to print 1
# 2
# 3
# 4
# 5
# 6
# 1
# 2
# 3
# 4
# 5
# 6 - in this order.

for i in range(1,5):
    for j in range(1,7):
     print(j , end="")
     print() 

# example 3 :
#  write a program to display 1234
# 1234
# 1234
# 1234 - in tis order .

for i in range(1,5):
    for j in range(1,5):
        print(j,end="")
    print() 

# example 4 :
# write a program to display 
# 1
# 12
# 123
# 1234 - in this order.

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end="")
    print() 

# example 5 :
#  write a program to display 
# 1
# 2
# 3
# 1
# 2
# 1 - in this order .

for i in range(3,0,-1):
    for j in range(1,i+1):
        print(j,end="")
        print() 

# example 6 :
#  write a program to display
# 1
# 12
# 123
# 1234 - in this order.
        
for i in range(1,5):
    for j in range(1,i+1):
        print(j , end="")
    print()

# example 7 :
#  write a program to display 
# 123
# 12
# 1 - in this order.

for i in range(3,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print() 

# example 8 :
#  write a program to display 
# 12345
# 1234
# 123
# 12
# 1 - in tis order.

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print() 

# example 9 :
#  write a program to display 
# 543
# 54
# 5 - in this order .

for i in range(1,6):
    for j in range(5,i+1,-1):
        print(j, end="")
    print() 

# example 10 :
#  write a program to display 
# 54321
# 5432
# 543
# 54
# 5 - in this order .

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j, end="")
    print() 

# example 11:
#  write a program to display 
# 654321
# 65432
# 6543
# 654
# 65 - in this order.

for i in range(1,6):
    for j in range(6,i-1,-1):
        print(j,end="")
    print() 

# example 12 :
#  write a program to display 
# 1
# 12
# 123
# 1234 - in this order.

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print() 

# example 13 :
#  write a program to display 
# 12345
# 1234
# 123
# 12
# 1 - in this order.

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# example 14 :
#  write a program to display 
# 1
# 12
# 123
# 1234 - in this order.

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()

# example 15:
#  write a program to display 
# 1234
# 123
# 12
# 1 - in this order.

for i in range (4,0,-1):
    for j in range(1,i+1):
       print(j,end="")
    print() 

# example 16:
#  write a program to display 
# 12345
# 1234
# 123
# 12
# 1 - in this order.

for i in range (5,0,-1):
    for j in range(1,i+1):
       print(j,end="")
    print() 

# example 17:
#  write a program to display 
# 1
# 2
# 3
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
# 5 - in this order.

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
        print() 

# example 18:
#  write a program to display 
# 12345
# 1234
# 123
# 12
# 1 - in this order.

for i in range (5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# example 19:
#  write a program to display 
# 12345
# 1234
# 123
# 12
# 1 - in this order.

for i in range (5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print() 

# example 20:
#  write a program to display 
# 123
# 12
# 1 - in this order.

for i in range (5,0,-1):
      for j in range(1,i-1):
        print(j,end="")
      print()

# example 21:
#  write a program to display 
# 123
# 12
# 1- in this order.
      
for i in range (5,0,-1):
       for j in range(1,i-1):
        print(j,end="")
       print() 

# example 22:
#  write a program to display 
# 54321
# 5432
# 543
# 54
# 5 - in this order.

for i in range(1,6):
    for j in range(5,i-1,-1):
                   print(j,end="")
    print()

# example 23:
#  write a program to display 
# 54321
# 5432
# 543
# 54
# 5 - in this order.

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print() 

# example 24:
#  write a program to display 
# 11111
# 2222
# 333
# 44
5 - in this order.

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i,end="")
    print() 

# example 25:
#  write a program to display 
# 0
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1 - in this order.

count=0
for i in range(1,6):
    for j in range(1,i+1):
        print(count)
        count=1 
    print

# example 26:
#  write a program to display 123456789101112131415
    
count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(count, end="")
        count+=1
    print

# example 27:
#  write a program to display 
# 1
# 11
# 111
# 1111
# 11111 - in this order.

count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(count,end="")
        count=1
    print() 

# example 28:
#  write a program to display 
# 1
# 23
# 456
# 78910
# 1112131415 - in this order.

count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(count,end="")
        count+=1
    print()

# printing the string .

str='hello world'
print(str)

str= "india is my country"
print(str) 

str="hello world"
print(str)

str= "india is my \n"
print(str)

msg="hello"
msg1="world"
msg2 = "thank you"
print(msg+msg1+msg2)

str='hello'*3
print(str)

# check wheather the letters are  present in the word or not.

msg="itvedant intitute"
print("it" in msg)

msg1="itvedant institute"
print("it" in msg1)

msg1="itvedant institute"
print("de" in msg1)

msg1="itvedant institute"
print("de" not in msg1)

print(msg[9])
print(msg[12])
print(msg[4])
print(msg[-6])
print(msg[-13])
print(msg[-20]) 

msg="itvedant institute"
print(len(msg))

#  it will print the entire message.

print(msg[:])

#  display the range of letters from the message.

msg="itvedant institute"
print(msg[1:9])

print(msg[1:11])

print(msg[4:8])

print(msg[2:])

print(msg[:8]) 

# performing various colon operations 

msg='hello world'
print(msg[-1:-4]) 

msg='hello world'
print(msg[-4:-1]) 

msg='hello world'
print(msg[0:-1])  

msg='hello world'
print(msg[:-1]) 

msg='hello world'
print(msg[-1:]) 

msg='hello world'
print(msg[::-1]) 

msg='itvedant institute'
print(msg[::-1]) 

msg='itvedant institute'
print(msg[:]) 

str="hello world"
print(str)
print(str.rstrip())

str="hello world"
print(str)
print(str.lstrip()) 

str="hello world"
print(str)
print(str.strip()) 

str= "hello world"
print(str.upper())

str= "hello world"
print(str.lower())

str= "hello world"
print(str.capitalize())

str= "hello world"
print(str.swapcase())

#  write a program to display the number of vowels by takig the user input .

name=input("enter the name")
vowel=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in name:
   if i in vowel:
       count+=1
print(count) 

#  performing various operations on msg.

msg="ABC123"
print(msg.isalnum()) 

msg="ankita"
print(msg.isalpha()) 

msg="5489"
print(msg.isdecimal())
msg="5"

print(msg.isdigit())
msg="demo" 

msg="ankita"
print(msg.islower()) 

msg="ankita"
print(msg.isupper())

msg="ANKITA"
print(msg.isupper()) 

msg="ANKitA"
print(msg.isupper())  

msg="ANKITA1999"
print(msg.isnumeric())

msg="1999"
print(msg.isnumeric())

msg="\nabc"
print (msg)
 
msg="\name"
print(msg.isprintable()) 

msg=" "
print(msg.isspace())

msg="Ankita"
print(msg.istitle()) 

msg="My name is Ankita Mishra"
print(msg.istitle()) 

msg="Ankita"
print(msg.istitle()) 

# performing various operations on list.

list=[10,15,53,29.32,"apple"] 
print(list) 

list=[10,15,53,29.32,"apple"]
print(list[0]) 

list=[10,15,53,29.32,"apple"]
print(list[3])  

list=[10,15,53,29.32,"apple"]
print(list[2])

list=[10,15,53,29.32,"apple"]
print(list[1])  

list=[10,15,53,29.32,"apple"]
print(list[-1]) 

list=[10,15,53,29.32,"apple"]
print(list[-2]) 

list=[10,15,53,29.32,"apple"]
print(list[-3])  

list=[10,15,53,29.32,"apple"]
print(list[:])

list=[10,15,53,29.32,"apple"]
print(list[2:])

list=[10,15,53,29.32,"apple"]
print(list[-4:-2]) 

list=[10,58,258,45,89,258,63,20,58]
for i in list:
    print(i) 

list=[10,58,258,45,89,258,63,20,58]
for i in list:
    print(i) 

    list=[300]
    print("after update")
    for i in list:
        print(i)

#  write a program by using append method .
        
list=[10,58,258,45,89,258,63,20,58]
for i in list:
     print(i) 

     list.append(58)
     print("after update")
     for i in list:
         print(i)

list=[85,58,63]
print(len(list)) 

# using append method 

list=[]
l=int(input("enter the number of elements"))
for i in range(1):
    num=int(input("enter the elements"))
    list.append(num)

#  performing various operations on list by using different functions.
    
list=[85,25,98]
print(list)
list.insert(2,58)
print(list)

list=[85,25,98]
print(list.reverse()) 

list=[58,25,89,28]
list.reverse()
print(list)  

list=[89,25,52,79]
list.sort()
print(list)

list=[82,258,58596]
list.extend([58,25])
print(list) 

list=[58,45,58,23,29,75,25,69]
list.remove(69)
print(list) 

list=[85,25,89,26,247]
print(list)
copy_list=list.copy()
print(copy_list)

#  performing various operations on tuple.

tuple=(43,25,87,48) 
for i in tuple:
    print(i) 

tuple=(43,25,87,48) 
for i in tuple:
    print(i) 

#  performing various operations on set .
    
set= {12.47,45,78,45,58,96,78}
print(set) 

set.add(71)
print(set) 

#  performing various operations on dictionary .

dic={"id" :101,"name": "ramesh","salary":50000,"designation":"programmer"}
print(dic) 

dic={"id" :101,"name": "ramesh","salary1":50000,"salary2":50000,"designation":"programmer"}
print(dic) 

dic={"id" :101,"name": "ramesh","salary1":50000,"salary2":50000,"designation":"programmer"}
print(dic) 
print(dic["id"])

dic={"id" :[101,102],"name": "ramesh","salary1":50000,"salary2":50000,"designation":"programmer"}
print(dic) 

#  creating dictionary in list.

list=[{"id":101,"name":"ramesh"},{"id":102,"name":"reetu"}]
print(list) 

list=[{"id":101,"course":"java"},{"id":102,"course":"python"},{"id":103,"course":"net"}]
for i in range(len(list)):
     if i<2:
         print(list[i]) 

# write a program to create a dictionary with te keys and values.

# example 1  :
                
dic={"id" :101,"name": "ramesh","salary":50000,"designation":"programmer"}
print(dic)
for key in dic.items():
    print(key)
print()
for key,value in dic.items():
    print(key," " ,value) 
                                                    
dic={"python":["ram","vinita"],"java":["neena","meena"]}
for key,value in dic.items():
    if key=="python":
        print(key," ", value)

# example 2 :
        
dic={"id":101,"name":"ramesh"}
print(dic)
dic["name"] = "suresh"
print(dic) 

#  performing operations on def function .

def func():
    print("this is function")
func() 
func() 

def fun_1(id,name):
    print("id :",id)
    print("name :" ,name)

fun_1(101,"rahul") 

def fun_1(id,name):
    print("id :",id)
    print("name :" ,name)

id=int(input("enter the id:"))
name = input("enter the name :")
fun_1(101,"rahul")  

def fun():
     def game():
      print("this is game")
     game()
     fun() 

def loop(num):
    if num<=10:
       print(num)
       loop(num+1)
       loop(1)

# find out the area of circle.
       
def area(radius):
    pie=3.14
    area=pie*radius*radius
    print(area) 

def area(radius):
    return 3.14*radius*radius
num=area(5)
print(num) 

def add(num,num1):
    return num+num1
result=add(10,20)
print(result) 

# find out area of rectangle:

def area (length,breadth):
    return length*breadth

length=int(input("enter the lengt of rectangle : "))
breadth=int(input("enter the breadth of rectangle : "))

result= area(length,breadth)
print(result) 

# perfroming various operations by using def function.

def odd(num,num1):
    return num+num1
print(odd(10,20))

result=lambda num,num1 :num+num1
print(result(10,20)) 

msg=lambda:print("hello")
print(msg()) 

even=lambda x:x%2==0
print(even(10)) 

even=lambda x:x%2==0
print(even(105897)) 

def loop(num):
    print(num)
    loop(1)  

#  argument method OR args function 

def loop(*num):
    for i in num:
        print(i)
        loop(1,2,3,4)
        loop(1,2)
        loop(1,2,3,4,5) 

def loop(*num):
    for i in num:
        print(i)
        list=[4,58,259,148,25879,2248,225,1148,2147,52,125,58]
        loop(*list) 

def loop(**karg):
    for i,j in karg .items():
        print(i,j)
        dic={"id":101,"name":"ankita","salary":50000}
        loop(**dic) 

def add (num):
    return lambda x:num*x
result=add(10)
print(result(20))  

# class creation: 
 
class Employee():   
# class ka is employee
# defining fuction- 
    def empdata(self):  
# def is a method 
        print("employee method") 

emp=Employee() 
# object creation 

emp.empdata()
# calling the function using object 

def empname(self):
    print("employee name is: ramesh") 

class Employee:
     def __init__(self):
        print("Constructor") 
emp=Employee() 

# class creation

class person:
    def persondata(self):
        print("person name :ramesh ")
    def personagedetails(self):
        print("age : 25")
class employee (person):
    def employeesalarydetails(self):
        print("employee salary : 10000")
emp=employee()
emp.persondata()
emp.personagedetails()
emp.employeesalarydetails() 

# function overiding

class car:
    def cardetails(self):
         print("car name maruti")
         def speeddetails(self):
             print("80 per/km")
class maruti (car):
     def brandetails(self):
         print("maruti suzuki")
     def speedetails(self):
         print("90 per/km")
m=maruti()
m.cardetails()
m.brandetails()
m.speedetails()  

# function overloading
# what is polymorphism?
# overriding is possible in python , parent and child function havimg same name and function.
# overloading - it takessame name with different parametres.
# same name - different parametres.

# self - self refer current class object.

list=[10,15,18,13,12,7,48,80]
newlist=[]
for i in list:
     if i%2==0:
         newlist.append(i)
         print(newlist)

# filter - it contains 2 parametres 
#  1st - includes numbers
# 2nd parameter - it will call function 
# filter method is used to filter the data from te list  on te basis of te requirement .
# map
# reduce
# all this above metods are used for list.

#  by using filter metod: 

numbers=[10,15,13,20,26,9,3,41]
def even(n):
     return n%2==0 
newlist =list(filter(even,numbers))
print (newlist)   

numbers=[10,15,13,20,26,9,3,41]
newlist=list(filter(lambda X :X%2==0 , numbers))
print(newlist)  

# map

list=[10,12,40,30,35,15]
def add(n):
    return n+2
newlist=list(map(add,list))
print(newlist) 

newlist=list(map(lambda X:X+2 , list))
print(newlist) 

# reduce :
# method 1 : 

import functools
list=[10,20,30,5,40]
sum=functools.reduce(lambda x,y:x+y , list)
print(sum)  

# method 2 : 
from functools import reduce
list=[10,20,30,5,40]
sum=reduce(lambda x,y:x+y , list)
print(sum)

# list comprehension :

list=[]
for i in range(1,11):
    list.append(i)
    print(list)  

list=[X for X in range(1,11)] 
print(list) 

list=[X for X in range(1,11) if X%2==0]
print(list)   

msg="india is my country"
msg=msg.split("n")
for i in msg:
    print(i) 

msg="india is my country"
msg=msg.split("n-1")
for i in msg:
    print(i) 

msg="india is my country"
msg1=msg.split(" ")
msg1.reverse()
for i in msg[::-1]:
    print(i,end='')    


msg="india is my country"
msg1=msg.split(" ")
msg1.reverse()
for i in msg1:
    print(i)
  
msg="india is my country"
msg1=msg.split(" ")
for i in range(len(msg1)-1,-1,-1):
    print(msg1[i])  

# string is having  one method called format.
# performing format function.
    
msg="name:{},age :{}".format("ram",45)
print(msg)

msg="name:{1},age :{0}".format("ram",45)
print(msg) 

msg="name:{0},age :{1}".format("ram",45)
print(msg) 

msg="name:{a},age :{age}".format(a="ram",age=45)
print(msg) 

msg= "hi hello"
msg1=msg.replace("e","a") 
print(msg1) 

msg="india"
char_list =[char for char in msg]
print(char_list) 

msg1="india"
msg1=[]
for i in msg1:
    msg1.append(i)  
print(msg1)    

# file handling : 

file=open("ABC.txt" , "w")
file.write("hello world")
print("success fully write")
file.close()   

# print is used to write anyting in console to be printed.

file=open("ABC.txt","r")
data=file.read()
print(data)
file.close()  

file=open("XYZ.txt","w")
file.write("my name is ankita")
print("i love myself")
file.close()  


# if it is giving error then eiter you can use double slash or r method.
# 1st create the file and copy the pat where  you want to copy te path 
# then go ahead write down te msg that you want to save in the folder .

file=open("C:\\Users\\Amrendra Mishra\\Desktop\\demo\\ABC.txt","w")
file.write("hello world")
file.close() 

file=open("C:\\Users\\Amrendra Mishra\\Desktop\\demo\\ABC.txt","r")
data=file.read()
print(data)
file.close()  

file=open( "ABC.txt","r")
data=file.read()
file1=open("PQR.txt","w")
file1.write(data)
file1.close()
file1=open("PQR.txt","r")
data=file1.read()
print(data)
file1.close()   

# 1st we need to read and write the codes then we need to open te file from we need to copy the data into the anoter file.
# 1st save it ten open te notepad and save it and again run the code so whatever changes you have made that canges will display in the console.

#  writing the file

file=open( "LMN.txt","w")
msg=input("enter the message : ")
file.write(msg)
print("written successfully")
file.closed() 

# reading the file

file=open( "LMN.txt","r")
data=file.read()
print(data)
file.closed()

file=open( "LMN.txt","a")
msg=input("enter the message : ")
file.write(msg)
print("written successfully")
file.closed()  


# by appending the data will be preserved  

# write a program to print hello world.

print("hello world") 

#  write a program by giving the time to code to display.

import time
time.sleep(2)
print('2 seconds have passed since this program ran') 

# time is a module in which sleep is the function we used that means that tere should be interval of 2 sec and after 
# this interval the sentence should be displayed.

# flask is the external module , this is to installed by using pip 

import flask

# comments are denoted by # symbol which will convert the code into comments which will not run. it just convert it into the teory.
# comments will ignore some set of lines.

# REPL - read , evaluate , print loop  like if the pyton is stored in the correct manner then we will get the prompt as
# pyton version will be displayed.

import time
print("waiting for 1 sec")
time.sleep(1) 

# single line code can be commented by single inverted code like ''
# multiline comments in python is denoted by double inverted code like  " "
#  if there are n number of lines that is to be ommented then you can use the tripple inverted commas like this '''

print("Twinkle, twinkle, little star")
print ("How I wonder what you are")
print("Up above the world so high")
print("Like a diamond in the sky")
print("Twinkle, twinkle little star")
print("How I wonder what you are")
print("When the blazing sun is gone")
print("When he nothing shines upon")
print("Then you show your little light")
print("Twinkle, twinkle, all the night")
print("Twinkle, twinkle, little star")
print("How I wonder what you are")

'''print ("Twinkle, twinkle , little star
 How I wonder what you are
 Up above the world so high
 Like a diamond in the sky
 Twinkle, twinkle little star
 How I wonder what you are
 When the blazing sun is gone
 When he nothing shines upon
 Then you show your little light
 Twinkle, twinkle, all the night
 Twinkle, twinkle, little star
 How I wonder what you are")'''

# by using control / 
# we can convert the code into comments.

print("5*1")

#  write a program to make a code audible from the computer on behalf of the user .

import pyttsx3
engine = pyttsx3.init()
engine.say("hey ankita i am a python module. welcome to the place of python")
engine.runAndWait() 

import pyttsx3
engine = pyttsx3.init()
engine.say("hey asha mishra i am a python module. welcome to the place of python")
engine.runAndWait()  

import pyttsx3
engine = pyttsx3.init()
engine.say("hey amrendra mishra i am a python module. welcome to the place of python")
engine.runAndWait() 

# the importance of the above code is like on behalf of the person the python will code will talk to the oter person based on the text 
# which have been typed.

# OS is a python module.

import OS 

# the above code will give te error as te OS module is te external module so we need to install this module from the google
#  like externally.

import os 
print(os.listdir()) 

import os
os.listdir("path") # returns list

# import os  # importing the moduke
# print(os.listdir()) # function to display all the directory contents.

# dont add the useless comments to te code. it should be useful.
# dont write te whole explanantion .

# how and why this questions should be answered in te code explanantion . 

# variables are the containers in memeory . it is used to store the values which can be used later.

a=34
# here it will display the value of a 

print(a)
# but if you want to print string then that particular value should be in double inverted code followed by round parentesis
# then it will display the particular value.

print("a") 

print("a duck") 

a=34
c=56.23
print(c) 

# datatypes:
#integer - it is te whole number like 1,2,3,-1,-2,-3
# floating point umber - it is in the form of decimal 
# string - it is used to store the sequence of characters. and represented by double inverted code 
# booleans  - it is used to give the value as true or false , it saves the lot of memory.
# none - it is used to say that te value is nothing having te above datatypes and it does not use to allocate someting.

d=None
print(d)

e="a duck"
#  as the value of e is in te double inverted code so it is a string 
print(e) 

#  python can itself capable to identify the data types 

#  in , for , while is a keywords .
#  identifiers is something which have been named by the user. it can be class , functions or varibales names.

#  aritmetic operators :

a=75
b=64
print("a+b= ",a+b)
print("a-b= ",a-b)
print("a*b= ",a*b)
print("a/b= ",a/b)

#  print("demostrating assignmnet operators in python")

c=5
d=7
print(c,d)   

# this will print the values of c and d .

c+=5
print(c,d)  
# this will print thhe value of c and d 
d+=1    
# this will increament the value of d by 1 value.
print(c,d) 

d-=2  
# this will decreament the value of d by 2 values.
print(c,d) 

#  comparision operators in python:
#  you cannot add te tab or space uneccessary te pyton will give the identation error.

e=6
f=9
print(e==f) 
print(e>f)
print(e<f) 
print(e!=f) 


# == it is used to verify wheater the value is equal to or not .

#  logical operators in python:

e=5
f=58
print(e==f and e>f) 
print(e==f or e>f) 
print(not(e>f)) 

a="i am ankita"
b=58
c=None
d="false" 

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b)) 
print(type(c)) 
print(type(d))  

#  a number can be converted into string and vice versa.

a=56
b=56
print(a==b)

a=56
b="56"

print(a)
print(b)
print(c)

print(a==b)
print(a==c)
print(b==c)

a=56
b="56"
c=int(b)
print(a==b) 
print(type(a))
print(type(b))
print(type(c))

# 56y is not converted to integer. 

a=input("enter the name : ")
print("your name is : ",a) 

a=input("enter first number")
b=input("enter second number")
print ("the sum is : " , a+b) 

#  this will give the concatination result as we have not defined the integer of the value.

print("the sum is : " , int(a)+int(b)) 

#  if string are added then it is called conactination.
#  if we want the value in the integer form then we need to define the integer of that value to get te value in the integer form
#  not in the string form like in the concatination form.
#  by default the output of input is always a string so we need to define the int that is integer if we want the integer value.

#  write a python program to add 2 numbers.

a=input("enter first number")
b=input("enter second number")
print("the sum of these 2 number is : " , int(a)+int(b)) 

a=int(input("enter first number"))
b=int(input("enter second number"))
print("the sum of these 2 number is : " , a+b ) 

#  write a pyton program to find remainder when a number is divided by 2.

number=int(input("enter the number"))
print("remainder when the number is divided by 2 is : " , number%2) 

# check the type of variable assigned using input() function.

a=input("enter something")
print("the type of a is : ",type(a)) 

#  use comparision operator to find out wheather a given variable a is greater than b or not take a=34 and b = 80

a=34
b=80
print("a is greate than b :" , a>b) 

a=3489
b=80
print("a is greate than b :" , a>b) 

#  print will automatically gives the space in the output.

#  write a python program to find average of 2 numbers entered by the user .

a=int(input("enter the number"))
print("the average of this number : ", a/a)

#  write a python program to calculate square root of a number entered by the user .

a=int(input("enter the number"))
print("the square of this number : ", a*a)

#  STRING

name="harry" 
print(name)
print(type(name)) 

name ='john'
print(name)
print(type(name)) 

name1= "adam angelo"
name2 = 'john maskey'
name3 = "twinkle twinkle little star"

print(type(name1))
print(type(name2))
print(type(name3)) 

# string slicing - it is used to get some characters of the string.
# index or counting in python starts from 0.

# to find some characters of the string .

name="harry"
print(name) 
print(name[0]) 
print(name[3])
print(name[0:3]) 
print(name[1:3])  
print(name[1:4]) 

# to find the length of the wordname="following"

print(len(name)) 

mystr="abcdefgijklmnopqrstuvwxyz"
print(mystr[2:6])

# to find the values by using skipped value.

mystr="abcdefgijklmnopqrstuvwxyz"
print(mystr[1:9:2]) 

#  here 1st value is the start index , 2nd number is the last index through which the value will be printed and last value is the
#  skipped value

print(mystr[1:9:3]) 

print(len(mystr)) 

#  to check wheater te particular string ends with the particular characters or not.
#  we can use the endswith and startswith method.

mystr="abcdefgijklmnopqrstuvwxyz"
print(mystr.endswith("ggy")) 
print(mystr.endswith("xyz"))
print(mystr.endswith("XYZ"))

print(mystr.startswith("ggy"))
print(mystr.startswith("abc"))

# to find the count of particular characters in string 

print(mystr.count("a")) 
print(mystr.count("ab")) 

#  capitalize - it is used to get the letters in capital letters.
#  if the string is already capitalized then it will do nothing ,  the python will print the same thing.

print(mystr.capitalize()) 

mystr=("my name is harry name")
print(mystr.capitalize()) 
print(mystr.find("name")) 
print(mystr.replace("name" , "date")) 

# escape characters is having more then  1 characters.

myname=("my name is harry") 
print(myname) 

# \n is used to add the new line in a string.
#  t is for tab

myname=("my name is \n is harry") 
print("myname") 

myname="my name\nis\t\harry"
print(myname) 

# all the escape characters cannot be used at once.

# write a python program to display a user entered name followed by good afternoon using input() function.

name=input("enter your name : ")
print("good afternoon"+ name) 

name=input("enter your name : ")
print("good afternoon", name) 

#  write a program to fill in a letter template given below with name and date.

name=input("enter the name")
date=input("enter the date")

# template is a string we created 
# template=
# dear<name>,
# you are selected
# <|date|>

# print(template.replace('<|name|>',name).replace('<|date|>',date)) 

#  write a program to detect double spaces in a string.

mystr="this is me   and i am a good girl"

print(mystr.find("  ")) 

#  here we will get -1 which means that we dont ave word harry in our string.

print(mystr.find(" harry ")) 

#  replace thhe double space from problem 3 with single spaces.

mystr="this is me   and i am a good girl"
print(mystr.replace("  "," ")) 

#  write a program to format the following letter using escape sequence characters.

letter = "dear harry , this python course is  nice. thanks!"

letter = "dear harry , \n\tThis python course is  nice.\nthanks!"
print(letter) 

#  LIST AND TUPLES.

#  we can store or add list inside list.

a=12
b="this is a string"
c=False
mylist=[a,b,c]
print(mylist) 
print(type(mylist)) 

# list is the collection of items including integer , floating point number , strings , boolean values.

a=12
b="this is a string"
c=False
mylist=[a,b,c,258.24]
print(mylist) 

# indexing starts from 0 
# counting starts from 1 .

l1=[7,9,"harry"]
print(l1) 
print(l1[1])  
print(l1[2])
print(l1[0:2]) 
print(l1[0:3]) 
print(l1[0:4]) 
print(l1[0:40]) 

# slice of a list is a list.

mylistofnumbers=[1,8,7,2,21,15]
print(mylistofnumbers) 

# camel case - means taking the 1st letter of the word if the variable name is large.

# sort - it is used to give te list values in te ascending prder .
#  performing various operations on list.

mylistofnumbers=[1,8,7,2,21,15]
mylistofnumbers.sort()

a=mylistofnumbers.sort()
print(mylistofnumbers) 

mylistofnumbers=[1,8,7,2,21,15]
mylistofnumbers.reverse() 
print(mylistofnumbers) 

# append - it is used to add the value at the end of the original list.
# in the original list you will see the updations.
# append is not going to display the new list for any updations.

mylistofnumbers=[1,8,7,2,21,15]
mylistofnumbers.append(9)
print(mylistofnumbers) 

mylistofnumbers=[1,8,7,2,21,15]
mylistofnumbers.insert(2,9) 
# 2,9 - it means at index 2 of the list we need to insert 9
print(mylistofnumbers) 

# pop - it will delete value from the end of the list.
mylistofnumbers=[1,8,7,2,21,15]
mylistofnumbers.pop()
print(mylistofnumbers) 
 
mylistofnumbers=[1,8,7,2,21,15]
mylistofnumbers.pop()
mylistofnumbers.pop()
mylistofnumbers.pop()
print(mylistofnumbers) 


mylistofnumbers=[1,8,7,2,21,15]
mylistofnumbers.pop(2) 
print(mylistofnumbers) 

# pop(2) - the value from index 2 will be disappererd 

mylistofnumbers=[1,8,7,2,21,15]
mylistofnumbers.remove(2)
print(mylistofnumbers) 

mylistofnumbers=[1,8,7,2,21,28,15]
mylistofnumbers.remove(28)
print(mylistofnumbers) 

mylistofnumbers= [1,8,7,2,21,15,21]
mylistofnumbers.remove(21)
print(mylistofnumbers) 

mylistofnumbers= [1,8,7,2,21,15,21]
mylistofnumbers.remove(21)
mylistofnumbers.remove(21)
print(mylistofnumbers) 

# tuples is an immutable datatype in python . that means we cannot change or modify anything in python.

mytuple=(3,6,7)
print(mytuple) 
mytuple[0] 

# this will throw an error as we cannot modify anything in the tuple.

print(type(mytuple)) 

mytuple=()
print(mytuple)

mytuple=(4)
# it will directly print the 4.
print(mytuple)

mytuple=(4, ) 
# here it means tuple is having the value 4 
print(mytuple)

# tuple methods: 
# count - it is used to give the number of count of particular value.
a=(1,7,2)
print(a.count(1)) 
print(a.count(7)) 

a=(1,7,2,58,78,55,55,55,55,78,87)
print(a.count(55)) 

print(a.index(1)) 

a=[10,7,12,2,2]
print(a.index(2)) 

# write a program to store seven fruits in a list entered by the user.

f1=input("enter fruit1 : ")
f2=input("enter fruit2 : ")
f3=input("enter fruit3 : ")
f4=input("enter fruit4 : ")
f5=input("enter fruit5 : ")
f6=input("enter fruit6 : ")
f7=input("enter fruit7 : ")

fruitlist=[f1,f2,f3,f4,f5,f6,f7]
print(fruitlist) 

# write a program to accept marks of 6 students and display them in a sorted manner.
#  sometimes if it means like create array in python that means it is list in python.
# marks supposed to be in the integer.

marks1=int(input("enter marks of student1 : "))
marks2=int(input("enter marks of student2 : "))
marks3=int(input("enter marks of student3 : "))
marks4=int(input("enter marks of student4 : "))
marks5=int(input("enter marks of student5 : "))
marks6=int(input("enter marks of student6 : "))

markslist=[marks1,marks2,marks3,marks4,marks5,marks6]
markslist.sort()
print(markslist) 

# check that a tuple cannot be changed in python.

# first we have done the modification with the list.

mytuple=[4,58,2,8]
print(mytuple)  

mytuple[0] = 58
print(mytuple) 

print(type(mytuple)) 

# modification with the tuple.

a=(1,2,5)
print(a) 

#  doing modification 

a[0] = 90
print(a) 

# write a program to sum a list with 4 numbers.

mylist=[1,2,4,5]
sum=0
sum+=mylist[0]
sum+=mylist[1]
sum+=mylist[2]
sum+=mylist[3]
print("the value of sum is : ", sum)

# when we add a comma in python code the space is automatically appended.

#  write a program to count the number of zeros in the following tuple.
a=(7,0,8,0,0,9)

tu=(7,0,8,0,0,9)
print("the number of zeros in this tuple is : " , tu.count(0))

tu=(7,0,8,0,0,58,58,58,58,85 , 589,54,9)
print("the number of zeros in this tuple is : " , tu.count(58)) 

# dictionary and sets

oxford={ "gift":"something willenglity given to someone to appreciate"}
print(oxford) 
# print(oxford['this']) -  works in C++

mylist=[4,5,8] 
print(mylist) 

# get- it is the keyword which will display te value if the value is present. 
#  it will not trow the error.

# set - it is te collection of non- repetative elements.
# sets does not have duplicates .

# {} - it is a dict tat means user is trying to create a set.

myset={1,34,53}
print(len(myset)) 

myset={1,34,53}
myset.add(45)
myset.add(1)
myset.add("5") 
print(len(myset)) 

print(type(myset)) 
myset.remove(34)
print(myset) 

print(myset.pop())
print(myset)

print(myset.clear())
print(myset) 

# 1 and "1" are the integers and strings as per te inverted code in python.

# union - combining 2 sets 
# intersection - it will return those values which is present in the set.

# write a program to create a dictionary of hindi words with value as their english transaltion . provide user with an option to look it up.

oxford={
     "lakdi": "wood",
     "kursi": "chair",
     "chaku": "knife"
 }

key=input("enter the key\n")
print("the value corresponding to key is : " ,oxford.get(key))  
if (oxford.get(key)==None):
    print("value not found")
else:
    print("the value corresponding to key is : " ,oxford.get(key)) 

# write a program to input 8 numbers from the user and display all te unique numbers.

s=set()
for i in range(8):
    s.add(input("enter your number")) 

# can we have a set with 18(int) and "18" (str) as a value in it.

s=set()
for i in range(18):
    s.add(input("enter your number")) 

s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(s) 

# s={} what is the type of set?

set=()
print(type(set))

set={}
print(type(set)) 

# create an empty dictionary .allow 4 freinds to enter tere favorite language as values and use keys as tere names , assume that the names are unique.

# Create an empty dictionary
favorite_languages = {}

# Allow four friends to enter their favorite languages
for _ in range(4):
    friend_name = input("Enter friend's name: ")
    favorite_language = input(f"Enter {friend_name}'s favorite language: ")
    favorite_languages[friend_name] = favorite_language

# Display the dictionary
print("Favorite Languages Dictionary:", favorite_languages)

# if the keys are one of the key will be stay and if the values will be same then all the values will be same.

# conditionals:
# conditions expressions: 

#  bydefault syntax of if , elif and else statement 

# if condition1:
    # print
# elif condition2:
    # print
# else:
    # print 

# examples on conditional expressions.

a=1
if(a>4):
    print("a is greater than 4")
elif (a>2):
    print("a is greater than 2")
else:
    print("nothing") 

a=3
if(a>4):
    print("a is greater than 4")
elif (a>2):
    print("a is greater than 3")
else:
    print("nothing") 

#  we can use if and elif and exclude else 
    
a=30
if(a>4):
    print("a is greater than 4")
elif(a>2):
    print("a is greater than 2")
else:
    print("nothing") 

age=int(input("enter your age"))
if(age>18):
    print("yes")
else:
    print("no")

# relational operators:

a=435
b=64
print(a>5) 
print(b>=64) 
print(b>=164) 

# logical operators:

a=True
b=False
print(a and b ) 
#  while using and operator both the conditions will be statisfied.
print(a or b) 
#  while using or operator any one of the condition will be ststisfied.
print(not(a)) 

# elif OR else if condition bedefault syntax: 
# if (condition1):
    # code
# elif(condition2):
    # code
# elif(condition3):
    # code
# else: 
# code

# you can skip else , elif   and if there is only of condition then condition will be checked and 
# if  the condition is true the code will be executed oterwise te code is not going to be executed.

# write a program to find greatest of 4 numbers entered by the user .

a=45
b=6
c=86
d=23
if(a>b):
    maxNum1=a
else:
    maxNum1=b
if(c>d):
       maxNum2=c
else:
       maxNum2=c
if(maxNum2>maxNum1):
        maxNum=maxNum2
else:
        maxNum=maxNum1
print("maximum number out of these 4 numbers is",maxNum) 

# write a program to find out wheater a student is pass or fail, if it requires total 40% and at least 33% in eac subject to pass, 
# assume 3 subjects and take marks as an input from the user .

m1=int(input("enter the marks for subject1 :"))
m2=int(input("enter the marks for subject2 :"))
m3=int(input("enter the marks for subject3 :"))

overall=(m1+m2+m3)/3

if (overall>=40):
    if(m1>=33 and m2>=33 and m3>=33):
     print("you have passed the exam due to one of the subject")
else:
     print("you have not passed the exam due to overall percentage") 

#  a spam comment is defined as a text contatining following keywords:
# "make a lot of money"
# "buy now"
# "subscribe this"
# "click this"
     
# write a program to detect these spams.

spamwords=['buy now','subscribe this','click this']
email="this is a nice stock, you need to clcik tis and buy this stock"

#  1st example :

email=input("enter your email :")
spam=False 
if ('buy now' in email):
    spam=True

if ('subscribe this' in email):
     spam=True
     if('click this' in email):
         spam=True
         print("spam is",spam) 

#  2nd example:
         
email=input("enter your email :")
spam=False 
if ('buy now' in email):
     spam=True

if ('subscribe this' in email):
     spam=True

if ('click this' in email):
     spam=True

print("spam is",spam) 

# 3rd example:

email=input("enter your email :").lower()
spam=False 
if ('buy now' in email):
     spam=True

if ('subscribe this' in email):
     spam=True

if ('click this' in email):
     spam=True

print("spam is",spam) 

# write a program to wheater a given username  contains less than 10 caracters or not.

def check_username_length(username):
    if len(username) < 10:
        return True
    else:
        return False

# write a program whichh finds out wheater a given name is present in a list or not.

name="harry"
names=['harry','shubham','meena']
if(name in names):
     print("name is present")
else:
     print("name is not present ") 


# write a program to calculate a grade of a student from is marks from the following scheme:
# 90-100 ex
# 80-90 a
# 70-80 b
# 60-70 c
# 50-60 d
# <50 f
    
def calculate_grade(marks):
    if marks >= 90:
        return "Ex"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
    
# write a prgram to find out wheather a given post is talking about "harry or not"

text=input("enter your text:")
if "harry" in text.lower():
     print("yes harry is present")
else:
     print("no harry is not present") 

# LOOPS:
#  if we want to repeat certain set of instructions everytime then we are using loops.

# syntax of wile loop:
#  while condition:
#  body of the loop 

# performing operations on loops.
     
a=0
while(a<100):
    print(a)
    a+=1

a=100
while(a<1000):
     print(a)
     a+=1

i=0
while(i<20):
    print(i)
    i+=1 

i=0
while(i<20):
    print(i)
    i+=2

i=0
while(i<51):
     print(i)
     i+=1 

i=0
while(i<51):
    print(i)
    i+=1 

i=1
while(i<51):
     print(i)
     i+=1 

i=1
while(i<=5):
     print(i)
     i+=1 

i=1
while(i<6):
     print(i)
     i+=1 

i=0
while(i<5):
     print("harry")
     i=i+1
 
i=1
while(i<=5):
     print(i) 

i=1
while(i<=5):
     print(i) 
     i+=1 

# write a program to print the content of a list using while loops.

a=[1,2,3,4,5,"banana"]
i=0
while (i<len(a)):
     print(a[i])
     i+=1

a=[1,"apple",3,4,5,"banana"]
i=0
while (i<len(a)):
     print(a[i])
     i+=1

# syntax of for loop:
     
# 1st create te list 
     
for item in l:
    print(item)

# range is used to display the value with n-1

for i in range(34):
     print(i) 

for i in range(10,34):
     print(i) 

# range function will include the 1st value but exclude the last value .
    
a=[1,"apple",3,4,5,"banana"]
i=0
for i in range(len(a)):
     print(a[i])
     i+=1

a=[1,"apple",3,4,5,"banana"]
for item in a:
    print(item) 

for i in range(10,34,2):
    print(i) 

for i in range(10,34,3):
    print(i) 

#  can you use for loop with else?

# syntax : 

l=[]
for item in l:
    print(item)
else:
    print("done")

# loop iteration example:
    
a=[1,2,3,4,5]
for item in a :
     print(item)
     if(item==3):
         continue
     print("done this iteration for",item)
else:
    print("we are inside else")
    print("we have finished this loop")

a=[1,2,3,4,5]
for item in a :
     print(item)
     if(item==3):
         break
     print("done this iteration for",item)
else:
    print("we are inside else")
    print("we have finished this loop")

for i in range(0,80):
      print(i)
      if (i==3):
        break
     
for i in range (4):
    print("printing")
    if i==2:
        continue
    print(i)

# iteration : it is defined as the circle of loop going throug the values.
# iteration examples:
    
a=[1,2,3,4,5]
for item in a :
     print(item)
     if(item==3):
         break
print("we have finished this loop")

a=[1,2,3,4,5]
for item in a :
    print(item)
    if(item==4):
        break
print("we have finished this loop")

a=[1,2,3,4,5]
for item in a :
     print(item)
     if(item==3):
         continue
     print("we have finished this loop")

a=[1,2,3,4,5]
for item in a :
    print(item)
    if(item==2):
        break
print("we have finished this loop")

a=[1,2,3,4,5]
for item in a :
     print(item)
     if(item==3):
         break
     print("done this iteration for" , item)

a=[1,2,3,4,5]
for item in a :
     print(item)
     if(item==4):
         break
     print("we have finished this loop")

# continue - it will exceute till the last line of code.

# pass statement : 

# bydefault syntax : 

# l=[]
# for item in l:
    # pass

# write a program by using pass function :
     
for i in  range(0,78):
     pass
     print(" do something") 

# write a program to print multiplication table of a given number using for loop.

num=int(input("enter the number"))
for i in range(5):
    print(f"{num}X{i+1}={num*(i+1)}") 

num=int(input("enter the number"))
for i in range(10):
    print(f"{num}X{i+1}={num*(i+1)}") 

num=int(input("enter the number"))
for i in range(8):
    print(f"{num}X{i+1}={num*(i+1)}") 

# write a program to greet all te person names stored in a list l1 and which starts wit s.
# l1=["harry","soham","sachin","rahul"]

l1=["shivam","soham","harry","deepika","Sahil"]
for item in l1:
    if item. startswith("s"):
        print(f"good morning{item}") 

# attempt problem 1 using while loop.
        
# write a program to find wheater a given number is prime or not.

num=6
for i in range(2,6):
    if(num%i==0):
         print("not prime")
         break
else:
         print("this is prime")

num=13
for i in range(2,6):
    if(num%i==0):
         print("not prime")
         break
else:
         print("this is prime")

num=3
for i in range(2,6):
     if(num%i==0):
         print("not prime")
         break
else:
         print("this is prime")

num=9
for i in range(2,num):
    if(num%i==0):
         print("not prime")
         break
else:
         print("this is prime")

# else will only execute if the for loop have been completely executed .
        
# write a program to find the sum of first n natural numbers using while loop.

i=1  
sum=0
n=3
while (i<=n):
     sum+= i 
     i +=1
     print(f"the sum of first {n} natural numbers is{sum}") 

i=1  
sum=0
n=10
while (i<=n):
     sum+= i 
     i +=1
     print(f"the sum of first {n} natural numbers is{sum}")  

# write a program to calculate the factorial of a given number using for loop.
        
def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

# STAR PATTERN / PYRAMID PATTERN: 

#  write a program to display star pattern: 

# write a program to display the number of stars as per the given number .

n=int(input("enter the number : "))
for i in range(1,n+1):
     for j in range(n-i):
         print(" ",end="")
     for j in range(2*i-1):
         print("*",end="")
     for j in range(n-i):
         print(" ",end="")
     print("\n",end="")   

# write a program to display 
# ****** 
 
 
# ** 
 
 
# ** 
 
 
# ****** - in this order.

n=5
for i in range(n):
     for j in range(n):
         if(i==0 or j==0 or i==n-1 or j==n-1):
             print("*",end="")
         else:
             print(" ",end="")
             print("\n",end="") 

# write a program to display
# ***** 
 
# ** 
 
# ***** - in this order.

n=4
for i in range(n):
     for j in range(n):
         if(i==0 or j==0 or i==n-1 or j==n-1):
             print("*",end="")
         else:
             print(" ",end="")
             print("\n",end="")  

# write a program to display
# *** 
# ** 
# ***  - in this order.

n=3
for i in range(n):
    for j in range(n):
         if(i==0 or j==0 or i==n-1 or j==n-1):
             print("*",end="")
    else:
        print(" ",end="")
        print("\n",end="")   

# write a program to print the multiplication table of n using for loop in reversal order.

n=10
for j in range(1,n+1):
     i=n-j+1
     print(i) 

n=10
for j in range(1,n+1):
     i=n-j+1
     print(f"{n}X {i} = {n*i}") 

n=10
for j in range(1,11):
     i=11-j+1
     print(f"{n}X {i} = {n*i}") 

# DRY PRINICIPAL
#  it means do not repeat yourself.
# def is a reserved keyword in python.

def func1():
    print("hello harry")
    print("ypu are good")
    print("i am anoter line")

#  the selected lines of codes are the function defination.

func1()
func1()
func1()
func1()
func1() 

#  write a program to greet a user a with good day using functions.

def func1():
    print("good day")
    func1() 

# built in functions are already defined by the python like len , range & print.
# user defined functions are defined by the user .

# write a program by using range function.
    
print("i am a built in function ")
for i in range(3):
     print(i)

#  performing average.
     
def average(a,b,c):
    return(a+b+c)/3

avg=average(3,6,4)
print(avg)

avg = average()
print(avg )
#  the above code will throw an error as we dont called any numbers .

# performing concatination of 2 strings.

def greet(name="harry"):
     return"hello"+ name
a=greet("shubh") 
print(a)

def greet(name="harry"):
     return"hello"+ name
print(greet("shubh") )

#  in the above code the space will not present after hello.

def greet(name="harry"):
    return"hello "+ name
print(greet("shubh") )
 
#  in the above code  the space will present after hello.

# recursion :  recursion is used to make the use of the mathematical formulas.
# factorial(n)=n*factorial(n-1)
# factorial(0) = 1 ( by defination)

# write a program to find out the factorial .

def factorial(n):
# base condition actually stops recursion over and over happining .
    if (n==0 or n==1):
        return n* factorial(n-1) 
    
def factorial(n):
    if (n==0 or n==1):
        return 1
    return n* factorial (n-1)

a=factorial(3)
print(a)  

a=factorial(1)
print(a) 

a=factorial(100)
print(a) 

# write a program using function to find greatest of these numbers.

def greatest(num1,num2,num3):
     if (num1>num2):
         greater=num1
     else:
        greater = num2
     if(num3>greater):
         greater=num3
     return greater
a=greatest(333,585,6845)
print(a)  

# write a python program using function to convert celcius to farenhite

def cel2far(cel):
    return(cel* 9/5) +32
a=cel2far(35)
print(a) 

def cel2far(cel):
    return(cel* 9/5) +32
a=cel2far(135)
print(a) 

#  how do you prevent a python print() function to print a new line at the end.

print("harry and raj")
print("sadhna") 

#  print be default prints the new line.

print("harry" and "raj" , end="")
print("sadhna", end="") 

print("harry and raj" , end="")
print("sadhna", end="") 

print("harry and raj" , end=" ")
print(" and sadhna", end=" ")

print("Harry" and "Raj" , end=" ###")
print(" and sadhna", end=" ###") 

print("Harry and Raj" , end=" ###")
print(" and sadhna", end=" ###") 

# if we want that print statement shhould not print statement then simply write the end statement with the blank parenthesis in double inverted commas.

# write a recursive function to calculate the sum of first n natural numbers.
# sum(8) = 1+2+3+4+5+6+7+8
# sum(n) = sum(n-1)+n

def sum(n):
    if(n==1):
         return 1
    return sum(n-1)+n

a= sum(4)
print(a)

a= sum(5)
print(a) 

#  write a python function to print 1st n lines of the following pattern.

def printpattern(n):
     for i in range(n):
         print("*", end="")
     print("\n")
     printpattern(4) 

def printpattern(n):
     for i in range(n):
         print("*", end="")
     print("\n")
     printpattern(9) 

def printpattern(n):
     for i in range(n):
         print("*", end="")
     print("\n")
     printpattern(100) 

def printpattern(n):
     for i in range(n):
         print(i)
     printpattern(4)

def printpattern(n):
     for i in range(n):
      print(n-i)  
      printpattern(4)   

def printpattern(n):
     for i in range(n):
         print("*"*(n-i))
         printpattern(3) 

def printpattern(n):
    for i in range(n):
         print("*"*(n-i))
         printpattern(10)  

def printpattern(n):
     for i in range(n):
         print("*"*(n))
         printpattern(3)  

# write a python function which converts inces to cms.

def inches_to_cms(inches):
    cms = inches * 2.54
    return cms

# write a python function to remove a given word from a list  and strip it at the same time.

def process(l, word):
     word=word.strip()
     if word in l:
         l.remove(word)
         return l1

l1=["harry","rohan","akash","lovish"] 
l1=process(l1,    'harddy')
print(l1)  

def process(l, word):
     word=word.strip()
     if word in l:
         l.remove(word)
         return l1

l1=["harry","rohan","akash","lovish"] 
l1=process(l1,    'rohan   ')
print(l1)   

# write a python function to print multiplication table of a given  number.

f=open("this.txt,"r"")
text= f.read()
print(text)

f=open("this.txt,"r"")
text= f.read(6)
print(text)
f.close()

f=open("this.txt,"r"")
text= f.read(6)
text=f.readline()
print(text)
f.close()

f=open("this.txt,"r"")
text= f.read(6)
text=f.readlines()
print(text)
text=f.readlines()
print(text)
text=f.readlines()
print(text)
text=f.readlines()
print(text)
text=f.readlines()
print(text)
f.close()

# readlines - it actually read all the lines stored it in  a list and returns te list.
# write function actually takes thhe string .

f=open("write.txt","w")
f.write("this is a text , i want to write to this file")
f.close() 

f=open("write.txt","w")
f.write("this is a text , i want to write to this file\n")
f.write("second line: this is a text , i want to write to this file")
f.close() 

# here the file has been created.

# append mode : 

# in append we can keep on adding the lines in code.
# whenver we will use append as a then lots of lines of code will be added if the user want to add.


f=open("write.txt","a")
f.write("this is a text , i want to write to this file\n")
f.write("second line: this is a text , i want to write to this file")
f.close() 

with open("mine.txt","w") as f:
     f.write("this file is mine") 

# if we are using with statement then we dont need to use the close statement.

# write a program to read the text from a given file 'poems.txt' and find it out wheater it is contains the word twinkle.

with open("poems.txt","r") as f:
    if("twinkle"in f.read()):
        print("yes twinkle is present")
    else:
        print("the twinkle is not present")

# the game function in a program lets a user plays a game and returns the score as an integer. you need to read a file 'hiscore.txt 
# which is either blank or contains te previous hi-score you need to write a program to update the i-score whenever game() breaks the 
# hi-score.

# random module is used to generate some random integers.

# write a program by using random module.
        
import random
def game():
    score=random.randint(1,100)
    print(f"the score is {score}")
    return score 
score=game()
with open("hiscore.txt","r") as f:
     hiscore = int(f.read())
if hiscore < score:
     with open("hiscore.txt","w") as f:
      f.write(str(score)) 

# write a program to generate multiplication table from 2 to 20  and qwrite it on the different files . 
# place these files in a folder for a 13 years old.
     
for i in range(2,21):
# here we need to print te table from 2 to 20 

table=''
# whenever we need to generate the multiplication we are actually creating an empty string .

for j in range(1,11):
# here we will display te table from 1 to 10.

table +=f"{i}X {j} = {i*j}\n"
# here the above string is added to te table string  to display the table in te multiplication format .

with open (f'tables/{i}.txt','w') as f:
    f.write(table)  

# a files contains the word "donkey" multiple times , you need to write a program wich replaces tis word with ###### 
# by updating the same file.

with open('file.txt') as f:
    txt=f.read()

txt=txt.replace('donkey',"######") 

with open('file.txt','w') as f:
    txt=f.write() 

# repeat program 4 for a list of such words to be censored.

def censor_text(text, censor_words):
    for word in censor_words:
        text = text.replace(word, '*' * len(word))
    return text

# write a program to mine a log file and find out wheather it contains python.

def search_python_keyword(log_file_path):
    try:
        with open(log_file_path, 'r') as log_file:
            for line_number, line in enumerate(log_file, start=1):
                if 'python' in line.lower():
                    print(f"Found 'python' in {log_file_path} at line {line_number}:")
                    print(line.strip())

        print("Search completed.")
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")


#  write a program to find  out wheater a file is identical and matches the content of another file.
        
def are_files_identical(file1, file2):
    try:
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            content1 = f1.read()
            content2 = f2.read()

            return content1 == content2
    except FileNotFoundError:
        print("One or both files not found.")
        return False

if __name__ == "__main__":
    file1_path = input("Enter the path of the first file: ")
    file2_path = input("Enter the path of the second file: ")

    if are_files_identical(file1_path, file2_path):
        print("Files are identical.")
    else:
        print("Files are not identical.")


# write a program to wipe out the contents of a file using python.
        
def wipe_file_contents(file_path):
    try:
        with open(file_path, 'w') as file:
            file.truncate(0)
        print(f"Contents of '{file_path}' have been wiped out.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

# write a python program to remove a file to "removed_by_pyton.txt".

import os
oldname=input("enter the name of the file to rename")
newname=input("enter the name of te file")

with open(oldname,'r') as f:
    text=f.read()

with open(newname,'r') as f:
     f.write(text)

os.remove(oldname) 

# how to delete the file in python using OS?

import os

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path of the file you want to delete: ")
    delete_file(file_path)

# creation of class
# a very basic sample class.

class employee:
     name="harry"
     marks=34
     center="delhi"

harry=mployeee() -  a basic object 
print(harry.marks) 
print(harry.center) 
print(harry.name)  

# pascal case means the 1st letter of the variable is capital.
# EmployeeForLg - this is the pasacl case.

class employee:
    name="harry"
     marks=34
    center="delhi"

def printobj(self):
         print(f"the name is{self.name}")

harry=employee()
print(harry.marks) 
print(harry.center) 
print(harry.name)   
print(harry.printobj()) 

# self - the moment we write a function inside a class we need to write the self parameter.
# why we need to add te self paarmeter ?

# numpy gives the few syntax to display arrays in python.

#  changing the class atrributes .

class employee:
     name="harry" - name is the class attribute 
     marks=34
     center="delhi"
     def printobj(self):
         print(f"the name is{self.name}")


harry=employee()
shyam=employee()
print(harry.name)
print(shyam.name) 
# changing the name from harry to shyam.
shyam.name="shyam " 
# setting an instance attribute to shyam .
print(shyam.name) 
print(harry.name) 

# if you want to change the class attribute you should not use the class object .

# instance attribute is different from class attribute.

# instance attribute is te personal property of the object .
# class attribute is te personal attribute of the class.

# class creation

class employee:
     name="harry" 
     marks=34
     center="delhi"
     def printobj(self):
         print(f"the name is{self.name}")

employee.name="harrynew"  - setting a class atrribute for employee 
harry=employee()
shyam=employee()
print(harry.name)
print(shyam.name) 
# changing the name from arry to shyam.
shyam.name="shyam " 
print(shyam.name) 
print(harry.name) employee.printobj(harry)

# class creation

class employee:
     name="harry" 
     marks=34
     center="delhi"
     def printobj(self):
         print(f"the name is{self.name}")

employee.name="harrynew"  
harry=employee()
shyam=employee()
print(harry.name)
print(shyam.name) 
# changing the name from arry to shyam.
shyam.name="shyam " 
print(shyam.name) 
print(harry.name)
employee.printobj(harry) 

# class creation

class employee:
     name="harry" 
     marks=34
     center="delhi"
     def printobj(self54685445):
         print(f"the name is{self54685445.name}")

employee.name="harrynew"  
harry=employee()
shyam=employee()
print(harry.name)
print(shyam.name) 
# changing the name from arry to shyam.
shyam.name="shyam " 
print(shyam.name) 
print(harry.name)
employee.printobj(harry)  

# class creation

class employee:
     name="harry" 
     marks=34
     center="delhi"
     def printobj(self):
         print(f"the name is{self.name}")
         @staticmethod
         def greet():
             print("good day")


employee.name="harrynew"  
harry=employee()
shyam=employee()
print(harry.name)
print(shyam.name) 
# changing the name from arry to shyam.
shyam.name="shyam " 
print(shyam.name) 
print(harry.name)
employee.printobj(harry)
harry.greet()  
employee.greet()  

# constructors are the very important consistent of te class.

class employee:
     center= "not known"
     def __init__(self, name,marks,center):
         self.name=name 
         self.marks=marks
         self.center=center
         def printobj(self):
              print(f"the name is{self.name}")
              print(f"the marks is{self.marks}")
              print(f"the center is{self.center}") 

@staticmethod
def greet():
         print("good day")
         harry=employee("harry",50,"delhi")
         rohan=employee("rohan",80,"mumbai")
         harry.printobj() 
         rohan.printobj()    

# create a class programmer for storing infiormation of few programmers working at microsoft.

class programmer:
    def __init__ (self,name,language):
      self.name=name
      self.language=language
      harry=programmer("harry","python")
      harry=programmer("rohan","java")
      print(harry.name)
      print(rohan.name)  

# write a class calculator capable of finding a square cube and square root of a number .

 import math
class calculator:
    def __init__ (self,number):
         self.number=number
    def square(self):
         return self.number*self.number
    def squareroot(self):
         return math.sqrt(self.number)
    def cube(self):
         return self.number*self.number*self.number
two= calculator(2)
print(two.number)
print(two.cube())
print(two.square())
print(two.squareroot())  

# create a class with te class attribute a ;create an object from it and set a directly using object a=0. does this 
# change the class attribute?

class myclass:
     a=9
obj=myclass()
print(obj.a)
obj.a=0
# setting an instance attribute.
print(obj.a) 
print(myclass.a) 

# add a static method in problem 2 to greet the user with hello.

# write a class train which has a methods to book a ticket, get status (no.of seats) and get fare information of the trains
# running under indian railways.

class train:
    def __init__(self):
         self.seats=78
         self.fare=175
    def booktickets(self):
             self.seats=-1
    def getstatus(self):
                 print(self.seats)
    def getfareinformation(self):
                     print(self.fare)
tr=train()
tr.getfareinformation()
tr.getstatus()
tr.booktickets()
tr.getstatus()    

# can you change the self parameter inside a class to siomething else(say"harry"), 
# try changing self to slf or hary and see the effects.

# yes we can change the self to anything and it is not going to harm the program in any manner .
# only the thing is readibility of the code will reduce and this should be avoided.

# Inheritance

class employee:
    a=34

class programmer(employee):
         b=34

pr=programmer()
print(pr.a)
print(pr.b) 

em=employee()
print(em.a)
print(em.b) 

em=employee()
print(em.a) 

# print(em.b) this lines throws an error as we dont have b in class employee.

# the above code is an example of single inheritance.
    
class parent1:
     a=4
class parent2:
     b=2
class child(parent1,parent2):
     c=9

ch=child()
print(ch.a)
print(ch.b)
print(ch.c)  

# the above code is an example of multiple inheritance

class parent:
     a=4

class child1(parent):
    b=2

class child2(child1):
     c=9

ch=child2()
print(ch.a)
print(ch.b)
print(ch.c)  

#  by using super keyword
# 1st example:
 
class parent:
    a=4
    def __init__ (self):
         print("parent")
class child1(parent):
     b=2
     def __init__(self):
         print("cild1")
         super.__init__() 
class child2(child1):
     c=9
     def __init__(self):
         super().__init__()
         print("child2")
ch=child2()
print(ch.a)
print(ch.b)
print(ch.c) 

# 2nd example:

class employee:
     a=10
     b=4
     c=6
     @classmethod
     def setattrs(cls,a,b,c):
         cls.a=a
         cls.b=b
         cls.c=c
emp=employee()
print(employee.a)
print(employee.b)
print(employee.c)
emp.setattrs(1,2,3)
print(employee.a)
print(employee.b)
print(employee.c) 

# a , b, c are class atrributes, they didnt have to anyting with class object .
# here we have changed the class attributes not the instance attributes .

# property decorators.
# example 1:

class employee:
     a=10
     b=4
     c=6
     @classmethod
     def setattrs(cls,a,b,c):
          cls.a=a
          cls.b=b
          cls.c=c

          @property
          def length(self):
              return self.a
emp=employee()
print(employee.a)
print(employee.b)
print(employee.c)
emp.setattrs(1,2,3)
print(employee.a)
print(employee.b)
print(employee.c) 

# example 2 :

class employee:
     a=10
     b=4
     c=6
     @classmethod
     def setattrs(cls,a,b,c):
         cls.a=a
         cls.b=b
         cls.c=c
     @property
     def length(self):
         return self.a
        
emp=employee()
emp.setattrs(1,2,3)
print(emp.length)   

# getters & setters

class employee:
      a=10
      b=4
      c=6
      @classmethod
      def setattrs(cls,a,b,c):
          cls.a=a
          cls.b=b
          cls.c=c
      @property
      def length(self):
          return self.a
        
      @length.setter
      def length(self,value):
          self.a=value

emp=employee()
emp.setattrs(1,2,3)
print(emp.length)
emp.length=78
print(emp.length)  

# dunder methods: 

class employee:
    def __init__(self,a):
         self.a=a
    def __add__(self,obj):
             return self.a + obj.a
        
 a=employee(45)
 b=employee(40)

print(a+b)  

class employee:
     def __init__(self,a, name):
         self.a=a
         self.name= name

     def __add__(self,obj):
             return self.a + obj.a
    
     def __str__(self):
          return self.name
    
     def __len__(self):
          return self.a
        
a=employee(45,"harry")
b=employee(40,"rohan")

print(a,b)   
print(a+b)

print(len(a))
print(len(b))  

# create a class 2d vector and use it to create anoter class representing 3d vector.

class vector2d:
     def __init__(self,i,j):
         self.i=i
         self.j=j

    def printvector(self):
         print(f"{self.i}i+{self.j}j")

class vector3d:
     def __init__(self,i,j,k):
         self.i=k
         super().__init__(i,j,k)
         self.k=k

    def printvector(self):
         print(f"{self.i}i+{self.j}j+{self.k}k")

v2=vector2d(1,5)
v3=vector3d(1,5,9) 

v2.printvecto()
v3.printvector() 

# create a class pets from a class animals and further create class dog from pets. add a method back to class dog.

# create a class employee and add salary and increment properties to it.
# write a method salary after increement with te property decoractor with a setter which changes the value of increment based on the 
# salary.

class employee:
     def __init__ (self, salary, increment):
         self.salary=salary
         self.increment=increment

    @property
    def salaryafterincrement(self):
    return self.salary*(1+self.increment)
    
emp1=employee(12000,0.1)
print(emp1.salaryafterincrement)  

#  write a class complex to represent a complex number along with the overloaded operators + and * operators which adds and multiplies them.

class complex:
     def __init__ (self,a,b):
         self.a=a
         self.b=b
    def __add__(self,obj):
         return complex (self.a + obj.a + self.b,self.b + obj.b)
c1=complex(1,4)
c2=complex(11,3)

#  when we are adding complex number that means we are adding 1 real part and 1 imaginary part .

c3=c1+c2
print(c3.a,c3.b)  

# write a class complex to represent a complex number along with the overloaded operators + and * operators which calculates the sum and the dot product of them.

class vector:
     def __init__(self,l1):
         self.dim=len(l1)
         self.data=l1

    def __add__(self,obj):
         mylist=[]
         for i in range(len(obj.data)):
             mylist.append(obj.data[i]+self.data[i])
             return vector(mylist)
     def __mul__(self,obj):
         dot=0
         for i in range(len(obj.data)):
             dot+=(obj.data[i]*self.data[i])
             return dot 
        
v1=vector([1,2,3])
v2= vector([11,12,13])
v3=v1+v2
v4=v1*v2 
print(v1+v2)  
print(v3.data)   
print(v4)  

# write a str method to print the vector as follows: 
# assume vector of dimenssion 3 for this problem.

# override the len method on vector of problem 5 to display the dimenssion of the vector.

class vector:
    def __init__(self,l1):
         self.data=l1

    def __add__(self,obj):
         mylist=[]
         for i in range(len(obj.data)):
             mylist.append(obj.data[i] + self.data[i])
         return vector(mylist)
    
     def __mul__(self,obj):
         dot=0
         for i in range(len(obj.data)):
             return dot
        
    def __len__ (self):
         return len(self.data)
    
v1=vector([1,2,3])
v2=vector([11,12,13])
v3=v1+v2
v4=v1*v2
print(v3.data)
print(v4)
print(len(v3))  

# advanced python part 1 : 

# in order to avoid the crashing of program we use try except method.

# write a program by using try and except function .

# example 1 : 

try:
    print("hello world")
    a=int(input("entter the number : "))
    b=int(input("entter the  another number : "))
    print(a+b)


except Exception as e:
     print(e)  

 print("there were no errors") 

print("hello world")
a=int(input("entter the number : "))
b=int(input("entter the  another number : "))
print(a+b)
print("there were no errors")  

# example 2 :

try:
    print("hello world")
    a=int(input("entter the number : "))
    b=int(input("entter the  another number : "))
    print(a+b)


except Exception as e:
     print(f"the problem occurred {e}")   
     
    print("there were no errors")  

# whenever there is a problem in a try block except block will be executed 
#  and whhen except block is executed  any  line after te except block will be executed .

# example 3 :

try:
     print("hello world")
     a=int(input("entter the number : "))
    b=int(input("entter the  another number : "))
    print(a+b)

except ValueError:
     print("value error occurred")

except Exception as e:
     print(e)  

print("there were no errors")  

# example 4 :

try:
     print("hello world")
     a=int(input("entter the number : "))
     b=int(input("entter the  another number : "))
     print(a/b)


except Exception as e:
     print(e)  

print("there were no errors") 

# example 5 :

try:
     print("hello world")
     a=int(input("entter the number : "))
     b=int(input("entter the  another number : "))
     print(a/b)

except ValueError:
     print("value error occurred")

except ZeroDivisionError:
    print("this is a zero division error")

except Exception as e:
     print(f"this problem occured : {e}")  

print("there were no errors")  

# example 6 :

try:
     print("hello world")
     a=int(input("entter the number : "))
     b=int(input("entter the  another number : "))
     print(a/b)
     if b>199:
         raise Exception("this number is too large") 

except ValueError:
     print("value error occurred")

 except ZeroDivisionError:
    print("this is a zero division error")

 except Exception as e:
     print(f"this problem occured : {e}")  

 print("there were no errors")  

# try and except clause . so whenver try is successfull else will be executed.

# example 7 :

try:
     print("hello world")
     a=int(input("entter the number : "))
     b=int(input("entter the  another number : "))
     print(a/b)

except ValueError:
     print("value error occurred")

except ZeroDivisionError:
     print("this is a zero division error")

except Exception as e:
     print(f"this problem occured : {e}")  

else:
     print("try was successful")

print("there were no errors")   

#  example 8 :

try:
    a=int(input("entter the number : "))
    b=int(input("entter the  another number : "))

except Exception as e:
     print("this problem occured:{e}")
finally:

    print("i will always be executed") 

# what is the use of finally ?
    
# finally statement will always be executed .
#  it is used to clean up some resources .
# like if tere is some exception occured in te code then by using finally you may clear that excepion by using finally statement.

# example 9 :
    
def function():
     try:
         a=int(input("enter the name :"))
         b=int(input("enter another number : "))
         print(a/b)
         return a/b
    except Exception as e :
print(f"this problem occured : {e}") 
         return 0
    finally:
print("i will always be executed")

# function() 

# example 10:

def function():
     try:
         a=int(input("enter the name :"))
         b=int(input("enter another number : "))
         print(a/b)
         return a/b
    except Exception as e :
         print(f"this problem occured : {e}") 
         return 0
    finally:
print("i will always be executed")

# print(__name__)
# function() 
# if __name__ =='__main__':

# if dunder name == dunder main  is evaluate to true if we are running the particular file from the same module.
    
    # function() 
    # print("main")   

#  write a program by using global keyword.

a=9
def func():
    global a 
# here we ave defined the global keyword and creating te glbal variables from te local scopes
    a=8
    print(a)
    a=900
    print(a)

print(a)
func()
print(a) 

a=[1,5,6,'apple']
for item in a :
     print(item) 

a=[1,5,6,'apple']
i=0
for item in a :
     i=i+1
     print(f"item number {i} is item")   

a= [1,4,6,'apple']
for i , item in enumerate(a):
     print(f"item number {i+0} is {item}")  

# enumerate will display with te index position .

# list comprehensions: 

# 1st method : 
l1=[1,2,3,4,5,6]
l2=[]
for item in l1:
     l2.append(item*item)

# 2nd method :
    
l2=[i*i for i in l1] 
print (l2) 

# 3rd method : 

l2=[i*i for i in l1 if i>2] 
print (l2) 

#  write a program to open tere files 1.txt , 2.txt and 3.txt , if any of the files are not present ,
#  a message without exiting the program must be printed prompted the same.

try:
     with open('1.txt','r') as f:
         f.read()
      with open('2.txt','r') as f:
         f.read()
      with open('3.txt','r') as f:
         f.read()
except Exception as e:
print(f"the file is not present.reason: {e}") 

print("thanks for using this program") 

# write a program to print 3rd , 5th and 7t element from alist using enumurate function.

list1=[1,2,3,4,5,6,7,8,9,10]
for index , item in enumerate(list1):
    if(index+1==3 or index+1==5 or index+1==7):
         print(item) 

# write a list comprehension to print a list which contains the multiplication table if a user entered number .
        
num=int(input("enter a number :"))

multiplication=[i*num for i in range(1,11)]
print(multiplication) 

# write a program to display a/b where a and b are integers. if b=0 , display infinite by handling the zerodivisionerror.

def display_fraction(a, b):
    try:
        result = a / b
        print(f"{a}/{b} = {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero. Result is infinite.")

# Example usage:
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

display_fraction(a, b)


# store the multiplication tables generated in problem 3 in a file named table.txt.

num=int(input("enter a number : "))

multiplication=[i*num for i in range(1,11)]
print(multiplication)

with open('mul.txt','w') as f:
     f.write(str(multiplication)) 

try:
     print("hello world")
     a=int(input("enter a number : "))
     b=int(input("enter another number : "))

except ValueError:
     print("value error occured")
except ZeroDivisionError:
     print("infinite")
except Exception as e:
     print(f"this problem occured : {e}")
print(a/b) 

try:
     print("hello world")
     a=int(input("enter a number : "))
     b=int(input("enter another number : "))
     c=a/b

except ValueError:
     print("value error occured")
except ZeroDivisionError:
     c="infinite"
except Exception as e:
     print(f"this problem occured : {e}")
print(c) 

print("hello world")

# virtual enviroment is a python package .
# activate.ps1 is the script which activates the virtual enviriment .

# syntax for creating the virtual enviroment in python : 

# pip install virtualenv

#  we can create multiple virtual enviroment in python by using the above syntax .

#  pip freeze - this command is used to give all te packages that have been installed in the virtual enviroment in python.

# pip freeze > requirements.txt - all the packages will be displayed in the text format .

# comtypes==1.2.1
# distlib==0.3.8
# filelock==3.13.1
# platformdirs==4.2.0
# pypiwin32==223
# pyttsx3==2.90
# pywin32==306
# virtualenv==20.25.0

# write the program to find out the square of the number .

def square(n):
    return n*n
print(square(4)) 

square = lambda x:x*x
print(square(4))

square = lambda x:x*x
divide = lambda x,y:x/y
print(square(4))
print(divide(9,3)) 

# by using joins in python : 

freinds = ["rohit ","subh","nea","preeti"]

#  performing the joins .

#  write a program to join the characters to the code.

a="--".join(freinds)
print(a) 

freinds = ["rohit ","subh","nea","preeti"]

a="!".join(freinds)
print(a)  

freinds = ["rohit ","subh","nea","preeti"]

a="is a freind of".join(freinds)
print(a) 

# joins will join all the strings and display in the console.

# format method : 

a="i am a good boy and a friend of {}".format("harry")
print(a)  

a="i am a good boy {} and a friend of {}".format("earth" , "harry")
print(a) 

a="i am a good boy {0} and a friend of {1}".format("earth" , "harry")
print(a) 

a="i am a good boy {1} and a friend of {0}".format("earth" , "harry")
print(a) 

# map , filter and reduce methods: 

#  demostration for map : 

square=lambda x:x*x
l=[1,2,3,4,5,6]
c=map(square,l)
print(list(c)) 

#  demostration for filter .

greater=lambda x: x>4
a= [1,2,3,4,5,7,78,58,89]
d=filter(greater,a)
print(list(d))   

#  demostration for reduce.
#  reduce the functiion from functools modules.
# sum is the inbuilt function in python which is used to sum of the numbers.

from functools import reduce
sum=lambda x,y : x+y
a=[1,2,3,4,5,6,7,8] 
d=reduce(sum,a)
print(d)  

# create 2 virtual enviroments , install few packages in the 1st one , ow do you create a similar enviroment in te second one ?

# write a program to input name , marks and phone number of a student and format it using the format function like below:
# the name of the student is harry , his marks are 72 and phone number is 999999988

st="the name of the student is {} , his marks are {} and pone number is {}"
a=st.format("harry",34,9999999988)
print(a) 

# a list contains the multiplication table of 7 , write a program to convert it to a vertical string of a same number(7/14).

a=[i*7 for i in range(1,11)]
st=""
for item in a :
    st+=str(item) +'\n' 
    print(st)   

# write a program to filter a list of numbers which are divisible by 5.

def is_divisible(n):
    if n%5==0:
        return True
    return False
a=[1,2,3,4,5,6,7,8,9,60,10]
print(list(filter(is_divisible,a)))  

# write a program to find the maximum of te numbers in a list using the reduce function .

from functools import reduce 
a=[1,2,3,4,5,6,7,8,9,7,7,6,65,4,5]
def max(m,n):
    if m>n:
        return m
    return n 
maxnum=reduce(max,a)
print(maxnum)

# run pip freeze fro the system interpreter. take the contents and create a similar virtualview.

# comtypes==1.2.1
# distlib==0.3.8
# filelock==3.13.1
# platformdirs==4.2.0
# pypiwin32==223
# pyttsx3==2.90
# pywin32==306
# virtualenv==20.25.0
# the above are the elements which is tere in te virtualview.

# explore the flask module and create a web server using flask and python .

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<pello,World!/p"
app.run() 

# flask is the framework which is used to create the websites in pyton .

#  python -m venv env - this is used to create python virtual enviroment .

# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

# Initialize an empty list to store the numbers
result = []

# Iterate through the range from 1500 to 2700 (inclusive)
for num in range(1500, 2701):
    # Check if the number is divisible by 7 and a multiple of 5
    if num % 7 == 0 and num % 5 == 0:
        # If the condition is met, append the number to the result list
        result.append(num)

# Print the list of numbers
print("Numbers between 1500 and 2700 that are divisible by 7 and multiples of 5:")
print(result)

# Write a Python program to guess a number between 1 and 9.

import random

# Generate a random number between 1 and 9
random_number = random.randint(1, 9)

# Initialize a variable to keep track of the number of guesses
guess_count = 0

# Welcome message
print("Welcome to the Guessing Game! Guess a number between 1 and 9.")

# Start the guessing loop
while True:
    # Prompt the user to guess the number
    guess = input("Enter your guess (or 'exit' to quit): ")

    # Check if the user wants to exit
    if guess.lower() == 'exit':
        print("Exiting the game. The correct number was", random_number)
        break

    # Convert the user's input to an integer
    guess = int(guess)

    # Increment the guess count
    guess_count += 1

    # Check if the guess is correct
    if guess == random_number:
        print("Congratulations! You guessed the correct number in", guess_count, "guesses.")
        break
    elif guess < random_number:
        print("Too low! Try guessing higher.")
    else:
        print("Too high! Try guessing lower.")


# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".  
# For numbers that are multiples of three and five, print "FizzBuzz".
        
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# find the given number is prime or not?

def is_prime(num):
    # If the number is less than 2, it's not prime
    if num < 2:
        return False
    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            # If the number is divisible by any number in this range, it's not prime
            return False
    # If the loop completes without finding a divisor, the number is prime
    return True

# Test the function with a number
number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

# swap 2 number without using thied variable?
    
# 1st method:

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

# 2nd method:

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)

    
# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.
# the numbers obtained should be printed in a comma-separated sequence.

result = []

for num in range(100, 401):
    # Check if all digits of the number are even
    if all(int(digit) % 2 == 0 for digit in str(num)):
        result.append(str(num))

# Join the numbers in the result list with commas and print the sequence
print(",".join(result))


# calculate sum from 1 to given number?

def sum_up_to(n):
    return (n * (n + 1)) // 2

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Calculate the sum from 1 to the given number
result = sum_up_to(num)

# Print the result
print("The sum from 1 to", num, "is:", result)

# REGULAR EXPRESSIONS:

import re
# Meta Charcters
# [] A set of characters"[a-m]"

msg="Hello World "
find=re.findall("[a-r]",msg)
print(find)

# \	Signals a special sequence (can also be used to escape special characters)	"\d"
msg="My Age is 25"
find=re.findall('\d',msg)
print(find)
# .	Any character (except newline character)	"he..o"
msg="Hello World "
x = re.findall("H..o", msg)
print(x)

# ^	Starts with	"^hello"
# Check if the string starts with 'hello':
msg="Hello World "
x = re.findall("^He", msg)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

#Check if the string ends with 'planet':

txt = "hello World"
x = re.findall("ld$", txt)
if x:
  print("Yes, the string ends with 'world'")
else:
  print("No match")


#Check if the string ends with 'planet':
txt = "hello World"
# *	Zero or more occurrences	"he.*o"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*W", txt)

print(x)

# +	One or more occurrences	"he.+o"
txt = "hello"

#Search for a sequence that starts with "he", followed by 1 or more
#  (any) characters, and an "o":

x = re.findall("h.+e", txt)


#?	Zero or one occurrences	"he.?o"

txt = "hegllo World

#Search for a sequence that starts with "he", 
# followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, 
# not one, but two characters between "he" and the "o"

print(x)

# {}	Exactly the specified number of occurrences	"he.{2}o

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)

# |	Either or	"falls|stays"	

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#()	Capture and group
  
# WEBSCRAPPING :

# 1st we will import the modules from packages.

import requests
from bs4 import BeautifulSoup
url = "https://www.javatpoint.com/java-tutorial"

# to fetch data from web page.
# get is a metod of requests which is used to fetch the data from url

r=requests.get(url)
content_1 = r.content
print(r.content)
print(content_1) 

# package is the folder and module is the zip file.
# tree format - it sould be displayed in html format .
# to parse the tml content 

soup = BeautifulSoup(content_1,"html.parser")
# print(soup) 

# what is preetyfy.

# it is also used to give a tree like structure .

print(soup.prettyify)
title=soup.title 
print(title) 

print(title.text)

para = soup.findAll('p')
print(para) 

for p in para:
    print(p) 

#  find all method is used to find all paragraps.

#  ancored is the links or refrences.
    
ancored= soup.findAll('A')
for i in ancored:
    print(i) 

# div is for compartments.
# it is having id.
    
div=soup.findAll('div')
for i in div:
    print(i)   

print(soup.find('div')['id']) 

ancored=soup.findAll('a')
for link in ancored:
    print(link.get("href")) 

#  href is going to give the links.
# href is the refrences.
    
print(soup.find('p').get_text()) 

href=soup.findAll('a')
for link in href:
    print(link.get("href"))   

# 1st method to be called then call the get metod to get all te refrences.
    
print(type(title)) 

# <class 'bs4.element.Tag'> - it is the inbuilt object .

print(type(title.string))   

#  <class 'bs4.element.NavigableString'> - it is the inbuilt object 
#  navigable string is an object .

print(title.string) 

# webscrapping process

import requests

url= "https://www.javatpoint.com/java-tutorial"

# to get content from web page.

#  te page we need to web scaping on we need to copy that URL.


r=requests.get(url)
htmlcon = r.content
print(htmlcon)  

# to get the data in the html format we use beautiful soup.

# beautiful soup

# bs4 is the model and beautiful soup is tee package

from bs4 import BeautifulSoup 

import requests

url= "https://www.javatpoint.com/java-tutorial"
r = requests.get(url)
content=r.content

# parse the html content

content_1 = BeautifulSoup(content,"html.parser")
print(content_1)    

import shutil 

shutil.copy("package.py","package1.py") 

# shutil is used to copy the data.

import shutil 

shutil.copy("package.py","package1.py") 

# FILE HANDLING :

# r -  opens file in read mode - file should be already created to open in read mode.
# w -  opens the file in write mode - if file already present, it will open it in write mode. If the file is not already present, it will create the file by itself.
# a -  opens file in write mode - If you want to have previously entered data and also enter new data, open in append mode.
# x -  create a new file for write only.
# r+ - open the file for read/write. 
# w+ - w+ is a file mode in Python that opens a file for both writing and reading. It overwrites the existing file if it exists, or creates a new file if it does not.
# a+ - The a+ mode in file handling in Python is used to open a file for both appending and reading. This means that you can add new data to the end of the file,
            #  as well as read the existing data from the file. If the file does not exist, it will be created.
# x+ : This mode will read and write the file in the same condition as the x mode.

# Creating a file
            
# file = open("ABC","w")
# file.write("Hello World!!")
# print("Successfully executed")
# file.close()

# Reading the file
            
# file = open("ABC","r")
# data = file.read()
# print(data)
# file.close()

# Creating the file and entering input from the user.
            
# file = open("Demo.txt", "w")
# inputData = input("Enter the data to be inserted in file:")
# file.write(inputData)
# print("Successfully Executed")
# file.close()

# file = open("Demo.txt","r")
# data = file.read()
# print(data)
# file.close()

# Creating a file in specific location as per your requirement.
            
# Method 1 - using r keyword befor path - r stands for raw data
            
# file = open(r"D:\testPython\abc.txt", "w")
# inputData = input("Enter the data to be inserted in file:")
# file.write(inputData)
# print("Successfully Executed")
# file.close()

# Method 2 - using \\ instead of r
            
# file = open("D:\\testPython\\abcd.txt", "w")
# inputData = input("Enter the data to be inserted in file:")
# file.write(inputData)
# print("Successfully Executed")
# file.close()

# file = open("D:\\testPython\\abc.txt","r")
# data = file.read()
# print(data)
# file.close()

# Creating a new file and then copying content from that file into new file
            
# file = open("D:\\testPython\\test.txt", "w")
# inputData = input("Enter the data to be inserted in file:")
# file.write(inputData)
# file = open("D:\\testPython\\test.txt","r")
# data = file.read()
# file = open("D:\\testPython\\test1.txt","w")
# file.write(data)
# file.close()

# Reading a already created file and then copying content from that file into new file and then again reading that file.
            
# file = open("D:\\testPython\\test.txt","r")
# data = file.read()
# file = open("D:\\testPython\\test1.txt","w")
# file.write(data)
# file.close()
# file = open("D:\\testPython\\test1.txt","r")
# data = file.read()
# print(data)
# file.close()

# file = open("D:\\testPython\\testAppend.txt","a")
# inputData = input("Enter the data to be inserted in file:")
# file.write(inputData)
# file.close()


# file = open("D:\\testPython\\testAppend.txt","r")
# data = file.read()
# print(data)
# file.close()

# For copying files/folders we have to use shutil module
            
import shutil

# file = open("Prac.txt","w")
# file.write("Hello World!!")
# file.close()

# file = open("Prac.txt","r")
# data = file.read()
# print(data)
# file.close()

# Copy the content from the file into another file

# shutil.copy("Prac.txt","Prac1.txt")

# Copy the entire file from one folder to another.

# shutil.copytree(r"C:\Users\SHUBHAM\Desktop\Python_File\Sh",r"C:\Users\SHUBHAM\Desktop\Python_File2\tp")

# Why we use shutil(shell utilities) instead of OS(Operating System)
# shutil is platform independent
# os operates according to your operating system.

# For removing/deleting file from a folder we need to use OS module.

# import os
# os.remove(r"C:\Users\SHUBHAM\Desktop\Python_File2\tp\pqr.txt")

# Move file from one location to another

# shutil.move(r"C:\Users\SHUBHAM\Desktop\Python_File\Sh\move.txt",r"C:\Users\SHUBHAM\Desktop\Python_File2\tp")

# copy - copy the file from on folder to another folder 
# remove - use to delete the file from folder
# move - use to move the data from 1 folder to the another folder. 

# webscrapping process: (format)

from bs4 import BeautifulSoup

import requests

url = " copy paste the url"
r= requests.get(url)
content = r.content

# parse the html content

content_1 = beautifulSoup(content , "html.parser")
print(content_1)

anchor =content_ordererd . findAll('a')
i1=0
for a in ancored:
    i1+1
    print(a)
print(i1)

# finding div 

div = content_ordererd.findAll('div')
i2=0
for d in div:
    i2+1
    print(d)
print(i2)

idTag = (content1.find("div")["id"])
print(idTag)

#  getting the links.

l1=[]
ancor = content.findAll("a")
for link in ancor:
    l2 = link.get("href")
    l1.append(l2)
print(l1) 

# adding two lists.

list1=[1,2,3,4,5,6]
list2=[6,7,8,9,9]
print(list1+list2) 


