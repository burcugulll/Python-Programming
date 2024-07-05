import random
rastgele_sayi=random.randint(1,100)
sayac=0
hak=10
print("1 ile 100 arasinda sayi olusturuldu\n")
while sayac<hak:
   alinan=int(input("Tahmininizi giriniz: "))
   sayac+=1
   if alinan==rastgele_sayi:
       break
   elif alinan<rastgele_sayi:
       print("Daha buyuk bir sayi deneyiniz: ")
   else:
       print("Daha kucuk bir sayi deneyiniz: ")

if sayac==hak:
    print("Haklariniz bitti.Sayi {} idi.".format(rastgele_sayi))
else:
    print("Tebrikler.Puaniniz {}".format(hak-sayac))
