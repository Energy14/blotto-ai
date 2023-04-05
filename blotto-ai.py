print("First player input:")
a1 = int(input())
a2 = int(input())
a3 = int(input())
print("Second player input:")
b1 = int(input())
b2 = int(input())
b3 = int(input())

if((b1 + b2 + b3)!=6):
    print("Invalid input")

if((a1>b1 and a2>b2) or (a1>b1 and a3>b3) or (a2>b2 and a3>b3)):
    print("First player wins")
elif((a1<b1 and a2<b2) or (a1<b1 and a3<b3) or (a2<b2 and a3<b3)):
    print("Second player wins")
else:
    print("Draw")
