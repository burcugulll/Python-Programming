#20010011066
#BURCU GÜL
while True:
    print("\n1-İkilik tabandan onluk tabana çevirme\n2-Onluk tabandan ikilik tabana çevirme\n3-Çıkış\n")
    secim=int(input("Islem seciniz: "))
    if secim==1:
        sayi = input("Onluk tabana donusturmek istediginiz sayiyi giriniz: ")
        while True:
            sonuc = 0
            carpan = 1
            for i in sayi:
                if i=="0" or i=="1":
                    sayi=int(sayi)
                    gecici=sayi%10
                    sonuc=sonuc+gecici*carpan
                    sayi=sayi//10
                    carpan=carpan*2
                else:
                    sayi = input("Onluk tabana donusturmek istediginiz sayiyi 1 ve 0 lardan olacak sekilde dogru giriniz: ")
                    break
            if(sayi==0):
                break
        print(sonuc)

    elif secim==2:
        ikilik = " "
        sayi=int(input("İkilik tabana donusturmek istediginiz sayiyi giriniz: "))
        if sayi==0:
            print(sayi)
        while sayi!=0:
           ikilik=str(sayi%2)+ikilik
           sayi=sayi//2
        print(ikilik)


    elif secim==3:
        print("Cikis yaptiniz")
        break

    else:
        print("Hatali numara girdiniz...")
        continue