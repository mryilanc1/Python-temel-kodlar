print("""
*****************************
Amstrong Sayisi sistemi

*****************************
""")
toplam = 0
a = str(input("Sayinzi girin"))

liste = [c for c in a]
for b in liste:
    b = int(b)
    b = b ** len(liste)
    toplam+=b
a = int(a)
if a == toplam:
    print("girmis oldugunuz sayi ",a,"Amstrong Sayidir")
else:
    print("Girmis oldugunuz sayi amstrong sayisi degildir...")



