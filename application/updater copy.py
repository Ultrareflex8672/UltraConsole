from html.parser import HTMLParser
import urllib.request
import zipfile
import shutil
import os
import time
import sys
import psutil
import signal

class Updater(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_target = False  # Belirtilen id'yi bulmak için bayrak
        self.data_list = []  # Bulunan verileri saklamak için liste
        self.current_version = 4001 # Bu programın sürümü


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

        # Güncelleme betiğinin içeriği
        update_script = '''
from html.parser import HTMLParser
import urllib.request
import zipfile
import shutil
import os
import time
import sys
# import psutil
# import signal
import subprocess

try:
    exe_name = "UltraConsole.exe"
    # for process in psutil.process_iter(attrs=['pid', 'name']):
    #     if process.info['name'] == exe_name:
    #         print(f"{exe_name} Kapatılıyor...")
    #         os.kill(process.info['pid'], signal.SIGTERM)
    #         print(f"{exe_name} kapatıldı.")
    # print(f"{exe_name} görevleri sonlandırıldı.")

    try:
        if sys.platform.startswith("win"):
            os.system(f"taskkill /F /IM {exe_name} 2>nul")
        else:
            os.system(f"pkill -f {exe_name} 2>/dev/null")
        print(f"{exe_name} kapatıldı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")
        
    if getattr(sys, 'frozen', False):
        exe_path = sys.executable
        current_dir = os.path.dirname(exe_path)
        main_folder = current_dir
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        main_folder = parent_dir

    zip_url = "https://github.com/Ultrareflex8672/UltraConsole/archive/refs/heads/main.zip"
    zip_path = os.path.join(main_folder, "UltraConsole.zip")

    print("Güncelleme dosyası indiriliyor...")
    urllib.request.urlretrieve(zip_url, zip_path)
    time.sleep(3)
    print("İndirme tamamlandı!")

    extract_folder = os.path.join(main_folder, "extracted")
    
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)

    print("Güncelleme dosyası çıkarıldı!")

    source_folder = os.path.join(main_folder, "extracted", "UltraConsole-main")

    for item in os.listdir(source_folder):
        source_path = os.path.join(source_folder, item)
        target_path = os.path.join(main_folder, item)
        try:
            if os.path.isdir(source_path):
                if not os.path.exists(target_path):  
                    shutil.copytree(source_path, target_path)
                else:
                    for root, dirs, files in os.walk(source_path):
                        rel_path = os.path.relpath(root, source_folder)
                        merge_target = os.path.join(main_folder, rel_path)

                        if not os.path.exists(merge_target):
                            os.makedirs(merge_target)

                        for file in files:
                            src_file = os.path.join(root, file)
                            dst_file = os.path.join(merge_target, file)
                            shutil.copy2(src_file, dst_file)
            else:
                shutil.copy2(source_path, target_path)
        except Exception as e:
            print(f"Hata oluştu: {e}")

    time.sleep(2)
    print("Güncelleme yüklendi! Geçici dosyalar temizleniyor...")

    os.remove(zip_path)
    shutil.rmtree(extract_folder)
    shutil.rmtree("UC_updater")

    print("Geçici dosyalar temizlendi!")

    input("Devam etmek için Enter'a basın...")
except Exception as e:
    print("Hata oluştu: ", e)
    input("Hata oluştu, devam etmek için Enter'a basın...")
    
# Bir üst dizindeki UltraConsole.exe'nin tam yolunu al
#exe_dir = os.path.dirname(os.getcwd())  # Üst dizin yolu
#exe_path = os.path.join(exe_dir, "UltraConsole.exe")  # UltraConsole.exe'nin tam yolu

# exe'nin kendi dizininde çalışmasını sağlamak için 'cwd' parametresi kullanılır
subprocess.run([exe_name])
                            '''

        os.makedirs("UC_updater", exist_ok=True)  # Eğer yoksa klasörü oluştur
        with open("UC_updater/update.py", "w", encoding="utf-8") as file:
            file.write(update_script)

        # Güncelleme betiğini çalıştır
        python_cmd = "python" if sys.platform.startswith("win") else "python3"
        os.system(f"{python_cmd} UC_updater/update.py")
    
    




        

        

        





