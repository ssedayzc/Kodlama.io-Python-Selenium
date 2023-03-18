"""
string değişkenler : yorumlar,ödev-ders vs konu başlıkları,hesap bilgileri...
integer değişkenler : yorum sayısı,progress bar,kart bilgileri...

"""

# Mail alma onayı

toApprove = input("Kodlama.io tarafından mail almak ister misiniz Y/N ?")

if(toApprove == 'y' or toApprove == 'Y'):
    print('Mail yoluyla bilgilendirilecekseniz.')

else:
    print('Tarafınıza mail iletilmeyecektir.')



# Progress Bar
progressBar = 0


dersProgrami = input("Ders programını tamamladınız mı True/False ?")
degerlendirme = input("Değerlendirmeyi tamamladınız mı True/False ?")
odev1 = input("Ödev 1'i tamamladınız mı True/False ?")
odev2 = input("Ödev 2'yi tamamladınız mı True/False ?")

if(dersProgrami== "True" or dersProgrami== "true" ):
    progressBar += 25

if (degerlendirme == "True" or degerlendirme == "true"):
    progressBar += 25

if (odev1 == "True" or odev1 == "true"):
    progressBar += 25

if (odev2 == "True"or odev2 == "true"):
    progressBar += 25

print(f"{progressBar}% tamamlandı")



