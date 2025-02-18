from application.menu_olusturucu import MenuSystem as MS        # MenuSystem Sınıfını application/menu_olusturucu.py Dosyasından Al

if __name__ == "__main__":                                      # Programın ana modül olup olmadığını kontrol et
    config = MS.read_config()                                   # Ayarları oku
    menu_data = MS.load_json(config["menu_path"])               # Menü verilerini yükle
    root = list(menu_data.keys())[int(config.get("menu_root"))] # İlk menüyü al (menu.cfg Dosyasındaki JSon da 1. Seviyede Birden Fazla Menü varsa İlk Menüyü Alır)                          # Menü başlığını al
    ms = MS(menu_data[root])                                    # Menü sistemini başlat (init fonksiyonu çalışır ancak henüz menü gösterilmez)
    ms.show_menu(root)                                          # Menüyü göster


