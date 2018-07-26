# coding: utf-8

# In[2]:


print("""*********************
 Sistemimize Hoşgeldiniz.
    Ortadoğu Yazılım 
      Üye Girişi

**********************""")
sys_kullanıcı = "mr.yılancı"
sys_şifre = "123456"

kullanıcı = input("kullanıcı Adı:")
şifre = input("Şife:")

if (sys_kullanıcı == kullanıcı and sys_şifre != şifre):
    print("Şifreniniz Yanlış")

elif (sys_kullanıcı != kullanıcı and sys_şifre != şifre):
    print("Kullanıcı Adı ve şifre yanlış")

elif (sys_kullanıcı != kullanıcı and sys_şifre == şifre):
    print("Sistemimizde Böyle Bir Kullanıcı Mevcut değil...")

else:
    print("Giriş Başarıyla Gerçekleşti...")





