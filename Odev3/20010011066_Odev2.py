#20010011066
#BURCU GÜL
import random

Kelime_listesi=["system", "data", "algorithm", "such", "base", "node", "model", "case",
"program", "information", "set", "code", "function", "process", "application", "software",
"class", "point", "type", "network", "tree", "object", "element", "input", "operation", "level",
"memory", "table", "order", "file", "variable", "language", "write", "list", "structure",
"compute", "sequence", "computer", "bit", "probability", "machine", "array", "page", "error",
"step", "search", "most", "path", "graph", "web", "length", "several", "security", "proof",
"access", "obtain", "matrix", "task", "image", "form", "return", "interface", "resource",
"address", "implementation", "loop", "first", "read", "location", "hardware", "behavior",
"programming", "field", "key", "parameter", "distribution", "definition", "instance",
"interaction", "internet", "representation", "edge", "stack", "return", "procedure",
"link", "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
"detection", "write", "execute", "least", "key"]
sesli=['a','e','i','o','u']
sessiz=['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','y','z','x','q','w']
tr_harf=['ç','ğ','ı','ö','ş','ü']
kontrol = True
while kontrol:
    puan = 0
    tahmin_sayisi = 0
    kelime = random.choice(Kelime_listesi)
    #print(kelime)
    kelime_uzunluk = len(kelime)
    print("Kelimeniz {} harflidir".format(kelime_uzunluk))

    #kelime uzunluğuna göre tahmin sayisi hesaplama
    if kelime_uzunluk % 2 == 1:
        tahmin_sayisi = (kelime_uzunluk // 2) + 1
    else:
        tahmin_sayisi = kelime_uzunluk // 2
    # _ alanı oluşturuyor
    bos_kelime = "_" * kelime_uzunluk
    print(bos_kelime)

    tahmin_edilen_harfler = []
    while tahmin_sayisi>0 and bos_kelime!=kelime:
        tahmin=input("Harf giriniz:").lower()
        #print(bos_kelime)

        if not tahmin.isalpha() or tahmin in tr_harf:
            print("Geçersiz giriş.Lütfen tekrar bir harf giriniz:")
            continue


        if tahmin in tahmin_edilen_harfler:
            print("Bu harfi girdiniz.Başka bir harf giriniz")
            continue

        tahmin_edilen_harfler.append(tahmin)
        #puan hesaplama
        if tahmin in kelime:
            if tahmin in sesli:
                for i in kelime:
                    if i==tahmin:
                        puan+=3
            if tahmin in sessiz:
                for i in kelime:
                    if i==tahmin:
                        puan+=2
            for i in range(kelime_uzunluk):
                if kelime[i]==tahmin:
                    bos_kelime=bos_kelime[:i]+tahmin+bos_kelime[i+1:]
            print(bos_kelime)
            print("Puan:",puan)
            print("Kalan hak:",tahmin_sayisi)

        else:
            puan+=-4
            tahmin_sayisi-=1
            print("Yanlış tahmin.Kalan hak:",tahmin_sayisi)
            print("Puan:", puan)
            if tahmin_sayisi==0:
                print("Kaybettiniz")
                print("Kelime {} idi".format(kelime))



    if bos_kelime==kelime:
        print("Tebrikler Kelimeyi bildiniz")
        secim=input("Yeni kelime için 1,Çıkış için 2 yi seçiniz: ")
        if secim=='1':
            continue
            kelime = random.choice(Kelime_listesi)
            kelime_uzunluk = len(kelime)
            if kelime_uzunluk % 2 == 1:
                tahmin_sayisi = (kelime_uzunluk // 2) + 1
            else:
                tahmin_sayisi = kelime_uzunluk // 2

            bos_kelime='_'*kelime_uzunluk
            print(bos_kelime)
        else:
            print("Çıkış yaptınız")
            print("Puanın:",puan)
            break
    else:
        break
        print("Kaybettin.Kelime:",kelime)
        print("Puanın:",puan)
        break
