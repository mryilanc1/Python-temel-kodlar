# coding: utf-8

# In[4]:


a1 = float(input("Not1:"))
a2 = float(input("Not2:"))
a3 = float(input("Not3:"))

ort = (a1 + a2 + a3) / 3

print("Not1={} + Not2= {} + Not3={} Ortalama = {}".format(a1, a2, a3, ort))

if (ort >= 50):
    print("Başarılı")
else:
    print("Başarısız")


