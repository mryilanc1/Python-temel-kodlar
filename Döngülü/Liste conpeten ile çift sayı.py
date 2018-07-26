print("""
*****************************

İki İle Bölümünden list.companet 
            ve 
        continue ile....

*****************************
""")
sayi = range(1,101)
pro = [a for a in sayi if not (a % 2 == 1) ]
print(pro)