name="manish"
name2='anish'

names=["manish","anish","nish","ish"] #List datatypes

country="japan"
country1="usa"
country2="nepal"

countries=["japan","usa","nepal"] #list
print(countries[1])
print(countries[-1])
countries.append("indaia") #adds to last of lists
# print(countries)
countries.pop() #removes last item of list
countries.insert(0,"india") #adds to 0 indes(first)
print(countries)
countries.remove("japan") #remove japane
countries[1]="china" #add china to repalce usa
print(len(countries())) #count
print(countries)


countries={"japan","usa","nepal"} #sets are not in order




countries1=("japan","usa","nepal") #tuples
print(countries1[0])
countries1[1]="china" #not working because tuples is immutable
print(countries1.count("japan"))
print(countries1.index("nepal"))


full_name="bishwas dhital"
address="pokhara"
company="digital pathasala"
college="pokhara engineering collefe"

# dictionary
person_information={
  "full_name":"bishwas dhital",
  "address":"pokhara",
  "company":"digital pathshalsa",
  "college":"Pokhara engineering college"
}

person_information["full_name"]
print(person_information)
person_information["color"]="blue" #add the color to the person_infomation 
person_information.pop("college") #remove the college