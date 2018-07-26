print("""
******************************

Sonsuz Toplam

******************************

""")

toplam = 0
while True:
    girdi = input("girdiyi ekleyin...")

    if (girdi == "q"):
        print("Toplam Girdi", toplam)
        break

    girdi = int(girdi)
    toplam += girdi
