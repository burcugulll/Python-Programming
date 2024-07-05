cift_sayilar = []
asal_sayilar = []
while True:
    sayi = int(input("Sayi gir -> "))
    if sayi == -1:
        break
    elif sayi <= 2:
        print("2 den büyük sayi giriniz")
    elif sayi % 2 == 0:
        cift_sayilar.append(sayi)
    else:
        asal_mi = True
        for i in range(2, sayi):
            if sayi % i == 0:
                asal_mi = False
                break
        if asal_mi:
            asal_sayilar.append(sayi)
for i in range(len(cift_sayilar)):
    for j in range(i + 1, len(cift_sayilar)):
        if cift_sayilar[i] > cift_sayilar[j]:
            cift_sayilar[i], cift_sayilar[j] = cift_sayilar[j], cift_sayilar[i]
for i in range(len(asal_sayilar)):
    for j in range(i + 1, len(asal_sayilar)):
        if asal_sayilar[i] > asal_sayilar[j]:
            asal_sayilar[i], asal_sayilar[j] = asal_sayilar[j], asal_sayilar[i]
print("Asal listesi:", asal_sayilar)
print("Çift listesi:", cift_sayilar)
birlestirilmis_liste = []
i, j = 0, 0
while i < len(cift_sayilar) and j < len(asal_sayilar):
    if cift_sayilar[i] < asal_sayilar[j]:
        birlestirilmis_liste.append(cift_sayilar[i])
        i += 1
    else:
        birlestirilmis_liste.append(asal_sayilar[j])
        j += 1
"""while i<len(asal_sayilar):
    birlestirilmis_liste.append(asal_sayilar[i])
    i+=1
while j<len(cift_sayilar):
    birlestirilmis_liste.append(cift_sayilar[j])
    j+=1"""
if i < len(cift_sayilar):
    birlestirilmis_liste += cift_sayilar[i:]
if j < len(asal_sayilar):
    birlestirilmis_liste += asal_sayilar[j:]
print("Asal veya çift olan sayıların sıralı listesi:", birlestirilmis_liste)