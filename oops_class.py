# class Person:
#     def __init__(self, name, age=18):
#         self.name=name
#         self.age=age
# p1 = Person("Email")
# print(p1.age)

# class Student:
#     pass

# class Student:
#     pass
# s1 = Student()

# class Car:
#     pass
# car1 = Car()
# car2 = Car()
# car3 = Car()

# class Student:
#     pass
# s1 = Student()
# s1.name = "Shivani"
# print(s1.name)

# class Student:
#     pass
# s1 = Student()
# s2 = Student()
# s1.name="Ritesh"
# s2.name="hunny"
# print(s1.name)
# print(s2.name)

# class Student:
#     pass
# s1 = Student()
# s1.name="Ram"
# s1.age=18
# s1.marks=78
# print(s1.name)
# print(s1.age)
# print(s1.marks)

# class Mobile:
#     pass
# m1 = Mobile()
# m2 = Mobile()
# m1.brand="Samsung"
# m2.brand="Redmi"
# print(m1.brand)
# print(m2.brand)

# class Book:
#     pass
# b1 = Book()
# b1.title="Python Programming"
# b1.price="458"
# print(b1.title)
# print(b1.price)

# class Student:
#     def display(self):
#         print("Welcome to Python OOP")
# s1 = Student()
# s1.display()

# class Employee:
#     def display(self):
#         print("Name:",self.name)
#         print("Salary:",self.salary)
# e1 = Employee()
# e1.name="Shivani"
# e1.salary=100000
# e2 = Employee()
# e2.name="Anshu"
# e2.salary=58000
# e1.display()
# e2.display()

# class Student:
#     def __init__(self,name,age): 
#      self.name = name
#      self.age = age
# s1 = Student("Anshu",18)
# print("Name:",s1.name)
# print("Age:",s1.age)

# class Employee:
#     def __init__(self,name,id,salary):
#         self.name=name
#         self.id=id
#         self.salary=salary
# e1=Employee("shivani",2,100000)
# e2=Employee("rittu",3,100001)
# print(e1.name,e1.id,e1.salary)
# print(e2.name,e2.id,e2.salary)

# class Car:
#     def __init__(self,brand,model,color):
#         self.brand=brand
#         self.model=model
#         self.color=color
# c1=Car("BMW","X5","Black")
# c2=Car("Defender","D4","Blue")
# print(c1.brand,c1.model,c1.color)
# print(c2.brand,c2.model,c2.color)

# class Book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
# b1=Book("Python Programming","John",500)
# # print(b1.title,b1.author,b1.price)
# print("Title:",b1.title)
# print("author:",b1.author)
# print("Price:",b1.price)

# class Mobile:
#     def __init__(self,brand,model,storage):
#         self.brand=brand
#         self.model=model
#         self.storage=storage
# m1=Mobile("Samsung","S24","256GB")
# m2=Mobile("Redmi","R25","150GB")
# print(m1.brand,m1.model,m1.storage)
# print(m2.brand,m2.model,m2.storage)

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2*(self.length + self.width)
# r1=Rectangle(10,5)
# print("Area:",r1.area())
# print("Perimeter:",r1.perimeter())

# class Student:
#     def __init__(self,name,roll_number,marks):
#         self.name=name
#         self.roll_number=roll_number
#         self.marks=marks
#     def display_result(self):
#         print("Name:",self.name)
#         print("Roll_Number:",self.roll_number)
#         print("Marks:",self.marks)
# s1=Student("Shivani",10,95)
# s1.display_result()

# class Product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def calculate_total(self):
#         return self.price * self.quantity
# p1=Product("Laptop",50000,1)
# print("Product:",p1.name)
# print("Price:",p1.price)
# print("Quantity:",p1.quantity)
# print("Total:",p1.calculate_total())  

# class Movie:
#     def __init__(self,name,director,rating,year):
#         self.name=name
#         self.director=director
#         self.rating=rating
#         self.year=year
#     def display(self):
#         print("Movie:",self.name)
#         print("Director:",self.director)
#         print("Rating:",self.rating)
#         print("Year:",self.year)
#         print()
# m1=Movie("3 Idiots","Rajlumar Hirani",8.4,2009)
# m2=Movie("Dangal","Nitesh Tiwari",8.3,2016)
# m3=Movie("Yevadu","RamChran",9.1,2019)
# m1.display()
# m2.display()
# m3.display()

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Student("Shivani",18)
# print("Name:",s1.name)
# print("Age:",s1.age)


# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Name:",self.name)
#         print("Age",self.age)
# s1=Student("Anu",20)
# s1.display()

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display(self):
#         print("Brand:",self.brand)
#         print("Model:",self.model)
#         print()
# c1=Car("Defender","D4")
# c2=Car("Creta","C4")
# c1.display()
# c2.display()

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length * self.width
# r1=Rectangle(10,2)
# print("Area:",r1.area())

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# dog=Dog()
# dog.sound()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print()
# p1=Person("Suman",35)
# p2=Person("Satish",43)
# p1.display()
# p2.display()

# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance += amount
#         print("Deposited:",amount)
#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:",amount)
#         else:
#             print("Insufficient balance")
#     def display(self):
#         print("Account Holder:",self.account_holder)
#         print("Balance:",self.balance)
# account=BankAccount("Shivani",10000)
# account.deposit(5000)
# account.withdraw(3000)
# account.display()

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department=department
#     def display(self):
#         print("Name:",self.name)
#         print("Salary:",self.salary)
#         print("Department:",self.department)
# m1=Manager("Rishi",290000,"IT")
# m1.display()

# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")
# class Car(Vehicle):
#     def start(self):
#         print("Car starts with a key")
# class Bike(Vehicle):
#     def start(self):
#         print("Bike start with a button")
# car=Car()
# bike=Bike()
# car.start()
# bike.start()

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >=75:
            return"B"
        elif self.marks >=60:
            return"C"
        elif self.marks>=40:
            return"D"
        else:
            return"F"
    def display(self):
        print(self.name,"Grade:",self.calculate_grade())
s1=Student("Shivani",97)
s2=Student("Komal",78)
s3=Student("Vinay",85) 
s1.display()
s2.display()
s3.display()       

        