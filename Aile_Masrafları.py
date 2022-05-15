import time as t
aylık_gider={"ocak":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "şubat":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "mart":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "nisan":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "mayıs":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "haziran":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "temmuz":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "ağustos":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "eylül":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "ekim":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "kasım":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     "aralık":[["elektrik",0],["su",0],["eğitim",0],["gıda",0]],
     }
isim=input("isminizi  giriniz...")
soyad=input("soyisminizi giriniz...")
print(f"Hosgeldiniz sayın {isim.capitalize()} {soyad.capitalize()}")
t.sleep(1.25)
while True:
     print("Ocak ", "Şubat ", "Mart ", "Nisan", "Mayıs ", "Haziram ", "Temmuz ",
           "Ağustos ", "Eylül ", "Ekim ", "Kasım ", "Aralık ", sep="\n", )
     t.sleep(1)
     ay =input("Kaydetmek istediğiniz ayı yazınız...")
     ay=ay.lower()
     masraf_adı=int(input("elektrik için : 0\nsu için :1\neğitim için :2\ngıda için :3"))
     masraf_tutarı=int(input("Masraf tutarını giriniz..."))
     aylık_gider[ay][masraf_adı][1]+=masraf_tutarı
     cevap=int(input(("Sistemden çıkış yapmak istiyormusunuz: EVET (1) HAYIR (0)")))
     if cevap==1:
          break
     else:
          continue

while True:
     gecmis = input("Herhangi bir aya ait geçmişinizi görmek ister misiniz? ( evet or hayır )")
     gecmis=gecmis.lower()
     if gecmis== "hayır":
          print("*"*100)
          t.sleep(1)
          break
     print("Ocak ", "Şubat ", "Mart ", "Nisan", "Mayıs ", "Haziram ", "Temmuz ",
           "Ağustos ", "Eylül ", "Ekim ", "Kasım ", "Aralık ", sep="\n", )
     ay1 = input("hangi ayın geçmişini görmek istiyorsunuz? :")
     ay1=ay1.lower()
     for i,j in aylık_gider[ay1]:
          print(f"{ay1} ayındaki {i} faturan {j} tl'dir. ")
#sonradan veri silme ve ekleme işlemleri ekleyebilirim örn kırtasşye nasrafı eklemek istiyordur kullanıcı
#bu tarz işlemler...
while True:
     cevap_1=int(input("Masraf-ay tablonuzu görmek ister misiniz?\nevet:1 hayır: 0"))
     if cevap_1==0:
          break
     for a in aylık_gider.keys():
          print("** {} ayında :".format(a.capitalize()))
          for x, y in aylık_gider[a]:
               print(f"-- {x} masrafı {y} tl'dir")










