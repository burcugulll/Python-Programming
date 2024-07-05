parola=input("parola giriniz: ")
turkce_karakter="çğıöşü"
turkceler=""
for i in parola:
    if i in turkce_karakter:
        if i not in turkceler:
            turkceler+=i
print("turkce karakter: ",turkceler)
