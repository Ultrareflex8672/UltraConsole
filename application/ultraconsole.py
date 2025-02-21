from application.menu_olusturucu import MenuSystem as MS

class UltraConsole(MS):

    def go_main_menu():
        all_config = MS.read_config()                               # Tüm ayarları oku (Şuanda burada bir işlevi yok ancak ileride kullanılabilir)
        modules_path = all_config.get("module_path")                     # Modül yolu al (Şuanda burada bir işlevi yok ancak ileride kullanılabilir)
        menu_root_config = MS.read_config("menu_root")              # Menü kökünü al
        MS.check_and_create_config(MS.read_config("menu_file"))     # Menü dosyasını kontrol et ve oluştur
        menu_data = MS.load_json(MS.read_config("menu_file"))       # Menü verilerini yükle
        root = list(menu_data.keys())[int(menu_root_config)]             # İlk menüyü al (menu.cfg Dosyasındaki JSon da 1. Seviyede Birden Fazla Menü varsa İlk Menüyü Alır)                          # Menü başlığını al
        ms = MS(menu_data[root])                                    # Menü sistemini başlat (init fonksiyonu çalışır ancak henüz menü gösterilmez)
        ms.show_menu(root)                                          # Menüyü göster