ogrenciler=[]

#öğrenci ekleme
def ogrEkle(fullName):
    ogrenciler.append(fullName)

#öğrenci silme
def ogrSil(fullName):
    ogrenciler.remove(fullName)

#öğrencileri listeleme
def ogrListele():
    for i in ogrenciler:
        print(str(i))

#öğrenci no görüntüleme
def ogrNoSorgula():
    name= input("Numarası bilinmeyen öğrencinin adını giriniz")
    surname = input("Numarası bilinmeyen öğrencinin soyadını giriniz")
    fullName = name+'-'+surname
    print("Öğrenci numarası : ",ogrenciler.index(fullName))

#birden fazla kayıt alma
def kayitAl():
    while(True):  
        name = input("İsim : ")
        if (name=='q' or name=='Q'):
            break
        surname = input("soyisim : ")
        if (surname=='q' or surname=='Q'):
            break
        fullName = name +'-'+surname
        ogrEkle(fullName)

#birden fazla sil
def ogrencileriSil(silinecekKayit):
    onay = True
    while(onay):  
        ogrSil(silinecekKayit)
        onay = input("Kayıt silme işlemine devam edecek misiniz ? E/H")
        if(onay.capitalize == 'E'):
            onay = True
        else: onay = False
        
kayitAl()
ogrListele()
silinecekKayit = input("Silinecek kayıt için isim-soyisim\n")
ogrencileriSil(silinecekKayit)   
ogrNoSorgula()

