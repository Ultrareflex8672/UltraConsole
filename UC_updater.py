from html.parser import HTMLParser
import urllib.request
import zipfile
import shutil
import os
import time
import sys
import subprocess

exe_name = "UltraConsole.exe"
selection = input("\n</> UltraConsol kaynak kodlarının da indirilmesini istiyor musunuz?\n(Kaynak kodlar FrameWaork geliştricileri için gereklidir, yalnız modül geliştirici iseniz genellikle gerekli değildir)\n(E/H): ")

try:
    # Çalışan ana programı kapat
    try:
        print(f"✖ {exe_name} kapatılıyor...")
        if sys.platform.startswith("win"):
            os.system(f"taskkill /F /IM {exe_name} 2>nul")
        else:
            os.system(f"pkill -f {exe_name} 2>/dev/null")
        print("██ 10%")
        print(f"❎ {exe_name} kapatıldı! Güncelleme işlemi devam ediyor...")
        time.sleep(1)
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
    # Alternetif kapatma yolu
    # for process in psutil.process_iter(attrs=['pid', 'name']):
    #     if process.info['name'] == exe_name:
    #         print(f"{exe_name} Kapatılıyor...")
    #         os.kill(process.info['pid'], signal.SIGTERM)
    #         print(f"{exe_name} kapatıldı.")
    # print(f"{exe_name} görevleri sonlandırıldı.")
    
    # Dosya ve klasör yollrını tanımla
    if getattr(sys, 'frozen', False):
        exe_path = sys.executable
        current_dir = os.path.dirname(exe_path)
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))

    parent_dir = os.path.dirname(current_dir)

    if os.path.exists(os.path.join(current_dir, exe_name)):
        main_folder = current_dir
        temp_folder = os.path.join(main_folder, "UC_updater")
        os.makedirs(os.path.join(main_folder, "UC_updater"), exist_ok=True)
    elif os.path.exists(os.path.join(parent_dir, exe_name)):
        main_folder = parent_dir
        temp_folder = current_dir
        os.makedirs(os.path.join(main_folder, "UC_updater"), exist_ok=True)
    else:
        raise Exception(f"Güncelleme yapılacak '{exe_name}' bulunamadı. 'UC_updater' ı '{exe_name}' nin bulunduğu klasörde ya da alt klasöründe çalıştırın.")

    
    zip_url = "https://github.com/Ultrareflex8672/UltraConsole/archive/refs/heads/main.zip"
    zip_path = os.path.join(temp_folder, "UltraConsole.zip")
    UC_path = os.path.join(main_folder, exe_name)
    extract_folder = os.path.join(temp_folder, "extracted")
    source_folder = os.path.join(temp_folder, "extracted", "UltraConsole-main")

    # path_list = [f"exe_name:{exe_name}", f"exe_path:{exe_path}", f"current_dir:{current_dir}", f"parent_dir:{parent_dir}", f"main_folder:{main_folder}", f"temp_folder:{temp_folder}", f"zip_path:{zip_path}", f"extract_folder:{extract_folder}", f"source_folder:{source_folder}"]
    # for i in path_list:
    #     print(i)

    if current_dir and parent_dir and main_folder and exe_name and zip_url and zip_path and extract_folder and temp_folder:
        try:
            print("⬇️ Güncelleme dosyası indiriliyor...")
            urllib.request.urlretrieve(zip_url, zip_path)
            print("████████ 25%")
            print("✅ Güncelleme dosyası indirildi! Güncelleme işlemi devam ediyor...")
            time.sleep(1)
            print("📤 Güncelleme dosyaları çıkartılıyor...")
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(extract_folder)
            print("███████████████ 50%")
            print("✅ Güncelleme dosyaları çıkarıldı! Güncelleme işlemi devam ediyor...")
            time.sleep(1)
        except Exception as e:
            print("❌ Hata oluştu: ", e)

        
        not_including = {"application", "main.py", "UC_updater.py", "pyinstaller.txt", "requirements.txt", ".gitignore", "CHANGELOG.md"}

        for item in os.listdir(source_folder):
            if selection.lower() == "h" and item in not_including:
                print(f"❌ {item} atlandı.")
                continue

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
                print(f"❌ Hata oluştu: {e}")
        try:
            # time.sleep(2)
            print("🧹 Geçici dosyalar temizleniyor...")

            os.remove(zip_path)

            if main_folder == parent_dir:
                shutil.rmtree(extract_folder)
            else:
                shutil.rmtree(temp_folder)
            print("██████████████████████ 75%")
            print("✅ Geçici dosyalar temizlendi!")
            time.sleep(2)
            print("██████████████████████████████ 100%")
            print("\n🔄 UltraConsole başarı ile güncellendi! ✅")
            time.sleep(1)
            input("\nDevam etmek için Enter'a basın... ➡️")
        except Exception as e:
                print(f"⚠️ İşlem hatalarla tamamlandı! Güncelleme doğru yüklenmemiş olabilir. Hata: {e}")
    else:
        raise Exception("❌ Güncelleme devam edemiyor! Dosya yada klasör yollarında sorun var.")
    
except Exception as e:
    print("❌ Hata oluştu: ", e)
    input("Devam etmek için Enter'a basın... ➡️")
    
subprocess.run([UC_path])