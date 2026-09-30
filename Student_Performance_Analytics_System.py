
print("****************Student Performance Analytics System******************")
password= 23456
try:
    enter_password= int(input("Enter the password:- "))

except ValueError:
     print("Please enter a valid number!")
     exit()
if enter_password!=password:
      print("Wrong password!")
      exit()
else:
    print("login successfully")

class studentAnalyzer:
     def __init__(self, name_of_students , num_of_subjects , name_of_exams, student_admission_number, marks ):
          self.name_of_students= name_of_students
          self.num_of_subjects= num_of_subjects
          self.name_of_exams= name_of_exams
          self.student_admission_number= student_admission_number
          self.marks= marks

     def cal_marks(self):
         result= sum(self.marks)
         percentage= result/self.num_of_subjects
         return percentage
          
     def display_details(self):
        result= self.cal_marks()
        print("Name of student :", self.name_of_students)
        print("Number of subjects :", self.num_of_subjects)
        print("Name of exams :", self.name_of_exams)
        print("Student admission number :", self.student_admission_number)
        print("Result:", result)


student1= studentAnalyzer("Ananta Pandey", 5 , "Python , SQL , Numpy & Pandas , System design, Machine learning & AI", 4567890, [97,90,90,97,95])

student2= studentAnalyzer("Aanita Mishra", 5 , "Python , SQL , Numpy & Pandas , System design, Machine learning & AI", 4567891 ,[89,89,91,67,90] )

student3= studentAnalyzer("Aman Yadav", 5 , "Python , SQL , Numpy & Pandas , System design, Machine learning & AI", 4567892 , [40,72,51,57,43])

       
student4= studentAnalyzer("Bhawana Panwar  ", 5 , "Python , SQL , Numpy & Pandas , System design, Machine learning & AI", 4567893 ,[59,78,59,47,50] )

student5= studentAnalyzer("Bhoomi Dalal", 5 , "Python , SQL , Numpy & Pandas , System design, Machine learning & AI", 4567894, [89,88,89,67,60])

student6= studentAnalyzer("Chloe Smith", 5 , "Python , SQL , Numpy & Pandas , System design, Machine learning & AI", 4567895 ,[99,88,89,67,60] )

student7= studentAnalyzer("Charu sharma", 5 , "Python , SQL , Numpy & Pandas , System design, Machine learning & AI", 4567896 , [14,56,46,34,35])

student8= studentAnalyzer("Diya Dariwala", 5 , "Python , SQL , Numpy & Pandas , System design, Machine learning & AI", 4567897,  [59,48,39,37,30])

student9= studentAnalyzer("Dhruv Rathi", 5 , "Python , SQL , Numpy & Pandas , System design, Machine learning & AI", 4567898 , [59,48,89,37,60])

student10= studentAnalyzer("Dev Rathi", 5 , "Python , SQL , Numpy & Pandas , System design, Machine learning & AI", 4567899, [39,48,49,57,60] )

students =[
            student1,
            student2,
            student3,
            student4,
            student5,
            student6,
            student7,
            student8,
            student9,
            student10

         ]

while True:
     user_input= input("1. Show Result \n 2. Indiviual marks   \n 3. Filter Student \n 4.  Show top 3 performers of the year \n 5. Exit \n")
     if user_input=="1":
          student1.display_details()
          print("-"*50)
          student2.display_details()
          print("-"*50)
          student3.display_details()
          print("-"*50)
          student4.display_details()
          print("-"*50)
          student5.display_details()
          print("-"*50)
          student6.display_details()
          print("-"*50)
          student7.display_details()
          print("-"*50)
          student8.display_details()
          print("-"*50)
          student9.display_details()
          print("-"*50)
          student10.display_details()
          print("-"*50)
          
     elif user_input=="2":
          enter_admission= int(input("Enter the admission number of student :- ")) 
          
          for student in students:
               if student.student_admission_number==enter_admission:
                   print(f"(Python , SQL , Numpy & Pandas , System design, Machine learning & AI) {student.marks}")
              
          
     elif user_input=="3":
        user_input= input("1. Students adove 80% \n 2. students below 50% \n 3. failed students \n ")
        
        if user_input== "1":
         found = False
         for student in students:
            if student.cal_marks() > 80:
             print( student.name_of_students )
             print(f"scored : {student.cal_marks()}%")
            print("-"*15)
            found = True
         if not found:
           print("No student found")
        elif user_input=="2":
          found = False
          for student in students:
             if student.cal_marks() < 50:
                print( student.name_of_students )
                print(f"scored : {student.cal_marks()}%")
                print("-"*15)
                found = True 
          if not found:
               print("No student found")

        elif user_input=="3":
          found = False
          for student in students:
             if  student.cal_marks() < 40:
                print( student.name_of_students )
                print(f"scored : {student.cal_marks()}% and  failed the exam")
                print("-"*15)
                found = True 
          if not found:
               print("No student found")


        
     elif user_input == "4":
      if not students:
          print("No students found")
      else:
        
          top_students = sorted(students, key=lambda s: s.cal_marks(), reverse=True)
        
        
          top_3 = top_students[:3]
        
          print("\n----- Top 3 Performers -----")
          for i, student in enumerate(top_3, start=1):
            print(f"{i}. {student.name_of_students} - {student.cal_marks()}%")
            print("-" * 25) 
                    
     
     elif user_input== "5":
         user_exit= input("Do you want to exit this?(yes/no) ").strip().lower()

         if user_exit == "yes":
             print("Exiting......")
             break
         else:
          continue
     else:
         print("Invalid choice")