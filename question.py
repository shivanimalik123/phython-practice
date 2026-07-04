# name=input("enter your name")
# age=int(input("enter your age"))
# print("Hello", name,)
# print("I am",age,"years old")

# a=int(input("first number"))
# b=int(input("second number"))
# sum=a+b
# print(sum)
# print(a-b)
# print(a*b)
# print(a/b)


# radius = float(input("enter radius"))
# area=3.14 *  radius * radius
# print("area of circle=",area)

# num=4
# if num % 3 == 0:
#     print("even number")
# else:
#     print("odd number")

# a=4
# b=3
# c=6
# if a > b:
#     print("larger")
# elif b < c:
#     print("smaller")
# else:
#     print("equal")

# marks=70
# if marks >= 90:
#     print("Grade A")
# elif marks >=80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grde C")
# else:
#     print("Grade D")

# year=2024
# if year % 4==0:
#     print("leap year")
# else:
#     print("not leap year")

# num=1
# while num <=100:
#     print(num)
#     num += 1

# num=2
# while num <=20:
#     print(num)
#     num += 2

# num=10
# while num >=1:
#     print(num)
#     num -=1

# name=(input("enter a string"))
# if name==name [::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# sentence=input("enter a sentence")
# print(len(sentence))


# name=input("enter your name")
# age=int(input("enter your name"))
# print("hello",name,"i am",age ,"years old")

# radius=float(input("enter a radius"))
# area= 3.14 *radius * radius
# print("area of circle" ,area)

# num=12
# if num % 4==0:
    # print("even number")
# else:
    # print("odd number")

# a=4
# b=3
# a,b=b,a
# print("a",a)
# print("b",b)

# celcius=float(input("enter temperature in celcius"))
# fahrenheit=(celcius * 9/5)+32
# print(fahrenheit)

# radius=float(input("enter area"))
# area= 3.14 * radius *radius
# print("area of circle",area)

# num=6
# if num % 4:
#     print("even number")
# else:
#     print("odd number")

# year=int(input("enter year"))
# if year % 400==0:
#     print("leap year")
# else:
#     print("not leap year")


# for i in range(1,101):
    # print(i)

# i=1
# while i <=10:
    # print("5 x",i,"=", 5 * i)
    # i +=1

# for i in range(1,11):
    # print(i * 5)

# num=10
# while num >=1:
#     print(num)
#     num-=1

# def greet():
#     print("hello ,students")
# greet()

# def my_name(name):
#     print("shivani")
# my_name("name")

# def add_numbers(a,b):
#     print(a+b)
# add_numbers(3,5)

# def check_even_odd(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# check_even_odd(5)

# def square(num):
#     print(num * num)
# square(4)

# def calSum(a):
#     global x
#     x=10
#     sum=a+x
#     return sum
# print(calSum(3))
# print(x)

# def mulOfTwo(a):
#     global x
#     x=4
#     mul=a * x
#     return mul
# print(mulOfTwo(2))
# print(x)


# lambda perameters:expression
# add=lambda a,b : a+b
# print(add(3,4))

# global and local and lambda practice questions

# square=lambda a : a*a
# print(square(4)) 

# add=lambda a,b : a+b
# print(add(5,6))

# cube=lambda a : a**3
# print(cube(2))

# mul=lambda a,b: a*b
# print(mul(2,3))


# x=5

# def show():
#     y=4
#     print(y)
# show()
#  print(x)


# name="Rahul"

# def show():
#     print(name)

# show()

# x=10
# def show():
#     x=20
#     print(x)

# show()
# print(x)


# try: 
#     print(10/0)
# except:
#     print("error")
# finally:
#     print("end")   


# try:
#     x=int("5")
#     print(x)
# except:
#     print("valid no")
# finally:
#     print("end")

# try:
#     num=int(input("enter a no"))
#     print(num / 0)
# except:
#     print("cannot divide")
# finally:
#     print("end")

# try:
#      nums=[10,20,30]
#      print(nums[0])
# except:
#      print("not found")
# finally:
#      print("end")     

# try:
#     num=str(5+"2")
#     print(num)
# except:
#     print("wrong input")
# finally:
#     print("finiish")

# try:
#     print("A")
#     print(10/0)
#     print("B")
# except:
#     print("Error")
# finally:
#     print("Done")


# def divide():
#     try:
#      print(10/0)
#     except:
#      print("error")
#     finally:
#      print("done")

# print("Start")
# divide()
# print("End")


# def a():
#     try:
#         print("A")
#         return
#     except:
#         print("B")
#     finally:
#         print("C")    
# print("Start")
# a()
# print("End")


# function questions
# def show():
#     print("A")

# print("Start")
# show()
# print("End")

# def test():
#     for i in range(1,4):
#         print(i)

# print("X")
# test()
# print("Y")
    
# def fun():
#     print("A")
#     return
#     print("B")

# print("Start")
# fun()
# print("End")

# print("1")
# def so():
#     print("2")
    
# print("3")
# so()
# print("4")

# def test():
#     print("Hello")
#     return "Hi"
#     print("c")

# print(test())


# a=int(input("enter first no."))
# b=int(input("enter second no."))
# sum=a+b
# print(sum)

# length=int(input("enter length"))
# breadth=int(input("enter breadth"))
# area = length * breadth
# perimeter = 2 * (length + breadth)
# print("Area",area)
# print("perimeter",perimeter)


# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# num=int(input("enter a number"))
# if num % 2==0:
#     print("even no")
# else:
#     print("odd no")


# n=int(input("enter a no"))
# square = n * n 
# print(square)

# for i in range(1,11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)


# for i in range(1,11):
#     print("3","x",i,"=",i*3)


# num=5
# if num > 5:
#     print("greater")
# elif num < 5:
#     print("smaller")
# else:
#     print("equal")


# num=-1
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")


# for i in range(1,6):
#     for j in range(i):
#         print("+",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# numbers=[10,20,30]
# print(len(numbers))   

# t=(2,4,5)
# print(len(t))

# student={
#     "name":"shivani",
#     "age": 18,
#     "marks": 90
# }
# print(student)

# s={1,2,3,4}
# print(s)

# f=open("students.txt","w")
# f.write("Hello Students")
# f.close()

f=open("students.txt","w")
f.close()