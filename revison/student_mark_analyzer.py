name="Bishwas"
marks = {
    "Math": 80,
    "Science": 75,
    "English": 68,
    "Computer": 90,
    "Nepali": 72
}

def calculate_average(marks):
  total_marks=sum(marks.values())
  average=total_marks/len(marks)
  return total_marks,average

total_marks,average=calculate_average(marks)

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Student:", name)
print("\nMarks:")

for subject,mark in marks.items():
    print(subject + ":", mark)