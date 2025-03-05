import os
import json

class DefaultMenu:
    # Varsayılan veri yapısı
    default_menu = {
    "Ana Menü": {
        "Hesap Makinesi": "hesap_makinesi",
        "Oyunlar": "oyunlar",
        "Bayrak Çiz": "bayrak",
        "Takvim": "takvim",
        "Ritmik Sayma": "ritmiksayma",
        "Not Hesaplama": "nothesaplama",
        "Çarpım Tablosu": "carpimtablosu",
        "BMI Hesaplama": "bmihesaplama",
        "Döviz Hesapla": "dovizhesaplama",
        "Sıcaklık Çevirme": "sicaklikcevirme"
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
    },
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
        "Adam Asmaca": "adamasmaca",
        "Pong": "pong",
        "Sayı Tahmin Etme": "sayitahmin",
        "Taş Kağıt Makas": "taskagitmakas"
    }
}


    # Dosyanın var olup olmadığını ve geçerli JSON olup olmadığını kontrol et
    def check_and_create_config(config_path=None):
        # input(config_path)
        if config_path:
            if not os.path.exists("config"):
                # input("Dizin yok")
                os.makedirs("config")  # Klasör yoksa oluştur

            if not os.path.exists(config_path):
                # input("Dosya yok")
                DefaultMenu.save_config(config_path)  # Dosya yoksa oluştur
                return

            try:
                with open(config_path, "r", encoding="utf-8") as file:
                    content = file.read().strip()

                if not content:  # Dosya boşsa
                    # input("Dosya boş")
                    DefaultMenu.save_config(config_path)
                    return

                config_data = json.loads(content)  # JSON formatında olup olmadığını kontrol et

                if not isinstance(config_data, dict) or "Ana Menü" not in config_data:
                    # input("yapı bozuk")
                    DefaultMenu.save_config(config_path)  # Yapı uygun değilse varsayılan veriyi kaydet

            except (json.JSONDecodeError, FileNotFoundError):  # JSON hatası varsa dosyayı oluştur
                # input("json hatası")
                DefaultMenu.save_config(config_path)
        else:
            print("Menü dosyası yolu belirtilmedi.")

    # Varsayılan veriyi dosyaya kaydet
    def save_config(config_path):
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(DefaultMenu.default_menu, file, ensure_ascii=False, indent=4)