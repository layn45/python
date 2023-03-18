x=int(input('write a number\n'))
firstx=x
decimal=[]
y=1
pt=[]
exponent=0
while True:
    y+=1
    if x%y==0:
        decimal.append(y)
        x=x/y
        y=1
        continue
    elif firstx==y:
        print(decimal)
        break
    else:
        continue