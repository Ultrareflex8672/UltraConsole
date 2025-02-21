import os
from application.dosya_isleyici import FileLoader as FL

class ConfigHandler(FL):

    @staticmethod
    def read_config(special_config=None, file_path="config/config.cfg"):
        config = {
            "menu_file": "config/menu.cfg",
            "menu_root": 0,
            "settings_menu_root": 1,
            "module_path": "modules",
            "menu_min_screen_width": 0,  # Menü ekranının minimum genişliği (0 girilirse otomatik hesaplanır)
            "menu_max_screen_width": 75,
            "menu_title_color": "31",
            "menu_content_color": "33",
            "menu_frame_color": "32",
            "info_title_color": "32",
            "info_content_color": "31",
            "info_frame_color": "33",
            "info_min_screen_width": 50,  # Info ekranının minimum genişliği (En düşük 50. 50 nin altındaki değerlerde 50 olarak alınır)
            "info_max_screen_width": 100,
        }

        # **config klasörünü oluştur (Yeni Eklendi)**
        if not os.path.exists("config"):
            os.makedirs("config")
        
        # **Dosya yoksa varsayılan dosyayı oluştur (Yeni Eklendi)**
        if not os.path.exists(file_path):
            print(f"Dosya bulunamadı: {file_path}")
            print("Varsayılan ayarlarla yeni dosya oluşturuluyor...")
            ConfigHandler.create_default_config(config, file_path)
        
        # **Dosya varsa içeriğini yükle**
        file = FL.load_lines(file_path)
        for line in file:
            # Satırı işleyerek boşluklardan ve yorumlardan temizle
            line = line.strip()
            if line and not line.startswith("#"):  # Yorum satırlarını yok say
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()

                # Eğer değeri bulunabiliyorsa, config'deki ilgili anahtara yaz
                if key in config:
                    config[key] = value
                else:
                    print(f"Uygulama: Özelleştirilmiş ayarlarda bilinmeyen anahtar '{key}' bulundu.")

        if special_config:
            if special_config in config.keys():
                return config[special_config]
            else:
                print(f"Uygulama: Özelleştirilmiş ayarlarda bilinmeyen anahtar: '{special_config}'")
                return None
        return config

    @staticmethod
    def create_default_config(config, file_path="config/config.cfg"):
        # **config klasörünü oluştur (Yeni Eklendi)**
        if not os.path.exists("config"):
            os.makedirs("config")

        # **Dosya oluşturma işlemi değiştirildi (FL.write_file yerine açık dosya yöntemi kullanıldı)**
        with open(file_path, "w", encoding="utf-8") as file:
            for key, value in config.items():
                file.write(f"{key} = {value}\n")
        print(f"{file_path} dosyası varsayılan ayarlarla oluşturuldu.")

    @staticmethod
    def save_config(config, file_path="config/config.cfg"):
        with open(file_path, "w", encoding="utf-8") as file:
            for key, value in config.items():
                file.write(f"{key} = {value}\n")

