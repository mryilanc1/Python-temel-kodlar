
# coding: utf-8

# In[5]:


ilk=input("birinci sayı:")
ikinci=input("ikinci sayı:")

print("\ndeğişim öncesi:\n ilk sayı: {}\tİkinci Sayı: {}".format(ilk,ikinci))


(ilk,ikinci)=(ikinci,ilk)
print("Değişim sonrası ilk sayı : {}\n İkinci sayı : {} ".format(ilk,ikinci))

