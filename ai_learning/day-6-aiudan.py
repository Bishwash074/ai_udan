#function
# function vaneko a blok of code raixa ,jasko sayatw bata hamile code repetion lai kaam garna sakxam
# manegable banauna sakxam,sharing easy  parna sakxam
# how we can achive DRY principle

def greet(name):
  print("hello"+name)
 
greet("anish")
greet("manish")
greet("nish")


# return
def add(a,b):
  return a+b

sum=add(3,2)
print(sum)

def student():
  return "Mansih",23,"Itahari"

data=student() #or name,age,location=student()
print(data)

def say_hello(name="manish"):
  print("hello"+name)

say_hello()


# parameter and argument in function

#to get different output we use parameter and argument
# parameter->recive garnye placeholder receiver side bata k k liney b=vanne kura
# argument->tapaile dinye data/value 

# lambda function
# syntax
# lambda num:num*num
num = 2
result = lambda num: num * num
print(result(num))



