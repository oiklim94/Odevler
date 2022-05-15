print("Kullanıcıya istediği karakter kadar güçlü şifre oluşturma ve bunu bir listeye kaydeterek sınıflandırma")
ad="iklim"
sıfre_i="iklim123"
sıfre_app = []
kullanıcı_dogrulama=input("Adınızı giriniz...")
sıfre_dogrulama=input("sıfrenizi giriniz")
import random as r
if ad== kullanıcı_dogrulama and sıfre_i==sıfre_dogrulama:
    print("Uygulamayaa hoşgeldin iklim")
    print("uygulamadan çıkmak istediğinde 0'a bas... ")
    sıfre = ""
    harf_sessiz = "abBcCdDfFgGhHjJkKlLmMnNpPrRsStTvVyYzZxXwWqQ"
    harf_sesli = "aAeEıIiİoOuU"
    ozel_krt = "3!0^+%&/6()12=?89_-#${[]}456"
    karma = [harf_sessiz, harf_sesli, ozel_krt]
    while True:
        sayı = int(input("İstediğiniz karakter sayısını giriniz..."))
        if sayı == 0:
            break
        for i in range(sayı):
            secim = r.randint(0, 2)
            olsılk = r.randint(0, len(karma[secim]) - 1)
            sıfre = str(karma[secim][olsılk]) + sıfre
        app = input("neyin sıfresi olduğunu yazınız")
        sıfre_app.append([app, sıfre])
else:
    print("uygulamadan atıldınız...")
sıfreler={"iklim": sıfre_app}
cevap=int(input("Sıfrelerinizi görmek ister misiniz... \n (EVET) 1 \n (HAYIR) 0"))
if cevap==1:
    print(sıfreler["iklim"])
elif cevap==0:
    print("Uygulamadan çıkış yapıldı...")