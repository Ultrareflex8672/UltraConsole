from application.menu_olusturucu import MenuSystem as MS
import os

class SettingsMenu():
  
    def menu_goster(self, **kwargs):
        config = MS.read_config()                                   # Ayarları oku
        menu_data = MS.load_json(config["menu_file"])               # Menü verilerini yükle
        root = list(menu_data.keys())[int(config.get("settings_menu_root"))]
        settings_menu = MS(menu_data[root], 1, "application", "settings", "SettingsMenu", None, "settings", **kwargs)                                    # Menü sistemini başlat (init fonksiyonu çalışır ancak henüz menü gösterilmez)
        settings_menu.show_menu(root)
        
    def settings(self, **kwargs):
        if kwargs.get("selected_key") == 1:
            SettingsMenu.ayarlari_goster(MS.read_config())
        elif kwargs.get("selected_key") == 2:
            SettingsMenu.ayar_degistir(MS.read_config())

    def ayarlari_goster(ayarlar):
        ayar_dokumu = "            ".join(f"{key}: {value}" for key, value in ayarlar.items())
        MS.create_frame("Mevcut Ayarlar", ayar_dokumu)
    
    def ayar_degistir(ayarlar):
        while True:
            ayarlar_listesi = [f"{key}: {value}" for key, value in ayarlar.items()]
            os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
            secim = MS.create_frame("Ayar Değiştirme Menüsü", ayarlar_listesi + ["Geri Dön"], "menu")
            
            if secim.lower() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
                break
            
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
        MS.save_config(ayarlar)
        MS.create_frame("Ayarlar Kaydedildi", "Ayarlar başarıyla kaydedildi.")

