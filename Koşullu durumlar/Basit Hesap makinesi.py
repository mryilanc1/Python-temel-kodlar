# coding: utf-8

# In[12]:


print(""" ********************************************

   Python'la Tek işlemlik  Hesap Makinesi

                  İşlemler;
        1-Toplama
        2-Çıkarma
        3-Çarpma
        4-Bölme


********************************************""")



işlem = input("İşlemi Giriniz:")

a = float(input("Birinci Sayıyı giriniz:"))
b = float(input("İkinci Sayıyı Giriniz:"))

if (işlem == "1"):
    print("{} + {} toplamı = {} ".format(a, b, a + b))

elif (işlem == "2"):
    print(" {} - {} = {}".format(a, b, a - b))

elif (işlem == "3"):
    print(" {} * {} = {}".format(a, b, a * b))

elif (işlem == "4"):
    print(" {} / {} = {}".format(a, b, a / b))

else:
    print("işlem geçersiz!!!!")




