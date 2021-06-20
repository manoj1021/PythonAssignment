
lis1 = []
for i in range(1999,3201):
    if i%7 == 0 and i%5 !=0:
        lis1.append(i)

for j in range(0,len(lis1)):
    print(lis1[j],end=",")