import random as r
sayı_b=r.randint(1,5)
tahmin=0
while True:
    toplam=0
    tahmin+=1
    for i in range(3):
        sayı_k =int(input("bir sayı giriniz..."))
        toplam+=sayı_k
    if toplam!=sayı_b:
        print("Tüh bu sefer tutmadı")
    else:
        break
print(f"{tahmin}: kullandığınız tahmin sayısı, {sayı_b}:bilgisayarın tuttuğu sayı!!!")