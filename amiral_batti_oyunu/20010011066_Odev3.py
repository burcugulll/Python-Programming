#20010011066
#BURCU GÜL
import random
import os

def OyunAlaniOlustur(boyut=10, doldurulacakDeger='?'):
    oyunAlani = [[doldurulacakDeger for x in range(boyut)] for y in range(boyut)]
    return oyunAlani;

def GemiOlustur(bas, yon, uzunluk):
    # Yön = 0 -> gemi yatay, Yön = 1 -> gemi dikey
    if yon == 0:
        return [[bas[0] + x, bas[1]] for x in range(uzunluk)]
    else:
        return [[bas[0], bas[1] + x] for x in range(uzunluk)]

def FiloOlustur(oyunAlani):
    boyut = len(oyunAlani)
    gemi4 = GemiOlustur([random.randrange(boyut - 3), random.randrange(boyut - 3)], random.randint(0, 1), 4)
    while True:
        gemi3 = GemiOlustur([random.randrange(boyut - 2), random.randrange(boyut - 2)], random.randint(0, 1), 3)
        if not any(gemiKoordinati in gemi3 for gemiKoordinati in gemi4):
            break
    while True:
        gemi2 = GemiOlustur([random.randrange(boyut - 1), random.randrange(boyut - 1)], random.randint(0, 1), 2)
        if not any(gemiKoordinati in gemi2 for gemiKoordinati in gemi4) and not any(
                gemiKoordinati in gemi2 for gemiKoordinati in gemi3):
            break
    while True:
        gemi1 = GemiOlustur([random.randrange(boyut), random.randrange(boyut)], random.randint(0, 1), 1)
        if not any(gemiKoordinati in gemi1 for gemiKoordinati in gemi4) and not any(
                gemiKoordinati in gemi1 for gemiKoordinati in gemi3) and not any(
                gemiKoordinati in gemi1 for gemiKoordinati in gemi2):
            break
    return gemi1, gemi2, gemi3, gemi4

def GemileriYerlestir(oyunAlani, gemi1, gemi2, gemi3, gemi4):
    for gemi in [gemi1, gemi2, gemi3, gemi4]:
        for koordinat in gemi:
            oyunAlani[koordinat[1]][koordinat[0]] = 'G'

def OyunAlaniniYaz(oyunAlani, mod):
    boyut = len(oyunAlani)
    for satir in reversed(range(0, boyut)):
        for sutun in range(0, boyut):
            if mod == 0:
                if oyunAlani[satir][sutun] == 'G':
                    print('{:3}'.format('?'), end="")
                else:
                    print('{:3}'.format(oyunAlani[satir][sutun]), end="")
            else:
                print('{:3}'.format(oyunAlani[satir][sutun]), end="")
        print()

def AtisYap(oyunAlani, x, y):
    if oyunAlani[y][x] == '*' or oyunAlani[y][x] == 'X':
        print("\nBurayı daha önce vurdunuz!")
    elif oyunAlani[y][x] == 'G':
        print("\nTebrikler bir gemi vurdunuz!")
        oyunAlani[y][x] = 'X'
    else:
        print("\nMaalesef isabet edemediniz!")
        oyunAlani[y][x] = '*'

def oyun():
    os.system('cls')  # Konsolu temizle
    print("**************** AMİRAL BATTI OYUNUNA HOŞGELDİNİZ ****************\n")
    print("Oyun alanının boyutunu en az 10 olacak şekilde tamsayı değer giriniz.")
    while True:
        boyut = int(input("Boyut: "))
        if boyut < 10:
            print("\nOyun alanının boyutları 10x10 veya daha büyük olacak şekilde değer girin!")
        else:
             break
    print("\nGemilerin gösterileceği Açık Mod için 1, Gizli Mod için 0 giriniz.")
    while True:
        mod = int(input("Mod: "))
        if not (mod == 0 or mod == 1):
            print("\nSadece 0 ve 1 değerleri ile seçim yapın!")
        else:
            break
    oyunAlani = OyunAlaniOlustur(boyut, '?')
    gemi1, gemi2, gemi3, gemi4 = FiloOlustur(oyunAlani)
    filo = [gemi1, gemi2, gemi3, gemi4];
    GemileriYerlestir(oyunAlani, gemi1, gemi2, gemi3, gemi4)
    atis_sayisi = round(boyut * boyut / 3)
    os.system('cls')  # Konsolu temizle
    OyunAlaniniYaz(oyunAlani, mod)
    print("\nOyun alanının sol alt köşesi (1,1) noktasıdır.")
    while True:
        print("\nAtışın yapılacağı (x,y) koordinatlarını giriniz.")
        while True:
            x = int(input("x: "))
            y = int(input("y: "))
            if x > boyut or y > boyut or x < 1 or y < 1:
                print("\nOyun alanı içerisinde olacak şekilde değerler giriniz!")
            else:
                break
        os.system('cls')  # Konsolu temizle
        AtisYap(oyunAlani, x - 1, y - 1)
        for gemi in filo:
            try:
                gemi.remove([x - 1, y - 1])
            except:
                pass
            if len(gemi) == 0:
                filo.remove(gemi)
                print("Tebrikler bir gemiyi batırdınız!")
        atis_sayisi -= 1
        print(f"\nKalan atis sayisi: {atis_sayisi}")
        print("\n")
        OyunAlaniniYaz(oyunAlani, mod)

        if not any('G' in koordinat for koordinat in oyunAlani):
            print("\nBütün gemiler vuruldu!")
            print(f"\nTebrikler {atis_sayisi} puan ile oyunu kazandınız!")
            return
        if atis_sayisi <= 0:
            print("\nAtis sayiniz bitti. Kaybettiniz!")
            return
if __name__ == "__main__":
    while True:
        oyun()
        tekrar = input("Tekrar oynamak ister misiniz? ( Evet için E/e, Hayır H/h ): ")
        if not (tekrar == 'e' or tekrar == 'E'):
            print("\nÇıkış yapılıyor..!")
            break