# students=[]

# while True:
#     print("\n==== Student Management System=====")
#     print("1. Add Student")
#     print("2. View All Students")
#     print("3. Search Student")
#     print("4. Update Student")
#     print("5. Delete Student")
#     print("6. Exit")

#     choice=int(input("Enter Choice: "))

#     if choice==1:
#         sid=int(input("Enter Student ID:"))
#         name=input("Enter Student Name:")
#         age=int(input("Enter Age:"))
#         course=input("Enter Course:")

#         student = [sid,name,age,course] 
#         students.append(student)

#         print("Student Added Successfully !")

#     elif choice == 2:
#         if len(students)== 0:
#            print("No Students Found!")

#         else:
#            for student in students:
#              print("Student ID:",student[0])
#              print("Student Name:",student[1])
#              print("Age:",student[2])
#              print("Course:",student[3])

#         print("-----------------------------")

#     elif choice == 3:
#         sid=int(input("Enter Student ID to  Search: "))
#         found = False

#         for student in students:
#             if student[0] == sid:
#                 print("Student ID:",student[0])
#                 print("Student Name:",student[1])
#                 print("Age:",student[2])
#                 print("Course:",student[3])
#                 found = True
#                 break
      
#         if found == False:
#             print("Student Not Found! ")

#     elif choice == 4:
#         sid=int(input("Enter Student ID To Update: "))
#         found = False
#     for student in students:
#        if student[0]== sid:
#           student[1]=input("Enter New Name: ")
#           student[2]=input("Enter New Age: ")
#           student[3]=input("Enter New Course: ")

#           print("Student Updated Successfully: ")
#           found = True
#           break
#     if found == False:
#        print("Student Not Found! ")

#     elif choice == 5:
#         sid=int(input("Enter Student ID to Delete: "))
#         found = False   

#         for student in students:
#              if student[0] == sid:
#                 students.remove(student)
#                 print("Student Deleted Successfully: ")
#                 found = True  
#                 break   
       
#         if found == False:
#             print("Student Not Found! ")
        
#     elif choice == 6:
#         print("Thank You! ")
#         break






