print("Girilen sayıların ebob ve ekokonu hesaplayan program")

def islemler():
     ortak_carpan = []
     ebob = 1
     s1 = int(input("Birinci sayı giriniz..."))
     s2 = int(input("İkinci sayıyı giriniz"))
     if s1 < s2:
          kucuks = s1
          buyuks = s2
     else:
          kucuks = s2
          buyuks = s1
     for i in range(2, kucuks // 2):
          if buyuks % kucuks == 0:
               ebob = kucuks
          else:
               kalan1 = kucuks % i
               if kalan1 == 0:
                    kalan2 = buyuks % i
                    if kalan2 == 0:
                         ortak_carpan.append(i)
                    else:
                         continue
               else:
                    continue
     for a in ortak_carpan:24
          ebob *= a
     print(f"{s1} ve {s2} sayılarının ebobu {ebob}'dır")
     ekok = s1 * s2 // ebob
     print(f"{s1} ve {s2} sayılarının ekoku ise {ekok}'dır")
     print(f"{kucuks} kucuk sayı, {buyuks} buyuk sayıdır.")
islemler()