import os
import json

class DefaultMenu:
    # Varsayılan veri yapısı
    default_menu = {
    "Ana Menü": {
        "Hesap Makinesi": {
            "Toplama": "hesap_makinesi",
            "Çıkarma": "hesap_makinesi",
            "Çarpma": "hesap_makinesi",
            "Bölme": "hesap_makinesi",
            "Üs Alma": "hesap_makinesi",
            "Kare Alanı": "hesap_makinesi",
            "Karenin Çevresi": "hesap_makinesi"
        },
        "Oyunlar": {
            "Taş Kağıt Makas": "taskagitmakas",
            "Adam Asmaca": "adamasmaca",
            "Pong": "pong",
            "Sayı Tahmin": "sayitahmin"
        },
        "Bayrak Çiz": "bayrak",
        "Takvim": "takvim",
        "Ritmik Sayma": "ritmiksayma",
        "Not Hesaplama": "nothesaplama",
        "Çarpım Tablosu": "carpimtablosu",
        "BMI Hesaplama": "bmihesaplama",
        "Döviz Hesapla": "dovizhesaplama",
        "Sıcaklık Çevirme": "sicaklikcevirme",
        "Örnek Modül": "ornek_modul"
    },
    "Ayarlar": {
        "Program Ayarları": {
            "Ayarları Görüntüle": "settings",
            "Ayarları Değiştir": "settings"
        },
        "Kullanıcı Ayarları": {
            "Kendi Ayarlarım": {
                "Bilgilerimi Görüntüle": "",
                "Kullanıcı Adı Değiştir": "",
                "E-Posta Değiştir": "",
                "Telefon Değiştir": "",
                "Şifre Değiştir": ""
            },
            "Diğer Kullanıcılar": {
                "Kullanıcıları Görüntüle": "",
                "Kullanıcı Adı Değiştir": "",
                "E-Posta Değiştir": "",
                "Telefon Değiştir": "",
                "Şifre Değiştir": ""
            }
        }
    },
    "Örnek Modül": {
        "Seçenek 1": "ornek_modul",
        "Seçenek 2": "ornek_modul",
        "Seçenek 3": "ornek_modul",
        "Seçenek 4": "ornek_modul",
        "Seçenek 5": {
            "Seçenek 5.1": "ornek_modul_alt_fonkisyon",
            "Seçenek 5.2": "ornek_modul_alt_fonkisyon"
        }
    }
}


    # Dosyanın var olup olmadığını ve geçerli JSON olup olmadığını kontrol et
    def check_and_create_config(config_path=None):
        if config_path:
            if not os.path.exists("config"):
                os.makedirs("config")  # Klasör yoksa oluştur

            if not os.path.exists(config_path):
                DefaultMenu.save_config(config_path)  # Dosya yoksa oluştur
                return

            try:
                with open(config_path, "r", encoding="utf-8") as file:
                    content = file.read().strip()

                if not content:  # Dosya boşsa
                    DefaultMenu.save_config(config_path)
                    return

                config_data = json.loads(content)  # JSON formatında olup olmadığını kontrol et

                if not isinstance(config_data, dict) or "Ana Menü" not in config_data or "Ayarlar" not in config_data:
                    DefaultMenu.save_config(config_path)  # Yapı uygun değilse varsayılan veriyi kaydet

            except (json.JSONDecodeError, FileNotFoundError):  # JSON hatası varsa dosyayı oluştur
                DefaultMenu.save_config(config_path)
        else:
            print("Menü dosyası yolu belirtilmedi.")

    # Varsayılan veriyi dosyaya kaydet
    def save_config(config_path):
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(DefaultMenu.default_menu, file, ensure_ascii=False, indent=4)