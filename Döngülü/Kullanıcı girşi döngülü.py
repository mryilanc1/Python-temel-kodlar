# coding=utf-8
print(
"""
*******************************

Kullanıcı Giriş Sistemi

*******************************

""")

sys_kullanıcı = {"Ramo":"121214","kaka":"12121412"}

sys_şifre = "121214"

sys_unut = "Ali"

hak = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adınız :")
    kullanıcı_şifre = input("Şifreniz :")


    hak -=1
    if (kullanıcı_adı == sys_kullanıcı and kullanıcı_şifre != sys_şifre):
        print("Şifreniz Yanlış\n","\nKalan Kullanıcı Giriş Hakkınız:",hak)
        q = input("Şifreyi unuttuysanız 'q' basın... yoksa 'q' dışında bir tuşa basın... ")
        if (q == "q"):
            b = input("Gizli Cevabınız Ne?")
            if (b == sys_unut):
                print("Şifeniz:",sys_şifre)


    elif (kullanıcı_adı != sys_kullanıcı and kullanıcı_şifre == sys_şifre):
        print("Kullanıcı Adınız Yanlış\n","\nKalan Kullanıcı Giriş Hakkınız:",hak)
    elif (kullanıcı_adı != sys_kullanıcı and kullanıcı_şifre != sys_şifre):
        print("Kullanıcı adınız ve Şifreniz Yanlış\n","\nKalan Kullanıcı Giriş Hakkınız:",hak)
    else:
        print("\nSisteme giriş gerçekleşti...")
        break
    if (hak == 0):
        print("Giriş Hakkınız kalmadı")
        break
