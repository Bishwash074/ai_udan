#1 Display the message: 'Welcome to DPLMS Student Registration System'.
print("Welcome to DPLMS Student Registration System.")

#2 Create a list containing these courses: Python with AI/ML, JavaScript, Flutter, and MERN Stack.
course_list=["AI/Ml with python","Javascript","Flutter","MERN stack"]

#3 Use a for loop to display all available courses.
for courses in course_list:
  print(courses)

#4 Ask the user to enter Student Name, Email, Age, and Selected Course
student_name=input("Enter the student name")
email=input("Enter the email")
age=int(input("Enter the age"))
selected_course=input("Enter the secleted course")
print(student_name,
      email,
      age,
      selected_course)

#5 Store the entered information inside a Python dictionary.
student={}
student["student_name"]=student_name
student["email"]=email
student["age"]=age
student["selected_course"]=selected_course
print(student)

#6 Use an if...else statement to check whether the selected course exists in the course list.
if selected_course in course_list:
  print("course exist")
else:
  print("course doesnot exist")

#7 If the course exists, display 'Registration Successful!'; otherwise display 'Course Not Available.'
if selected_course in course_list:
  print("Registration Successful!")
else:
  print("Course Not Available.'")

#8 Print the student's registration details in a clean, formatted output.
if selected_course in course_list:
  print("Registration Successful!")
  print(student_name)
  print(email)
  print(age)
  print(selected_course)
else:
  print("Course Not Available.'")