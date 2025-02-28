from html.parser import HTMLParser
import urllib.request
import zipfile
import shutil
import os
import time
import sys

class Updater(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_target = False  # Belirtilen id'yi bulmak için bayrak
        self.data_list = []  # Bulunan verileri saklamak için liste
        self.current_version = 2505 # Bu programın sürümü


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
        try:
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

            current_dir = os.path.dirname(os.path.abspath(__file__))  # Çalıştığımız dizin

            # Ana dizin (main_folder)
            main_folder = parent_dir = os.path.dirname(current_dir)  # Üst dizin yolu

            # Kaynak dizin (extract içindeki UltraConsole-main klasörü)
            source_folder = os.path.join(main_folder, extract_folder, "UltraConsole-main")

            # Kaynak dizinin içeriğini listele
            for item in os.listdir(source_folder):
                source_path = os.path.join(source_folder, item)
                target_path = os.path.join(main_folder, item)

                if os.path.isdir(source_path):  # Eğer kaynak bir klasörse
                    if not os.path.exists(target_path):  
                        shutil.copytree(source_path, target_path)  # Eğer hedefte yoksa direkt kopyala
                    else:
                        # Hedefte klasör zaten varsa, içeriği birleştir
                        for root, dirs, files in os.walk(source_path):
                            rel_path = os.path.relpath(root, source_folder)  # Göreceli yol hesapla
                            merge_target = os.path.join(main_folder, rel_path)

                            if not os.path.exists(merge_target):
                                os.makedirs(merge_target)  # Hedef klasörü oluştur

                            # Dosyaları kopyala (varsa üzerine yaz)
                            for file in files:
                                src_file = os.path.join(root, file)
                                dst_file = os.path.join(merge_target, file)
                                shutil.copy2(src_file, dst_file)

                else:  # Eğer kaynak bir dosyaysa
                    shutil.copy2(source_path, target_path)  # Dosya varsa üzerine yaz, yoksa ekle

            time.sleep(2)  # 2 saniye bekler
            print("Güncelleme yüklendi! Geçici dosyalar temizleniyor...")
        

            # 5. Geçici çıkarma klasörünü ve ZIP dosyasını temizle
            os.remove(zip_path)  # ZIP dosyasını sil
            shutil.rmtree(extract_folder)  # Geçici klasörü sil
            
            time.sleep(1)  # 1 saniye bekler
            print("Geçici dosyalar temizlendi!")

            new_version, old_version = Updater.version(self)
            str_new_version = ".".join(str(new_version))
            str_current_version =".".join(str(old_version))
            time.sleep(1)  # 1 saniye bekler
            print("UltraConsole V"+str_current_version+" 'dan V"+str_new_version+" 'a başarı ile güncellendi!")
            input("Devam etmek için Enter'a basın...")
            if new_version != old_version:
                os.system(os.path.join(main_folder, "main.py"))
            # time.sleep(1)  # 1 saniye bekler
        except Exception as e:
            print("Hata oluştu: "+e)

        

        





