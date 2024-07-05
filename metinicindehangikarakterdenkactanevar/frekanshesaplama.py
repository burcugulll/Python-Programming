frekans=""
metin=input("bir metin giriniz: ")

for i in range(len(metin)):
    sayac=0
    for karakter in metin:
        if karakter == metin[i]:
            sayac+=1
    frekans+=str(sayac)

print(metin)
print(frekans)