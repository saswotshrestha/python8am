import random
v = random.randrange(1,3)
a = int(input("rock, paper or scissors(1,2,3): "))
print(a,v)
if a == 1:
    if v == 1:
        print("draw")
    elif v == 2:
        print("you looseeeee")
    else:
        print("youuu WIN!!!")
if a == 2:
    if v == 1:
        print("youuu WIN!!!")
    elif v == 2:
        print("draw")
    else:
        print("you looseeeee")
if a == 3:
    if v == 3:
        print("draw")
    elif v == 2:
        print("youuu WIN!!!")
    else:
        print("you looseeeee")
