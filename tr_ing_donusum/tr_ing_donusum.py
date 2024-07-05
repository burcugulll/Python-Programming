donusum={"Ç":"C",
         "Ğ":"G",
         "İ":"I",
         "Ö":"O",
         "Ş":"S",
         "Ü":"U",
         "ç":"c",
         "ğ":"g",
         "ı":"i",
         "ö":"o",
         "ş":"s",
         "ü":"u"}
tr_kar="ÇĞİOŞÜçğıöşü"
mes=input("Metni giriniz: ")
eng_mes=""
for i in mes:
    if i in tr_kar:
        eng_mes+=donusum[i]
    else:
        eng_mes+=i
print(eng_mes)
