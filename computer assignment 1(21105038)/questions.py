#program 1

print("                Program 1")
#taking input from the user
numb_1=int(input("enter first number: "))
numb_2=int(input("enter second number: "))
numb_3=int(input("enter third number: "))

sum = numb_1+numb_2+numb_3  #storing the sum of numbers input from the users

#taking average
avg = sum/3

#printing the average calculated
print("The average of numbers is: ",avg)
 
print("__________________________________________________________________________________")          
#program 2
print("                Program 2")

# Given conditions
tax_rate=0.2
standard_deduction=10000
dependent_deduction=3000


 #taking input from the user
Gross_income= float(input("Enter the gross income : "))
dependents=int(input("Enter the number of dependents: "))

#finding the taxable income
taxable_income = Gross_income-standard_deduction-(dependent_deduction*dependents)

#finding the tax
tax = taxable_income*tax_rate

#printing the tax
print("the tax to be paid is :",tax)

print("___________________________________________________________________________________")
#program 3
print("                Program 3")

 #printing the list elements required
print("Student=[SID,Name,Gender,Course Name,CGPA]")

#Student=[SID,Name,Gender,Course_Name,CGPA]
Student=[21105038,'Apurav Goel','M','Electronics and Communication',9.5]

 #printing the list
print(Student)

print("_____________________________________________________________________________________")
#program 4
print("                Program 4")

#taking marks of 5 students
print("Marks of five student : ")
marks = [65,89,45,78,96]

print("marks before sorting : ",marks)

#sorting the marks of 5 students
marks.sort()
print("marks after sorting : ",marks)

print("_________________________________________________________________________________")
#program 5a
print("                Program 5a")

#defining list named color
color = ["Red","Green","White","Black","Pink","Yellow"]

print("list before removing 4th element",color)

 #removing 4 th element
color.pop(3)
print("list after removing 4 th element ",color)


print("___________________________________________________________________________________")
#program 5b
print("                Program 5b")

 #definingg list named color
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("initial list is: ",color)
 #removing black from list
color.pop(3)

 #removing pink from list
color.pop(3)

 #inserting purple in list
color.insert(3,'Purple')

 #printing the final list
print('the final list is ',color)

print("___________________End______________________________")


