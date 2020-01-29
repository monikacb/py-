import random
num=random.randrange(2,4)
a=int(input("guessing the random number:"))
print(a)
if(a==num):
    print("guessing number is matched")
elif(a>=num):
    print("high guessing number")
else:
    print("invalid number")
