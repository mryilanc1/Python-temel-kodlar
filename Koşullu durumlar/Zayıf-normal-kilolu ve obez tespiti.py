
# coding: utf-8

# In[29]:


a=float(input("Boyunuzu Girin:"))
b=int(input("Kilonuzu Girin:"))

k=b/ (a**2)

if(k<18.5):
    print(" Durunuz *Zayıf")

elif (k >= 18.5 and  k <= 25):
   print("Durunuz *Normal")

elif (k>= 25 and  k <= 30):
   print( "Durunuz *Fazla Kilolu")

else:
         print("Obez")

