from application.ultraconsole import UltraConsole as UC

def carpimtablosu(**kwargs):
    carpim_tablosu = []

    for i in range(1, 11):
        satir = []
        for j in range(1, 11):
            satir.append(str(i)+"x"+str(j)+"="+str(i * j))
        carpim_tablosu.append(satir)
    carpim_tablosu.append("Geri Dön")

    # # Çarpım tablosunu ekrana yazdır
    # for satir in carpim_tablosu:
    #     print(satir)
    UC.create_frame("Çarpım Tablosu", carpim_tablosu, "menu")