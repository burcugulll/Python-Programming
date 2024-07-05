#BURCU GÜL
#20010011066
import random

ekran = []
alan = 0
gizli_ekran = []
boyut = 0
puan = 0

def OyunAlaniOlustur():
    global ekran, gizli_ekran, boyut,puan,alan
    ekran = []
    gizli_ekran = []
    puan = 0

    boyut = int(input("Boyut giriniz (Min 10) : "))
    for i in range(boyut):
        ekran.append(["?"] * boyut)
        gizli_ekran.append(["?"] * boyut)
    alan = round(boyut * boyut * 3 / 10)
    mayin_sayisi = 0
    while mayin_sayisi < alan:
        random_satir = random.randint(0, boyut - 1)
        random_sutun = random.randint(0, boyut - 1)
        if ekran[random_satir][random_sutun] == "?":
            ekran[random_satir][random_sutun] = "X"
            mayin_sayisi += 1

def OyunOyna():
    global hamle

    while True:
        OyunAlaniOlustur()
        print("1-Gizli Mod (Mayinlar gözükmez) oynamak icin 1'e basin")
        print("2-Acik Mod (Mayinlar gözükür) oynamak icin 2'ye basin")
        mod = 0
        while True:
            mod = int(input("Modu seciniz:"))
            if mod not in [1, 2]:
                print("Yanlış seçim !!  tekrar deneyin.\n ")
                continue
            else:
                break

        while True:
            global puan
            if mod == 1:
                OyunAlaniniGoster(gizli_ekran)
                satir = int(input("Hangi satırı girmek istiyorsunuz:"))-1
                sutun = int(input("Hangi sutunu girmek istiyorsunuz:"))-1
                # köse kontrolu
                if gizli_ekran[satir][sutun] in range(0, 9):
                    print("Burayı daha önce açtınız. Yeni alan giriniz.\n")
                    continue

                if puan == (boyut * boyut) - alan:
                    print("\noyunu kazandınız puanınız:{}".format(puan))
                    break

                if ekran[satir][sutun] == "?":

                    puan += 1
                    cevre_mayin = 0

                    # sol üst köşe
                    if satir == 0 and sutun == 0:

                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun + 1] == "X":
                            cevre_mayin += 1

                        gizli_ekran[satir][sutun] = cevre_mayin

                    # sağ üst köse
                    elif (satir == 0) and (sutun == (boyut - 1)):

                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun - 1] == "X":
                            cevre_mayin += 1

                        gizli_ekran[satir][sutun] = cevre_mayin

                    # sol alt köşe
                    elif satir == boyut - 1 and sutun == 0:
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        gizli_ekran[satir][sutun] = cevre_mayin
                    # sağ alt köşe
                    elif satir == boyut - 1 and sutun == boyut - 1:
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        gizli_ekran[satir][sutun] = cevre_mayin
                    # üst kenar
                    elif satir == 0 and (sutun != 0 or sutun != boyut - 1):
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        gizli_ekran[satir][sutun] = cevre_mayin
                    # sol kenar
                    elif (satir != 0 or satir != boyut - 1) and sutun == 0:
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        gizli_ekran[satir][sutun] = cevre_mayin
                    # sağ kenar
                    elif (satir != 0 or satir != boyut - 1) and sutun == boyut - 1:
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        gizli_ekran[satir][sutun] = cevre_mayin
                    # alt kenar
                    elif satir == boyut - 1 and (sutun != 0 or sutun != boyut - 1):
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        gizli_ekran[satir][sutun] = cevre_mayin
                    # köşe veya kenar değilse
                    elif (satir != 0 or satir != boyut - 1) and (sutun != 0 or sutun != boyut - 1):
                        if ekran[satir - 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        gizli_ekran[satir][sutun] = cevre_mayin


                else:
                    print("Mayına bastınız oyun bitti")
                    print("Puanınız:{}".format(puan))

                    for satir in range(0, boyut):
                        for sutun in range(0, boyut):
                            if gizli_ekran[satir][sutun] in range(0, 9):
                                ekran[satir][sutun] = gizli_ekran[satir][sutun]

                    OyunAlaniniGoster(ekran)
                    secim = 0
                    while True:
                        print("Tekrar oynamak için (1), Çıkmak için (2)")
                        secim = int(input("Seçim:"))
                        if secim not in [1, 2]:
                            print("Yanlış seçim yaptınız tekrar seçin!! \n ")
                            continue
                        else:
                            break
                    if secim == 1:
                        print("\n\n")
                        break
                    elif secim == 2:
                        return

                if puan == (boyut * boyut) - alan:
                    print("Tebrikler oyunu kazandınız puanınız:{}\n".format(puan))
                    while True:
                        print("Tekrar oynamak için (1), Çıkmak için (2)")
                        secim = int(input("Seçim:"))
                        if secim not in [1, 2]:
                            print("Yanlış seçim yaptınız tekrar seçin!! \n ")
                            continue
                        else:
                            break
                    if secim == 1:
                        print("\n\n")
                        break
                    elif secim == 2:
                        return
            if mod == 2:
                OyunAlaniniGoster(ekran)
                satir = int(input("Hangi satırı girmek istiyorsunuz:"))-1
                sutun = int(input("Hangi sutunu girmek istiyorsunuz:"))-1
                # köse kontrolu

                if ekran[satir][sutun] in range(0, 9):
                    print("Burayı daha önce açtınız.Yeni alan giriniz")
                    continue

                if ekran[satir][sutun] == "?":

                    puan += 1
                    cevre_mayin = 0

                    # sol üst köşe
                    if satir == 0 and sutun == 0:
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun + 1] == "X":
                            cevre_mayin += 1

                        ekran[satir][sutun] = cevre_mayin

                    # sağ üst köse
                    elif (satir == 0) and (sutun == (boyut - 1)):
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun - 1] == "X":
                            cevre_mayin += 1

                        ekran[satir][sutun] = cevre_mayin
                    # sol alt köşe
                    elif satir == boyut - 1 and sutun == 0:
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        ekran[satir][sutun] = cevre_mayin
                    # sağ alt köşe
                    elif satir == boyut - 1 and sutun == boyut - 1:
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        ekran[satir][sutun] = cevre_mayin
                    # üst kenar
                    elif satir == 0 and (sutun != 0 or sutun != boyut - 1):
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        ekran[satir][sutun] = cevre_mayin
                    # sol kenar
                    elif (satir != 0 or satir != boyut - 1) and sutun == 0:
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        ekran[satir][sutun] = cevre_mayin
                    # sağ kenar
                    elif (satir != 0 or satir != boyut - 1) and sutun == boyut - 1:
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        ekran[satir][sutun] = cevre_mayin
                    # alt kenar
                    elif satir == boyut - 1 and (sutun != 0 or sutun != boyut - 1):
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        ekran[satir][sutun] = cevre_mayin
                    # köşe veya kenar değilse
                    elif (satir != 0 or satir != boyut - 1) and (sutun != 0 or sutun != boyut - 1):
                        if ekran[satir - 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir - 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir][sutun + 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun - 1] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun] == "X":
                            cevre_mayin += 1
                        if ekran[satir + 1][sutun + 1] == "X":
                            cevre_mayin += 1
                        ekran[satir][sutun] = cevre_mayin


                else:
                    print("Mayına bastınız oyun bitti")
                    print("Puanınız:{}".format(puan))
                    OyunAlaniniGoster(ekran)

                    secim = 0
                    while True:
                        print("Tekrar oynamak için (1), Çıkmak için (2)")
                        secim = int(input("Seçim:"))
                        if secim not in [1, 2]:
                            print("yanlış seçim yaptınız tekrar seçin: ")
                            continue
                        else:
                            break
                    if secim == 1:
                        print("\n\n")
                        break
                    elif secim == 2:
                        return

                if puan == (boyut * boyut) - alan:
                    print("Tebrikler oyunu kazandınız puanınız:{}\n".format(puan))
                    while True:
                        print("Tekrar oynamak için (1), Çıkmak için (2)")
                        secim = int(input("Seçim:"))
                        if secim not in [1, 2]:
                            print("Yanlış seçim yaptınız tekrar seçin!! \n ")
                            continue
                        else:
                            break
                    if secim == 1:
                        print("\n\n")
                        break
                    elif secim == 2:
                        return

def OyunAlaniniGoster(ekran):
    for satir in ekran:
        for sutun in satir:
            print(sutun, end="   ")
        print("\n")

OyunOyna()

