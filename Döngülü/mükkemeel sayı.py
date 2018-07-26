print("""
*********************************
 mukkemell sayi kontrol sistemi
*********************************

""")
toplam = 0
a = int(input("Sayinizi girin:"))
for muk in range(1,a):
    if (a % muk == 0):
        print(muk)
        toplam += muk
if (toplam == a ):
    print("Mukemmel sayi",a)
else:
    print("Mukemmel bir sayi degil",a)
