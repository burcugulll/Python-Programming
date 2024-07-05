def bilgi_al():
    per_sayisi = int(input("Kaç adet personel gireceksiniz? "))
    for i in range(1, per_sayisi + 1):
        bilgi = dict()
        ad_soyad = input("{}. personelin ad soyadını giriniz: ".format(i))
        bilgi['Ad_soyad'] = ad_soyad
        maas = int(input("{}. personelin maaşını giriniz: ".format(i)))
        bilgi['Maas'] = maas
        CS = int(input("{}. personelin çocuk sayısını giriniz: ".format(i)))
        bilgi['CS'] = CS
        eski_zam = int(input("{}. personelin eski zamını giriniz: ".format(i)))
        bilgi['EZam'] = eski_zam
        personel[first_id + i] = bilgi
    print(personel)

def listele():
    for id in personel.keys():
        print("Per ID = {}".format(id), end=" ")
        for per_key in personel[id].keys():
            print("{}={}".format(per_key, personel[id][per_key]), end=" ")
        print()

def yeni_zam_orani():
    for id in personel.keys():
        maas = personel[id]['Maas']
        if maas < 3000:
            zam_orani = 0.20
        elif maas < 4000:
            zam_orani = 0.15
        else:
            zam_orani = 0.10
        yeni_zam = maas * zam_orani + personel[id]['CS'] * 70
        if yeni_zam < personel[id]['EZam']:
            yeni_zam = personel[id]['EZam']
        personel[id]['YeniZam'] = yeni_zam
        personel[id]['YeniMaas'] = maas + yeni_zam

personel = dict()
first_id = 100
bilgi_al()
listele()
yeni_zam_orani()
listele()
