cumle = input("Bir cümle giriniz:")
print("Cümledeki kelime sayısı: ", len(cumle.split()))
aranan = input("Aranan kelimeyi giriniz:")
kontrol = 0

for kelime in cumle.split():
    if aranan == kelime:
        kontrol = 1

if kontrol == 1:
    print("Aranan kelime cümle içinde {} defa vardır".format(cumle.count(aranan)))
else:
    print("Aranan kelime cümle içinde yoktur")

cumle = cumle.replace(" ", " ")
print(cumle)
