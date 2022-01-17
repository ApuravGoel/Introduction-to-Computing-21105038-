# Program 1
print('               Program 1')

#storing a string
inp_str = 'Python is a case sensitive language'

#finding the length of string
print('               1 a')

print('The length of string is : ',len(inp_str))

#Reverse the order of the string
print('               1 b')
s1=inp_str[::-1]
print(s1)

#storing "a case sensitive" in new string
print('               1 c')
s2= inp_str[10:26]
print(s2)

#Replace "a case sensitive" with "object oriented"
print('               1 d')
s3= inp_str.replace('a case sensitive','object oriented')
print('The new string is : ',s3)

#finding the index of substring 'a'
print('               1 e')
s4=inp_str.find('a')
print('The index of substring a is : ',s4)

#Removing white spaces in the string
print('               1 f')
s5=inp_str.replace(' ','')
print('The new string is : ',s5)

print('__________________________________________________________')
#Program 2
print('               Program 2')
name ='Apurav Goel'   #storing name
sid = 21105038 #storing SID
dep_name = 'ECE' #storing department name
cgpa = 9.8 #storing cgpa
# printing the output in desired manner using string formating
name1 = 'Hey, %s Here!'%name
print(name1)
sid1= 'My SID is %s'%sid
print(sid1)
s6='I am from %s department and my CGPA is %s '%(dep_name,cgpa)
print(s6)

print('__________________________________________________________')
#Program 3
print('               Program 3')
a=56
b=10
#using various bitwise operators
print('The value of a&b : ',(a&b))
print('The value of a|b : ',(a|b))
print('The value of a^b : ',(a^b))
print('The value of a after left shift with 2 bits is : ',(a<<2))
print('The value of b after left shift with 2 bits is : ',(b<<2))
print('The value of a after right shift with 2 bits is : ',(a>>2))
print('The value of b after right shift with 4 bits is : ',(b>>4))


print('__________________________________________________________')
#Progam 4
print('               Program 4')
#taking three numbers from users
num1=float(input('Enter the first number: \n'))
num2=float(input('Enter the second number: \n'))
num3=float(input('Enter the third number: \n'))

#finding the greatest number
if num1>num2 :
    if num1>num3 :
        print('The greatest number is : ',num1)
    elif num1==num3 :
        print('The greatest number is : ',num3)
    else :
        print('The greatest number is : ',num3)

elif num1<num2 :
    if num2>num3 :
        print('The greatest number is : ',num2)
    elif num2==num3 :
        print('The greatest number is : ',num3)
    else :
        print('The greatest number is : ',num3)
        
elif num1==num2 :
    if num2>num3 :
        print('The greatest number is : ',num2)
    elif num2==num3 :
        print('The greatest number is : ',num3)
    else :
        print('The greatest number is : ',num3)
        
    
print('_________________________________________________________')
#Program 5
print('               Program 5')

us_str= input('Enter the string : \n')  #string input from user
s7 = us_str.lower() #bringing all the characters to lower case
#finding 'name' in string
if 'name' in s7:
    print('The string contains name')
else :
    print('The string does not contains name')

print('__________________________________________________________')
#Program 6
print('               Program 6')

#taking input of 3 side lengths of triangle from user
s1 = int(input('Enter the first side length : \n'))
s2 = int(input('Enter the second side length : \n'))
s3 = int(input('Enter the third side length : \n'))

#finding whether with the length entered we can form a triangle or not

if s3<s1+s2 and s2<s1+s3 and s1<s2+s3 :
    print('Triangle can be formed')
else :
    print('Triangle cannot be formed')
    
print('________________________End______________________________')    

