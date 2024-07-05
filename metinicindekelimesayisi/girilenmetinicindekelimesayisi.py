metin=input("bir metin giriniz: ")
kelime_sayisi=1

for i in metin:
    if i==" ":
        kelime_sayisi+=1
print("girdiginiz metinde {} adet kelime var".format(kelime_sayisi))