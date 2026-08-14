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

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)
r1=Rectangle(10,5)
print("Area:",r1.area())
print("Perimeter:",r1.perimeter())