print('               Program 1')
str1=input('Enter the string: \n') #taking the input from user
str=str1.lower()
def single_str(str):    #making a function to count the number of occurence of characters if string entered is single word

    counts= dict()
    if " " not in str:
       for i in  str:
          if i not in counts :
              counts[i]=1
          else :
              counts[i]=counts[i]+1
       print('The occurences of characters in string are as follows : ')
       
       for a in counts:
          print(a,counts[a])
    else :
        return 0
def multi_str(str):  #making a function to count the number of occurence of word in the string
    sp = str.split()
    if len(sp)==1:
        single_str(sp[0])
    else:
        counts=dict()
        for i in sp:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] = counts[i] + 1
        print('The occurences of words in string are as follows : ')
        
        for a in counts:
            print(a, counts[a])

# invoking functions according to the string entered
if " " in str:
    multi_str(str)
else :
    single_str(str)
print('_______________________________________________________________________')
print('               Program 2')
day = int(input('Day - '))        #input day from user
mon = int(input('Month - '))      #input month from user
year = int(input('Year - '))      #input year from user
def leap_year(year):              #defining a function to check whether year entered is leap year or not
    if(year%4==0 and year%100 !=0):
        return True
    elif(year%400==0 and year%100==0):
        return True
    else:
        return False
if 1<=mon<=12 and 1<=day<=31 and 1800<=year<=2025 :
    if mon in (1,3,5,7,8,10):     #if condition for months having 31 days
        if day==31:
            print('Next Date is : 1/',(mon+1),'/',year)
        else :
            print('Next Date is : ',(day+1),'/',mon,'/',year)
    if mon in (2,)  :             #if condition for february month
        if leap_year(year)==True :
            if day==29:
                print('Next Date is : 1/', (mon + 1), '/', year)
            elif day<29 :
                print('Next Date is : ', (day + 1), '/', mon, '/', year)
            else :
                print('Invalid input : The month has only 29 days')
        else :
            if day==28 :
                print('Next Date is : 1/', (mon + 1), '/', year)
            elif day<28 :
                print('Next Date is : ', (day + 1), '/', mon, '/', year)
            else :
                print('Invalid input : The month has only 28 days')
    if mon in (4,6,9,11):         #if condition for months having 30 days
        if day==30:
            print('Next Date is : 1/',(mon+1),'/',year)
        elif day<30 :
            print('Next Date is : ',(day+1),'/',mon,'/',year)
        else :
            print('Invalid input : The month has only 30 days')
    if mon in (12,) :             #if condition for december month
        if day==31:
            print('Next Date is : 1/ 1 /',(year+1))
        else :
            print('Next Date is : ',(day+1),'/',mon,'/',year)
else : #condition to print error for input not of given format
    print("Invalid input")
    print('For valid input : 1<=month<=12 and 1<=day<=31 and 1800<=year<=2025')
print('_______________________________________________________________________')
print('               Program 3')

n= int(input('Enter the number of elements  you want to enter in the list \n'))  #taking number of elements in the list from user
i=1
ls= list()
while i<=n :
    num=int(input('Enter the number you want to add to list \n'))  #taking number from user to be added in the list
    
    ls.append(num)                                             #adding the number entered in the list
    i+=1
ls.sort()
st= list()  #creating an empty list
# using for loop to store squares into empty list
for i in ls :
    st.append(i**2)
#creating a list of tuples 
g = list(zip(ls,st))
print(g)
print('_______________________________________________________________________')
print('               Program 4')
gp1 = float(input('Enter your grade point \n'))  #input grade points of user
gp= int(gp1)    #converting grade points to integer data type
if 4<=gp1<=10 :
    if gp==10 :
        print('Your Grade is \'A+\'and Outstanding Performance')
    if gp==9 :
        print('Your Grade is \'A\'and Excellent Performance')
    if gp == 8:
        print('Your Grade is \'B+\'and Very Good Performance')
    if gp == 7:
        print('Your Grade is \'B\'and Good Performance')
    if gp == 6:
        print('Your Grade is \'C+\'and Average Performance')
    if gp == 5:
        print('Your Grade is \'C\'and Below Average Performance')
    if gp == 4:
        print('Your Grade is \'D\'and Poor Performance')
else :   #condition to print error for invalid input
    print('Invalid input')
    print('For valid input : 4<=Grade points<=10 ')
print('_______________________________________________________________________')
print('               Program 5')

def pattern(n):
    k=n
    for i in range(0,n):      #loop to control no of rows
        num=65                #ASCII value for A
        b=k*2-1               #variable to control no of columns
        for j in range(0,i):  #loop to control no of spaces
            print(' ',end='')

        for j in range(0,b):  #loop to control no of columns
            ch=chr(num)
            print(ch,end='')
            num+=1
            
        print('\r')  #moving to next row
        k=k-1
pattern(6)   #invoking a function pattern
print('________________________________________________________________________')
print('               Program 6')
# 6a adding students details and printing them
dic = dict()
while True:
    choice1 = input('If you want to enter name and Sid press Y else N \n')
    choice = choice1.upper()
    if choice=='Y':
        SID= int(input('Enter your SID : \n'))
        name = input('Enter your name \n')
        name = name.upper()
        dic[SID]=name
    elif choice == 'N':
        break
    else :
        print('You have entered a wrong input')
print('Students details are as follows :')
if len(dic)==0 :
    print('No Student detail entered')
else :
    for i in dic:
        print(i,":",dic[i])
#6b sorting by students name
print()
print("Students details after sorting by name")
lst1  = sorted(dic.items(),key= lambda x:x[1])
d1 = dict(lst1)
print(d1)
for i in d1 :
    print(i,":",d1[i])
#6c sorting by  SID
print()
print('Students details after sorting by SID')
lst2  = sorted(dic.items(),key= lambda x:x[0])
d2 = dict(lst2)
print(d2)
for i in d2 :
    print(i,":",d2[i])
# 6d searching student details
def search():
    s=int(input('Enter the SID of the Student \n'))
    if s in dic :
        print("The name of the student is : ",dic[s])
    else :
        print('This student is not in the list')
sear= input('Enter Y to search students details and N to not search \n')
sear1 = sear.upper()
if sear1 == 'Y':
    search()
    while True :
        n1= input('Press Y to search again and N to stop search \n')
        n = n1.upper()
        if n=='Y':
            search()
        elif n=='N':
            break
        else :
            print('Wrong input')
else :
    exit()
print('_________________________________________________________________')    
print('               Program 7')
def fibo(i):      #defining a function to calculate the element of fibonacci sequence
    if i==0 :
        return 0
    elif i==1 :
        return 1
    else :
        return fibo(i-1) + fibo(i-2)
n = int(input('Enter the number of elements in the fibonacci sequence \n'))
print('The fibonacci sequence is :')
for i in range(0,n) :   # loop to print fibonacci sequence
    print(fibo(i),end=" ")
print()
a=0
for i in range(0,n):
    a += fibo(i)
avg = a/n            #calculating the average of resultant fibonacci series
print("The average of resultant fibonacci series is : ",avg)
print('__________________________________________________________________')
print('               Program 8')
set1= {1,2,3,4,5}
set2= {2,4,6,8}
set3={1,5,9,13,17}
#8a
n1= set1^set2 #symmetric difference
print('The new set of all elements that are in Set1 and Set2 but not both is ',n1)
#8b
n2 = set1^set2^set3
print('The new set of all elements that are in only one of the three sets Set1,Set2 and Set3 is ',n2)
#8c
n3= (set1|set2|set3)-(set1^set2^set3)-(set1&set2&set3)
print('The new set of elements that are exactly two of the sets Set1, Set2 and Set3 is ',n3)
#8d
n4=set()
for i in range(1,11):
    if i not in set1 :
        n4.add(i)
print('The new set of all integers in the range 1 to 10 that are not in Set1 is ',n4)
#8e
n5=set()
for i in range(1,11):
    if i not in (set1|set2|set3):
        n5.add(i)
print('The new set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3 is ',n5)
print('____________________  End__________________________________________')




