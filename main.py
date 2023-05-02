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

# users = [
#     ['ram','ram002'],
#     ['admin','admin002']
# ]

# nam = input("enter your name")
# pas = input("enter your password: ")

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