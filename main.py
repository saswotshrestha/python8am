# print("hello")
# print(45)

# x=10

# print(x)

# name = input("Enter name: ")
# print(name)

#x=10
#y=20

#if x>y:
 #   print("x is large")

#else:
 #   print("y is large")

# age = int(input("Enter age: "))
# if age >= 18 and age <= 40:
#     print("you can join the party")
#     if age >= 18 and age <= 25:
#         print ("you can drink coke")
#     elif age > 25:
#         print ("you can drink beer")
# else:
#     print("you cannot join the party")

# x = 7
# y = 8
# z = 9
# if x > y:
#     if x > z:
#         print ("x is greatest")
# if y > z:
#     if y>x:
#         print ("y is greater")
# else:
#     print ("z is greater")

# print ("Welcome to ATM")
# pin = 123
# amt = 10000
# check = int(input("enter your pin"))
# if check == pin:
#     print ("your amount is: ", amt)
#     wamt = int(input("how much do you want to withdraw: "))
#     if wamt > amt:
#         print ("you cannot withdraw more than your bank amount")
#     else:
#         amt = amt - wamt
#         print ("you have ", amt ," rupees" )
# else:
#     print ("wrong pin")

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# if a > b:
#     if b > c:
#         print (a,b,c)
#     else:
#         print(a,c,b)

# if b > a:
#     if a > c:
#         print (b,a,c)
#     else:
#         print (b,c,a)

# if c > a:
#     if a>b:
#         print(c,a,b)
#     else:
#         print(c,b,a)
# students = [
#     {'name': 'ram','age': 20},
#     {'name': 'shyam','age': 21},
#     {'laxmi'}
# ]

# print (f"my name is {students[0]['name']}",f" my age is {students[0]['age']}")
# print (f"my name is {students[1]['name']}",f" my age is {students[1]['age']}")

# data = [
#     {'name': 'ram', 'gender': 'male', 'status': True,
#      "address": {
#          "country": "nepal",
#      }
#      },
#     {'name': 'sita', 'gender': 'female', 'status': True,
#      "address": {
#          "country": "pokhara",
#      }
#      },
#     {'name': 'laxmi', 'gender': 'female', 'status': True,
#      "address": {
#          "country": "kathmandu"
#      }
#      },
# ]

# print (f"my name is {data[0]['name']} and i live in {data[0]['address']['country']}")
# print (f"my name is {data[1]['name']} and i live in {data[1]['address']['country']}")
# print (f"my name is {data[2]['name']} and i live in {data[2]['address']['country']}")

# a = input("enter first num: ")
# b = input("enter second num: ")
# c = input("enter third num: ")

# if a > b and a > c:
#     if b > c:
#         print(a,b,c)
#     else:
#         print(a,c,b)
# elif b > c and b > a:
#     if a > c:
#         print(b,a,c)
#     else:
#         print(b,c,a)
# else:
#     if b> a:
#         print(c,b,a)
#     else:
#         print(c,a,b)

# users = [
#     ['ram','ram002'],
#     ['admin','admin002']
# ]

# nam = input("enter your name: ")
# pas = input("enter your password: ")

# if nam == users[0][0] and pas == users[0][1]:
#     print ("welcome ram")
# elif nam == users[1][0] and pas == users[1][1]:
#     print ("welcome admin")
# else:
#     print("wrong")

# data ={
#     'name':'',
#     'email':'',
#     'address':'',
# }

# data['name']= input("name: ")
# data['email'] = input("email: ")
# data['address'] = input("address: ")

# print(data)

# users = [
#     {'username':'admin','password':'admin123'},
#     {'username':'ram','password':'ram002'}
# ]

# u = input("enter username: ")
# pas = input("enter password: ")

# if u == users[0]['username'] and pas == users[0]['password']:
#     print("welcome admin")
# elif u == users[1]['username'] and pas == users[1]['password']:
#     print("welcome ram")
# else:
#     print("password or username incorrect")

# n = int(input('enter a number: '))
# if n % 3 == 0 and n % 5 == 0:
#     print('it is divisible by 3 and 5')
# elif n % 3 == 0 and n % 5 != 0:
#     print('it is divisible by 3 but not 5')
# elif n % 3 != 0 and n % 5 == 0:
#     print('it is divisible by 5 but not 3')
# else:
#     print('it is not divisible by 5 and 3')

#loop: for ,while ,nested loop

# data = ['ram', 'sita', 'hari', 'gita', 'laxmi','rama']
# count = 0
# for i in data:
#     count = count + 1
# print(count)

# number = [1 , 2 ,3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 ,13]
# evn = 0
# for i in number:
#     if i % 2 == 0:
#         evn += 1
# odd = len(number) - evn
# print(f"there are {evn} even numbers")
# print(f"there are {odd} odd numbers")

# data =['ram','sita','hari','gita','laxmi']
# i = 1
# for x in data:
#     if i == 1 or i == 5:
#         print(x)
#     i += 1

# evn = 0
# odd = 0
# for i in data:
#     for j in i:
#         if j % 2 == 0:
#             evn += 1
#         else:
#             odd += 1
# print("even: ",evn)
# print("odd: ",odd)

# data = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13,14,14]
# ]

# for i in range(3):
#     print(data[i][0])

# a = int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{a} x {i} =",a*i)

# data = [
#     {'name': 'ram', 'age': 20,'gender':'male','status':True},
#     {'name': 'sita', 'age': 21,'gender':'female','status':True},
#     {'name': 'hari', 'age': 21,'gender':'male','status':True},
#     {'name': 'gita', 'age': 21,'gender':'female','status':False},
#     {'name': 'madan', 'age': 21,'gender':'male','status':False},
# ]

# total = 0
# tot_active = 0
# tot_inactive = 0
# tot_active_male = 0
# tot_inactive_male = 0
# tot_active_female = 0
# tot_inactive_female = 0

# for i in range(len(data)):
#     total += 1
#     if data[i]['status'] == True:
#         tot_active += 1
#     else:
#         tot_inactive += 1

#     if data[i]['status'] == True and data[i]['gender'] == 'male':
#         tot_active_male += 1
#     elif data[i]['status'] != True and data[i]['gender'] == 'male':
#         tot_inactive_male += 1

#     if data[i]['status'] == True and data[i]['gender'] == 'female':
#         tot_active_female += 1
#     if data[i]['status'] != True and data[i]['gender'] == 'female':
#         tot_inactive_female += 1

# print("total users: ",total)
# print("total active users: ",tot_active)
# print("total inactive users: ",tot_inactive)
# print("total active male users: ",tot_active_male)
# print("total inactive male users: ",tot_inactive_male)
# print("total active female users: ",tot_active_female)
# print("total inactive female users: ",tot_inactive_female)

# t = int(input("how many numbers: "))
# num = 1
# evn = 0
# while num <= t:
#     anum = int(input("enter mumber: "))
#     if anum % 2 == 0:
#         evn += 1
#     num += 1
# print(f"there are :{evn} even numbers")
# print(f"there are {t - evn} odd numbers")

# data = []
# sum = 0
# times = int(input("how many numbers: "))
# while times > 0:
#     num = int(input("enter number: "))
#     data.append(num)
#     times -= 1
# for i in range(0,len(data),2):
#     sum = sum + data[i]
# print(sum)

# nos = int(input("enter number of student: "))
# while nos != 0:
#     eng = int(input("enter your marks in english: "))
#     nep = int(input("enter your marks in nepali: "))
#     sci = int(input("enter your marks in science: "))
#     mth = int(input("enter your marks in math: "))
#     comp = int(input("enter your marks in computer: "))

#     tot = eng + nep +sci+mth+comp
#     per = tot / 5

#     if per > 35 and per < 45:
#         print("you got third division")
#     elif per > 45 and per < 60:
#         print("you got second division")
#     elif per > 60 and per < 75:
#         print("you got first division")
#     elif per > 75 and per <= 100:
#         print("you got distintion division")
#     else:
#         print("you have failed")
#     print ("anotehr student")
#     nos -= 1

# data = []
# ans = ""
# mal = 0
# fem = 0
# while ans != "no":
#     nam = input("your name: ")
#     gen = input("your gender(male/female): ")
#     data.append([nam,gen])
#     if gen == "male":
#         mal += 1
#     else:
#         fem += 1
#     ans = input("again(yes/no): ")
# print(f"male: {mal}")
# print(f"female: {fem}")
# print(f"total users: {len(data)}")
# data = []

# data = ['ram','sita','hari','gita','madan']
# a = 0
# for i in data:
#     print(i[a])
#     if a == 0:
#         a = -1
#     elif a == -1:
#         a = 0
