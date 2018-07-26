# coding=utf-8
print("""
******************************************************
 Atm Makinesine Hoşgeldiniz

İşlemler;

1-Bakiye Sorgulama

2-Para Yatırma

3-Para Çekme


Çıkmak için 'q' basın...


******************************************************

""")


bakiye = 1000

while True:
    islem= input("İşleminizi girin:")

    if (islem == '1'):
        print("Bakiyeniz {}".format(bakiye))
    elif (islem == '2'):
        miktar = int(input("Yatıracağınız Tutar:"))

        bakiye += miktar
    elif (islem == '3'):
        miktar = int(input("Çekeceğiniz Tutar:"))
        if (bakiye < miktar):
            print ("Yetersiz Bakiye")
            continue
        bakiye -=miktar

    elif (islem == 'q'):
        print("Yine Bekleriz")
        break

    else:
        print("Geçersiz İşlem")
        break