#20010011066
#BURCU GÜL
boyut=int(input("Boyut giriniz:"))
for i in range(1,boyut+1):
    for j in range(1,boyut+1):
        if i==1 or j==1 or i==boyut or i==boyut//2+1 or j==boyut:
            print("*",end="")
        else:
            print(" ",end="")
    print(" ")
print()
for i in range(1,boyut+1):
    for j in range(1,boyut+1):
        if j==1 or j==boyut or i==boyut:
            print("*",end="")
        else:
            print(" ",end="")
    print(" ")
print()
for i in range(1,boyut+1):
    for j in range(1,boyut+1):
        if i==1 or j==1 or i==boyut//2+1 or (j==boyut and i<=(boyut+1)/2) or (i>=(boyut+1)/2 and i==j) :
            print("*",end="")
        else:
            print(" ",end="")
    print(" ")
print()
for i in range(1,boyut+1):
    for j in range(1,boyut+1):
        if i==1 or j==1 or i==boyut:
            print("*",end="")
        else:
            print(" ",end="")
    print(" ")
print(" ")
for i in range(1,boyut+1):
    for j in range(1,boyut+1):
        if j==1 or j==boyut or i==boyut:
            print("*",end="")
        else:
            print(" ",end="")
    print(" ")