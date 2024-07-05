while True:
    sifre = input("Şifrenizi giriniz: ")
    kontrol = 1

    if len(sifre) < 8 or len(sifre) > 12:
        kontrol = 0
        print("Şifreniz en az 8 en fazla 12 karakter içermelidir")

    for i in range(10):
        if sifre.startswith(str(i)):
            kontrol = 0
            print("Şifreniz rakam ile başlayamaz")
        if sifre.endswith(str(i)):
            kontrol = 0
            print("Şifreniz rakam ile bitemez")

    kucuk_harfler = "abcçdefgğhıijklmnoöprsştuüvyzwq"
    buyuk_harfler = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZWQ"
    rakamlar = "0123456789"
    syc_k = 0
    syc_b = 0
    syc_r = 0
    syc_alfa = 0

    for karakter in sifre:
        if karakter in kucuk_harfler:
            syc_k += 1
        elif karakter in buyuk_harfler:
            syc_b += 1
        elif karakter in rakamlar:
            syc_r += 1
        else:
            syc_alfa += 1

    if syc_k == 0:
        kontrol = 0
        print("Şifre en az bir küçük harf içermelidir")
    if syc_b == 0:
        kontrol = 0
        print("Şifre en az bir büyük harf içermelidir")
    if syc_r == 0:
        kontrol = 0
        print("Şifre en az bir rakam içermelidir")
    if syc_alfa == 0:
        kontrol = 0
        print("Şifre en az bir alfanümerik olmayan karakter içermelidir")

    if sifre.find(" ") != -1:
        kontrol = 0
        print("Şifre boşluk karakteri içermemelidir")

    kontrol_t = 0
    for karakter in sifre:
        if sifre.count(karakter) > 1:
            kontrol_t = 1

    if kontrol_t == 1:
        kontrol = 0
        print("Şifrenizde tekrarlayan karakter olmamalıdır")

    if sifre.find("@") != -1:
        kontrol = 0
        print("Şifre @ karakteri içermemelidir")

    if kontrol == 0:
        print("Şifre uygun değil")
        devam = input("Şifrenizi tekrar girmek ister misiniz? (Evet için 'E', Hayır için 'H' giriniz): ").lower()
        if devam != 'e':
            break
    else:
        print("Şifre uygundur. Şifreniz: {} ".format(sifre))
        break
