# coding=utf-8
print("""
********************************************

Faktöriyel Bulma

*Çıkış İçin 'q' Basın...

********************************************""")

while True:
    sayi = input("İstenilen Faktöriyel:")

    if (sayi =="q"):
        print("İşlem Sonlandırılıyor...")
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1


        for f in range (2,sayi+1):
            faktoriyel *= f
        print("faktoriyel",faktoriyel)