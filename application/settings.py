from application.ayar_okuyucu import ConfigHandler as CH
from application.ekran_olustur import ScreenView as MS
import os

class SettingsMenu():
    def ayar_oku():
        config_dict = CH.read_config()
        return config_dict
    
    def settings_menu_item(level):
        main_settings_menu_items = ["Kullanıcı Ayarları", "Program Ayarları", "Çıkış"]
        general_settings_menu_items = ["Ayarları Görüntüle", "Ayarları Değiştir", "Geri Dön"]
        user_settings_menu_items = ["Kullanıcı Adı Değiştir", "Şifre Değiştir", "Geri Dön"]

        if level == 0:
            return main_settings_menu_items
        elif level == 2:
            return general_settings_menu_items
        elif level == 1:
            return user_settings_menu_items
        
    def menu_goster(level):
        os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
        menu_items = SettingsMenu.settings_menu_item(level)

        if level == 0:
            title = "Ayarlar"
        elif level == 1:
            title = "Kullanıcı Ayarları"
        elif level == 2:
            title = "Program Ayarları"

        secim = MS.create_frame(title, menu_items, "menu")

        if level == 0:
            if int(secim) == 1:
                pass
            elif level == 0 and int(secim) == 2:
                SettingsMenu.menu_goster(int(secim))
            elif level == 0 and int(secim) == 0:
                os.system("python main.py")
                
        if level == 1:
            if int(secim) == 1:
                pass
            elif int(secim) == 2:
                pass
            elif int(secim) == 0:
                SettingsMenu.menu_goster(level-1)
        if level == 2:
            if int(secim) == 1:
                SettingsMenu.ayarlari_goster()
            elif int(secim) == 2:
                SettingsMenu.ayar_degistir(SettingsMenu.ayar_oku())
            elif int(secim) == 0:
                SettingsMenu.menu_goster(level-1)
        return secim

    def ayarlari_goster():
        os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
        ayarlar = SettingsMenu.ayar_oku()
        ayar_dokumu = "            ".join(f"{key}: {value}" for key, value in ayarlar.items())
        MS.create_frame("Mevcut Ayarlar", ayar_dokumu)
        os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
        SettingsMenu.menu_goster(2)
    
    def ayar_degistir(ayarlar):
        while True:
            ayarlar_listesi = [f"{key}: {value}" for key, value in ayarlar.items()]
            os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
            secim = MS.create_frame("Ayar Değiştirme Menüsü", ayarlar_listesi + ["Geri Dön"], "menu")
            
            if secim.lower() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
                SettingsMenu.menu_goster(2)
            
            if secim.isdigit() and 1 <= int(secim) <= len(ayarlar):
                secim_index = int(secim) - 1
                secilen_anahtar = list(ayarlar.keys())[secim_index]
                yeni_deger = MS.create_frame("Yeni Değer Girişi", f"Uyarı: {secilen_anahtar} için yeni değeri girişi yapılıyor ", "Yeni değer:\n")
                if yeni_deger:
                    eminmisiniz = MS.create_frame("Yeni Değer Girişi", f"Uyarı: {secilen_anahtar} değeri {yeni_deger} olarak değiştirilecektir. Bu değişikliği yapmak istediğinize emin misiniz?", "E/H\n")
                    if eminmisiniz.lower() == "e":
                        ayarlar[secilen_anahtar] = yeni_deger
                        SettingsMenu.ayarlari_kaydet(ayarlar)
            else:
                MS.create_frame("Hata", "Geçersiz seçim yapıldı. Lütfen tekrar deneyin.")

    
    def ayarlari_kaydet(ayarlar):
        CH.save_config(ayarlar)
        MS.create_frame("Ayarlar Kaydedildi", "Ayarlar başarıyla kaydedildi.")

