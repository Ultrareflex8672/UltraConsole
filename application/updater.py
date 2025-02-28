from html.parser import HTMLParser
import urllib.request
import zipfile
import shutil
import os
import time

class Updater(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_target = False  # Belirtilen id'yi bulmak için bayrak
        self.data_list = []  # Bulunan verileri saklamak için liste
        self.current_version = 2052 # Bu programın sürümü


    def handle_starttag(self, tag, attrs):
        """Başlangıç etiketini işleyerek id kontrolü yap"""
        if tag == "b":  # Sadece <b> etiketlerine odaklan
            for attr, value in attrs:
                if attr == "id" and value == "user-content-version":
                    self.is_target = True

    def handle_endtag(self, tag):
        """Kapanış etiketini işleyerek id kontrolünü sıfırla"""
        if tag == "b" and self.is_target:
            self.is_target = False

    def handle_data(self, data):
        """Etiket içindeki metni al"""
        if self.is_target:
            self.data_list.append(data.strip())

    def version(self):
        # Web sayfasından HTML içeriğini al
        url = "https://github.com/Ultrareflex8672/UltraConsole"
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode("utf-8")

        # Parser'ı çalıştır ve veriyi işle
        parser = Updater()
        parser.feed(html_content)

        new_version = int(parser.data_list[0].replace(".", ""))

        # Bulunan veriyi yazdır
        return new_version, self.current_version
    
    def update(self):
        # 1. ZIP dosyasının URL'sini belirle
        zip_url = "https://github.com/Ultrareflex8672/UltraConsole/archive/refs/heads/main.zip"  # <-- Buraya gerçek ZIP dosyası linkini koy

        # 2. ZIP dosyasını indir
        zip_path = "UltraConsole.zip"

        print("Güncelleme dosyası indiriliyor...")
        urllib.request.urlretrieve(zip_url, zip_path)

        time.sleep(3)  # 3 saniye bekler
        print("İndirme tamamlandı! Güncelleme işlemi devam ediyor...")
        

        # 3. ZIP dosyasını aç ve içeriğini çıkar
        extract_folder = "extracted"
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_folder)

        time.sleep(2)  # 2 saniye bekler
        print("Güncelleme dosyası çıkarıldı!")

        # 4. UltraConsole-main klasörünü bir üst dizine taşı
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Çalıştığımız dizin
        parent_dir = os.path.dirname(current_dir)  # Üst dizin yolu
        input("123")
        ultra_console_folder = os.path.join(extract_folder, "UltraConsole-main")
        # target_path = os.path.join(parent_dir, "UltraConsole-main")
        target_path = parent_dir

        time.sleep(2)  # 2 saniye bekler

        if os.path.exists(ultra_console_folder):
            # # Eğer hedefte aynı isimde klasör varsa önce sil
            # if os.path.exists(target_path):
            #     shutil.rmtree(target_path)

            # shutil.move(ultra_console_folder, target_path)

            # Eğer hedef klasör yoksa oluştur
            if not os.path.exists(target_path):
                os.makedirs(target_path)

            # Kaynak klasör içindeki tüm dosya ve klasörleri al
            for item in os.listdir(ultra_console_folder):
                src_path = os.path.join(ultra_console_folder, item)
                dest_path = os.path.join(target_path, item)

                # Dosya veya klasör olup olmadığına göre taşı
                shutil.move(src_path, dest_path)
            
            print("Güncelleme dosyaları temizleniyor...")
            
            # 5. Geçici çıkarma klasörünü ve ZIP dosyasını temizle
            os.remove(zip_path)  # ZIP dosyasını sil
            shutil.rmtree(extract_folder)  # Geçici klasörü sil
            
            time.sleep(1)  # 1 saniye bekler
            print("Geçici dosyalar temizlendi!")

            old_version, new_version = Updater.version(self)
            time.sleep(1)  # 1 saniye bekler
            print("UltraConsole V"+old_version+" 'dan V"+new_version+" 'a başarı ile güncellendi!")
            time.sleep(2)  # 2 saniye bekler
        else:
            print("Uygulama dizininde bir sorun oluştu! Elle güncelleme yapınız. (https://github.com/Ultrareflex8672/UltraConsole/archive/refs/heads/main.zip)")

        





