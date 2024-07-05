#BURCU GÜL
#20010011066
import sys
def menu():
    print("********** MOTOSİKLET EKİPMANLARI SATIŞ OTOMASYONU **********")
    while True:
        print("1-Sipariş Ekleme\n"
              "2-Sipariş Güncelleme\n"
              "3-Sipariş Arama\n"
              "4-Sipariş Silme\n"
              "5-En Pahalı Siparişi Bulma\n"
              "6-Sipariş Listeleme\n"
              "7-Siparis Detaylarını Arama\n"
              "8-Toplam Sipariş Adedi\n"
              "9-Çıkış\n")
        secim = input("İşlem numarası seçiniz:")
        if secim == "1":
            islemler(1)
        elif secim == "2":
            islemler(2)
        elif secim == "3":
            islemler(3)
        elif secim == "4":
            islemler(4)
        elif secim == "5":
            islemler(5)
        elif secim == "6":
            islemler(6)
        elif secim == "7":
            islemler(7)
        elif secim == "8":
            islemler(8)
        elif secim == "9":
            print("ÇIKIŞ YAPTINIZ")
            sys.exit()
        else:
            print("Hatalı bir seçim yaptınız")
def islemler(islemNo):
    if (islemNo==1):
        def siparisEkle():
            try:
                print("********** SİPARİŞ EKLEME **********")
                with open("20010011066.txt","a",encoding="utf-8") as dosya:
                    siparisAdet = int(input("Kaç adet sipariş gireceksiniz: "))
                    siparisler={}
                    for i in range(siparisAdet):
                        siparis = dict()
                        siparisNo= input(f"{i+1}. sipariş numarasi:")
                        siparis1= input(f"{i+1}. sipariş içeriği(ekipman):")
                        adet = input(f"{i+1}. sipariş içeriğinin adeti:")
                        fiyat = input(f"{i+1}. sipariş içeriği fiyat:")
                        adres = input(f"{i+1}. siparişin adresi(il):")
                        siparis["siparis detay"]= siparis1
                        siparis["sipariş içeriğinin adeti"]= adet + " adet"
                        siparis["sipariş fiyat"]= fiyat + " TL"
                        siparis["sipariş adres"]= adres
                        siparisler[siparisNo + " nolu sipariş"] = siparis
                    for key in siparisler.keys():

                        siparisStringi = str(key) + " "

                        for value in siparisler[key].values():
                            siparisStringi += value + " "

                        dosya.write(f"{siparisStringi}\n")

                    print("Sipariş Eklendi.")
            except Exception as e:
                raise Exception("Sipariş ekleme hatası: "+str(e))
        siparisEkle()
    elif (islemNo == 2):
        def siparisGuncelleme():
            try:
                print("********** SİPARİŞ GÜNCELLEME **********")
                with open("20010011066.txt","r",encoding="utf-8") as dosya:
                    durum= None
                    siparisler = {}
                    siparis= []
                    siparisNo = input("Güncellemek istediğiniz sipariş numarasını giriniz:")
                    for line in dosya.readlines():
                        eleman = line.split(" ")
                        key, value = eleman[0], eleman[1:]
                        siparisler[key]=value
                        if siparisNo==key:
                            durum = True
                            siparis1 = input(f"{siparisNo}. siparişin yeni sipariş içeriği(ekipman):")
                            adet = input(f"{siparisNo}.siparişin yeni sipariş içeriği adet:")
                            fiyat = input(f"{siparisNo}. siparişin yeni sipariş içeriği fiyat:")
                            adres = input(f"{siparisNo}. siparişin yeni sipariş adresi(il):")
                            siparis.append("nolu sipariş")
                            siparis.append(siparis1)
                            siparis.append(adet + " adet")
                            siparis.append(fiyat + " TL")
                            siparis.append(adres)
                            siparisler[siparisNo] = siparis
                    if durum:
                        with open("20010011066.txt","w",encoding="utf-8")as ds:
                            for key in siparisler.keys():
                                ds.write(key)
                                for i in range(len(siparisler[key])):
                                    ds.write(" "+siparisler[key][i])
                        print("Güncelleme işleminiz gerçekleşmiştir.")
                    else:
                        print("Güncellemek istediğiniz sipariş bulunamamıştır.")
            except Exception as e :
                raise Exception("Sipariş güncelleme hatası: "+str(e))
        siparisGuncelleme()
    elif (islemNo == 3):
        def siparisArama():
            print("********** SİPARİŞ ARAMA**********")
            with open("20010011066.txt", "r", encoding="utf-8") as dosya:
                siparisler = {}
                siparisNo = input("Aramak istediğiniz sipariş numarasını giriniz:")

                bulduMu = False
                for line in dosya.readlines():
                    eleman = line.split(" ")
                    key, value = eleman[0], eleman[1:]
                    siparisler[key] = value
                    if siparisNo==key:
                        bulduMu = True
                        print(key, end=" ")
                        for i in range(len(siparisler[key])):
                            print(siparisler[key][i], end=" ")
                        print("\n")
                if bulduMu == False:
                    print("Aradğınız sipariş bulunamadı!\n")
        siparisArama()
    elif (islemNo==4):
        def siparisSilme():
            print("********** SİPARİŞ SİLME **********")
            with open("20010011066.txt","r",encoding="utf-8") as dosya:
                durum= None
                siparisler = {}
                siparisNo = input("Silmek istediğiniz sipariş numarasını giriniz:")
                for line in dosya.readlines():
                    eleman = line.split(" ")
                    key, value = eleman[0],eleman[1:]
                    siparisler[key]=value
                    if siparisNo==key:
                        durum = True
                        siparisler.pop(key)
                if durum:
                    with open("20010011066.txt","w",encoding="utf-8")as ds:
                        for key in siparisler.keys():
                            ds.write(key)
                            for i in range(len(siparisler[key])):
                                ds.write(" "+siparisler[key][i])
                    print("Silme işleminiz gerçekleşmiştir.")
                else:
                    print("Silmek istediğiniz sipariş bulunamamıştır.")
        siparisSilme()

    elif islemNo == 5:
        #bu sene yazdığım fonksiyon
        def enPahaliSiparisiBulma():
            print("********** EN PAHALI SİPARİŞİ BULMA **********")
            with open("20010011066.txt", "r", encoding="utf-8") as dosya:
                siparisler = {}
                for line in dosya.readlines():
                    eleman = line.split(" ")
                    key, value = eleman[0], eleman[1:]
                    siparisler[key] = value
                enPahaliSiparis = max(siparisler.items())
                print("En pahalı siparişin nosu:", enPahaliSiparis[0])
                print("En pahalı sipariş olan ürün:", enPahaliSiparis[1][2])
                print("En pahalı siparişin adedi:", enPahaliSiparis[1][3])
                print("En pahalı siparişin fiyatı:", enPahaliSiparis[1][5])
                print("En pahalı siparişin olduğu il:", enPahaliSiparis[1][7])

        enPahaliSiparisiBulma()

    elif (islemNo == 6):
        def siparisListeleme():
            #geçen sene yazdığım fonksiyon
            print("********** SİPARİŞ LİSTELEME **********")
            with open("20010011066.txt","r",encoding="utf-8") as dosya:
                siparisler = {}
                for line in dosya.readlines():
                    eleman = line.split(" ")
                    key, value = eleman[0],eleman[1:]
                    siparisler[key]=value
                for key in siparisler.keys():
                    print(key, end=" ")
                    for i in range(len(siparisler[key])):
                        print(siparisler[key][i], end=" ")
                    print("\n")
        siparisListeleme()

    elif (islemNo == 7):
        # bu sene yazdığım fonksiyon
        def siparisAraDetay():
            print("********** SİPARİŞ DETAYLARINI ARAMA **********")
            with open("20010011066.txt", "r", encoding="utf-8") as dosya:
                siparisler = {}
                siparisDetayi = input("Aramak istediğiniz sipariş detayını giriniz(ürün,şehir,fiyat olabilir):")
                bulduMu = False
                for line in dosya.readlines():
                    eleman = line.split(" ")
                    key, value = eleman[0], eleman[1:]
                    siparisler[key] = value
                    for item in siparisler[key]:
                        if siparisDetayi.lower() in item.lower():
                            print(key, end=" ")
                            bulduMu = True
                            for i in range(len(siparisler[key])):
                                print(siparisler[key][i], end=" ")
                            print("\n")
                if bulduMu == False:
                    print("Aradığınız sipariş detayı bulunamadı!\n")
        siparisAraDetay()

    elif (islemNo == 8):
        # bu sene yazdığım fonksiyon
        def toplamSiparis():
            with open("20010011066.txt", "r", encoding="utf-8") as dosya:
                kayitlar = 0
                for line in dosya.readlines():
                    kayitlar = kayitlar + 1
                print(str(kayitlar) + " tane sipariş var\n")

        toplamSiparis()

menu()
