from application.ultraconsole import UltraConsole as UC          # UltraConsole Developed by Ultrareflex (Kemal Burak YILDIRIM)

def ritmik_sayma(baslangic, artis, adim_sayisi):
    sayilar = [baslangic + (i * artis) for i in range(adim_sayisi)]
    return sayilar

baslangic = int(UC.create_frame("Ritmik Sayma Modülü","Başlangıç değerini girin: ", "\n"))
artis = int(UC.create_frame("Ritmik Sayma Modülü","Artış miktarını girin: ", "\n"))
adim_sayisi = int(UC.create_frame("Ritmik Sayma Modülü","Adım sayısını girin: ", "\n"))

def ritmiksayma(**kwargs):
    sayim = ritmik_sayma(baslangic, artis, adim_sayisi)
    str_sayim = " - ".join([str(i) for i in sayim]) 
    # String sorunu olunca bu satırı ekledim. Neden böyle yapmışım diye düşünmeyim diye aşağıdaki satırı silmedim.
    # str_sayim = " - ".join(sayim)
    return str_sayim