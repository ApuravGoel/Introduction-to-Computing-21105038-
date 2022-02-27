print('               Program 1')
#Tower of Hanoi problem with 3 disks
def TowerOfHanoi(n, source, dest, aux):
    if n == 0:
        return
    TowerOfHanoi(n - 1, source, aux, dest)
    print("Move disk", n, "from source",source, "to rod",dest)
    TowerOfHanoi(n - 1, aux,dest,source)


n = 3
TowerOfHanoi(n, 'A', 'B', 'C')
# A, B, C are the name of rods
print('________________________________________________________')
print('               Program 2')
print('Pascal triangle using recursive approach')

def pt(row,column):
    if column==0 or column==row :
        return 1
    else :
        return pt(row-1,column) + pt(row-1,column-1)
row= int(input("Enter the number of rows of pascal triangle : \n"))
for i in range(row):
    for j in range(row-i-1):
        print(' ',end='')
    for j in range(i+1):
        print(pt(i,j),end=' ')
    print()
print()

print('Pascal triangle using iterative approach')
r= int(input('Enter the no of rows of pascal triangle: \n'))
list_store = []
for i in range(r):
    list1=[]
    for j in range(i+1):
        if j==0 or j==i :
            list1.append(1)
        else :
            list1.append(list_store[i-1][j-1]+list_store[i-1][j])
    list_store.append(list1)

for i in range(r):
    for j in range(1,r-i):
        print(' ',end='')
    for j in range(i+1):
        print(list_store[i][j],end=' ')
    print()
print('___________________________________________________________')
print('               Program 3')
num1= int(input('Enter the first number: \n'))
num2= int(input('Enter the second number: \n'))
quot,rem=divmod(num1,num2)
print(f'The quotient obtained on the divison of {num1} and {num2} is: ',quot)
print(f'The remainder obtained on the divison of {num1} and {num2} is: ',rem)
print('               3a')
# to check whether function is callable
print('To check whether the functions/values are callable or not')
print(callable(divmod))
print('               3b')
print('To check whether the values obtained are non zero or not')
r= divmod(num1,num2)
x= all(r)
print(x)
print('               3c')

result = r + (4,5,6)
print('new result after adding 4,5,6 is : ',result)
res= list()
for i in result :
    if i>4 :
        res.append(i)
print('values greater than 4 are : ',res)

print('               3d')
res1 = set(result)
print('set of the original values is: ',res1)
print('               3e')
res2 = frozenset(res1)
print('The immutable set is: ',res2)
print('               3f')
m = max(res2)
print("The maximum value in the set is: ",m)
print('The hash value is :',hash(m))
print('______________________________________________________________')
print('               Program 4')
class Student :
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        print('Object was created')
        print(f'The name of the student is {self.name} and roll number is {self.roll_no}')

    def __del__(self):
        print(f'Destructor was called and object {self.name} was deleted')

Apurav = Student('Apurav ',21105038)
del Apurav
print('_______________________________________________________________')
print('               Program 5')
class Employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __del__(self):
        print(f"The record of {self.name} is deleted")

employee_1 = Employee('Mehak',40000)
employee_2 = Employee('Ashok',50000)
employee_3 = Employee('Viren',60000)
# 5a
# Updating the salary of Mehak
print('5a ',end='')
employee_1.salary= 70000
print(f'The updated salary of {employee_1.name} is {employee_1.salary}')
print("5b ",end='')
#5b
#Deleting the record of Viren
del employee_3


print('________________________________________________________________')
print('               Program 6')
a = input('The input word of George : \n')
b= input('The Word uttered by Barbie :\n')
def friendship_test(a,b):
    a1=a.lower()
    b1=b.lower()
    a2= ''.join(sorted(a1))
    b2= ''.join(sorted(b1))

    if a2==b2 :
        print('Friendship is real')
    else :
        print('Friendship is fake')
if " " in a or b :
    s=a.split()
    t=b.split()

    if len(s)  == 1 and len(t)== 1 :
        r = a.strip()
        u = b.strip()
        friendship_test(r,u)
    else :
        print('Invalid input')
else :
    friendship_test(a,b)
print('_____________________________End____________________________')    
