def NotHesapla(satir):

    satir = satir[:-1] # satirlari yazdirmak istedigimizde python tarafindan eklenen sondaki '/n' karakterini siliyoruz.
    #print(satir)
    lst_ogrenci_bilgileri = satir.split(",")
    #print(lst_ogrenci_bilgileri)

    #------ listeden ogrenci bilgilerini teker teker aliyoruz------------
    isim = lst_ogrenci_bilgileri[0]
    puan1 = int(lst_ogrenci_bilgileri[1])
    puan2 = int(lst_ogrenci_bilgileri[2])
    puan3 = int(lst_ogrenci_bilgileri[3])
    # ------/ listeden ogrenci bilgilerini teker teker aliyoruz------------

    # ------ ortalama puani hesapliyoruz------------
    ort_puan = puan1*(3/10) + puan2*(3/10) + puan3*(4/10)
    # ------ /ortalama puani hesapliyoruz------------

    # ------ harf notunu hesapliyoruz------------
    harf_notu = "--"
    if(ort_puan>=90): harf_notu = "AA"
    elif(ort_puan>=85): harf_notu = "BA"
    elif(ort_puan>=80): harf_notu = "BB"
    elif(ort_puan>=75): harf_notu = "CB"
    elif(ort_puan>=70): harf_notu = "CC"
    elif(ort_puan>=65): harf_notu = "DC"
    elif(ort_puan>=60): harf_notu = "DD"
    elif(ort_puan>=55): harf_notu = "FD"
    else: harf_notu = "FF"
    # ------ /harf notunu hesapliyoruz------------

    return isim + "------------>" + harf_notu + "\n"


# ----- dosyayi 'okuma' modunda acip ogrenci harf not bilgilerini hesapliyoruz-------
with open("OgrenciNotlari.txt","r", encoding="utf-8") as file:

    ogr_harf_not_liste = []

    for i in file:
        ogr_harf_not_liste.append(NotHesapla(i))

    #print(ogr_harf_not_liste)
# ----- /dosyayi 'okuma' modunda acip ogrenci harf not bilgilerini hesapliyoruz-------


# ----- yeni olusturdugumuz listeyi yeni bir dosyaya yaziyoruz-------

with open("OgrenciHarfNotlari.txt","w",encoding="utf-8") as file2:
    for i in ogr_harf_not_liste:
        file2.write(i)

# ----- /yeni olusturdugumuz listeyi yeni bir dosyaya yaziyoruz-------