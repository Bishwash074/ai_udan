#conditional statement

# if condition/scerionor:
#   statement/block of code to be execute
  

age=20

if age>18:
  print("you can vote")

else:
  print("you cannot vote")


password="nepal123"

if password=="nepal123":
  print("login sucess,passwrod matched")
else:
  print("login failed,password didnt matched")


# elif
marks=90
if marks>90:
  print("A+ ayo")
elif marks>=80:
  print("A ayo")
elif marks>=70:
  print("B+ayo")
else:
  print("fail vayo")


#Login system-->email,password
#  email,password
email="hello@gmail.com"
password="hello123"

# if email=="hello@gmail.com":
#   if password=="hello123":
#     print("login sucessfully,match vayo")
if email=="hello@gmail.com" and password=="hello123":
  print("login sucessfully,match vayo")
else:
  print("login failed")


#loops
# for loop->more used
# while loop
# for i in range(0,5):
#   print(i)

for i in range(10,0,-1):
  print(i)

countries=["japan","usa","nepal"]

for country in countries:
  print(country)

predeication_score=[77,99,23,67]
#loop prdeication_scores,and jasko value greater than 80 xa teslai good banyerw print garnye else not good score
for score in predeication_score:
  if score>80:
    print(score,"Good score")
  else:
    print(score,"Bad score")

emails_list=[
  "Bhatbhateni ma discount",
  "yeti aitlines free ticket congrats jityo",
  "What is the project update guys?",
  "Congratution,you won the rolex watch"
]

for email in emails_list:
  if "congrats" in email or "discount" in email or "Congratution" in email:
    print("spam ho:",email)
  else:
    print("Not spam",email)