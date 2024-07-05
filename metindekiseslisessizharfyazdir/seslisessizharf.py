sesli_harfler="aeıioöuü"
sessiz_harfler="bcçdfgğhjklmnprsştvyzqwx"
sesliler=""
sessizler=""
metin=input("Bir metin giriniz: ")

for i in metin:
    if i in sesli_harfler:
        sesliler+=i
    elif i in sessiz_harfler:
        sessizler+=i
print("sesli harfler: ",sesliler)
print("\n")
print("sessiz harfler: ",sessizler)

#sesli_harfler="aeıioöuü"
#sessiz_harfler="bcçdfgğhjklmnprsştvyzqwx"
#sesliler=""
#sessizler=""
#metin=input("Bir metin giriniz: ")

#for i in metin:
   # if i in sesli_harfler:
       # if i not in sesliler:
        #   sesliler+=i
   # elif i in sessiz_harfler:
      #  if i not in sessizler:
     #      sessizler+=i
#print("sesli harfler: ",sesliler)
#print("\n")
#print("sessiz harfler: ",sessizler)