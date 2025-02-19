import os
from application.ayar_okuyucu import ConfigHandler as CH
from application.menu_olusturucu import MenuSystem as MS

def oku_ve_goster():
    config_dict = CH.read_config()
    return config_dict

def ayarlari_goster(ayarlar):
    print("\nMevcut Ayarlar:")
    MS.create_frame("Ayarlar", ayarlar, "menu")
    # for i, (key, value) in enumerate(ayarlar.items(), 1):
    #     print(f"{i}. {key} = {value}")

def ayar_degistir(ayarlar):
    while True:
        ayarlari_goster(ayarlar)
        secim = input("\nDeğiştirmek istediğiniz ayarın numarasını girin (Çıkış için 'q'): ")
        
        if secim.lower() == "q":
            break
        
        if secim.isdigit() and 1 <= int(secim) <= len(ayarlar):
            secim_index = int(secim) - 1
            secilen_anahtar = list(ayarlar.keys())[secim_index]
            yeni_deger = input(f"{secilen_anahtar} için yeni değeri girin: ")
            ayarlar[secilen_anahtar] = yeni_deger
            ayarlari_kaydet(ayarlar)
        else:
            print("Geçersiz seçim, tekrar deneyin.")

def ayarlari_kaydet(ayarlar):
    CH.save_config(ayarlar)
    # with open(CONFIG_FILE, "w") as f:
    #     for key, value in ayarlar.items():
    #         f.write(f"{key} = {value}\n")
    print("Ayarlar başarıyla kaydedildi!")

def main():
    ayarlar = oku_ve_goster()
    ayar_degistir(ayarlar)
    ayarlari_kaydet(ayarlar)

