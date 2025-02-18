import os
from application.dosya_isleyici import FileLoader as FL

class ConfigHandler(FL):
    
    @staticmethod
    def read_config(file_path="config/config.cfg"):
        config = {
            "menu_file": "config/menu.cfg",
            "menu_root": 0,
            "module_path": "modules",
            "min_screen_width": 75,
            "menu_title_color": "31",
            "menu_content_color": "33",
            "menu_frame_color": "32",
            "info_title_color": "31",
            "info_content_color": "33",
            "info_frame_color": "32",
        }
        
        if os.path.exists(file_path):
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
        else:
            print(f"Dosya bulunamadı: {file_path}")
            print("Varsayılan ayarlarla yeni dosya oluşturuluyor...")
            ConfigHandler.create_default_config(config, file_path)
        
        return config
    

    # @staticmethod
    # def create_default_config(config, file_path="config/config.cfg"):
    #     for key, value in config.items():
    #         return FL.write_file(file_path, f"{key} = {value}\n")
    #     print(f"{file_path} dosyası varsayılan ayarlarla oluşturuldu.")

    # Erdinç Hoca'ya sorulacak:
    # dosya_okuyucu içindeki write_file fonksiyonu nedense çalışmıyor.
    # Bu yüzden aşağıdaki gibi değiştirildi.

    @staticmethod
    def create_default_config(config, file_path="config/config.cfg"):
        with open(file_path, "w", encoding="utf-8") as file:
            for key, value in config.items():
                file.write(f"{key} = {value}\n")
        print(f"{file_path} dosyası varsayılan ayarlarla oluşturuldu.")


    @staticmethod
    def save_config(file_path, config):
        with open(file_path, "w", encoding="utf-8") as file:
            for key, value in config.items():
                file.write(f"{key} = {value}\n")


# # Verileri değişkenlere ata
# menu_path = config.get("menu_path", "menu.cfg")  # Varsayılan değer "menu.cfg"
# menu_root = int(config.get("menu_root", 0))      # Varsayılan değer 0

# # Bu aşamada menu_path ve menu_root değişkenleri kullanıma hazır
# print(f"menu_path: {menu_path}")
# print(f"menu_root: {menu_root}")

# # Konfigürasyon ayarlarını değiştirmek ve kaydetmek istersek
# config["menu_root"] = 1  # Örneğin menu_root değerini 1 yapalım
# ConfigHandler.save_config(config_file, config)
