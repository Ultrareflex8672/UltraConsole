from application.ultraconsole import UltraConsole as UC
from application.log import log_ekle as LOG
from colorama import Fore, Back, Style
import os
import sys
import subprocess
import hashlib
import uuid
import shutil
import win32com.client
import random

access_authorization = False

def dosya_kasasi(**kwargs):
        user_data = kwargs.get("user_data")
        cpassword = user_data[2]
        main_dir, safe_dir, user_unlock_folder, user_unlock_temp_folder, user_lock_folder = get_dir(**kwargs)
        try:
            if not os.path.exists(user_unlock_temp_folder):
                subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{user_lock_folder}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{user_lock_folder}" /grant Everyone:(OI)(CI)F', shell=True)
                os.rename(user_lock_folder, user_unlock_temp_folder)
        except:
            pass
        finally:
            if not os.path.exists(user_unlock_folder) and not os.path.exists(user_unlock_temp_folder):
                os.makedirs(user_unlock_folder)
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) için dosya kasası oluşturuldu.")
                UC.create_frame("⚿ Yeni Dosya Kasası ☑", f"{user_data[1]} kullanıcısı için mevcut bir kilitli yada kilitsiz kasa bulunamadı. {user_unlock_folder} konumuna yeni kilitsiz bir kasa başarı ile oluşturuldu.", "info")
            subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
        
        if os.path.exists(user_unlock_folder) and not os.path.exists(user_unlock_temp_folder):
            menu_items = ["⚿  Kasayı Kilitle", "🗀  Kasayı Görüntüle"]
            if user_data[3] == 0:
                menu_items.append("⚠  Kasa Yönetimi (ADMIN)")
            menu_items = menu_items + ["Ana Menü"]
            UC.cls()
            if user_data[3] == 0:
                print(Fore.RED + Back.GREEN +"Uyarı:")
                print(Style.RESET_ALL + Fore.RED + "Bir yönetici hesabı ile giriş \nyaptınız.\n")
                print("Yönetici hesapları kasa yönetim \naraçlarını da içerir.\n")
                print("Şahsi kullanım için \n"+Back.GREEN+"standart kullanıcı"+Style.RESET_ALL + Fore.RED+" hesabı ile \ngiriş yapmanız "+Back.GREEN+"tavsiye edilir.")
                print(Style.RESET_ALL)
            selection = int(UC.create_frame("🗁  Kasa Kilidi Açık", menu_items, "menu"))
            if selection == 1:
                lock_folder(**kwargs)
            elif selection == 2:
                unlock_folder(**kwargs)
            elif selection == 3:
                admin(**kwargs)
            elif selection != 0:
                UC.create_frame("⚿ Dosya Kasası Modülü ⚠", f"Lütfen geçerli bir seçim yapınız.", "info")
                dosya_kasasi(**kwargs)
        if not os.path.exists(user_unlock_folder) and os.path.exists(user_unlock_temp_folder):
            menu_items = ["⚿  Kasa Kilidini Aç"]
            if user_data[3] == 0:
                menu_items.append("⚠  Kasa Yönetimi (ADMIN)")
            menu_items = menu_items + ["Ana Menü"]
            UC.cls()
            if user_data[3] == 0:
                print(Fore.RED + Back.GREEN +"Uyarı:")
                print(Style.RESET_ALL + Fore.RED + "Bir yönetici hesabı ile giriş \nyaptınız.\n")
                print("Yönetici hesapları kasa yönetim \naraçlarını da içerir.\n")
                print("Şahsi kullanım için \n"+Back.GREEN+"standart kullanıcı"+Style.RESET_ALL + Fore.RED+" hesabı ile \ngiriş yapmanız "+Back.GREEN+"tavsiye edilir.")
                print(Style.RESET_ALL)
            selection = int(UC.create_frame("⚿  Kasa Kilitli", menu_items, "menu"))
            if selection == 1:
                unlock_folder(**kwargs)
            elif selection == 2:
                admin(**kwargs)
            elif selection != 0:
                UC.create_frame("⚿ Dosya Kasası Modülü ⚠", f"Lütfen geçerli bir seçim yapınız.", "info")
                dosya_kasasi(**kwargs)
        if os.path.exists(user_unlock_folder) and os.path.exists(user_unlock_temp_folder):
            menu_items = ["⚿  Kasa Kilitleme Seçenekleri", "🗀 Kasayı Görüntüleme Seçenekleri"]
            if user_data[3] == 0:
                menu_items.append("⚠  Kasa Yönetimi (ADMIN)")
            menu_items = menu_items + ["Ana Menü"]
            UC.cls()
            if user_data[3] == 0:
                print(Fore.RED + Back.GREEN +"Uyarı:")
                print(Style.RESET_ALL + Fore.RED + "Bir yönetici hesabı ile giriş \nyaptınız.\n")
                print("Yönetici hesapları kasa yönetim \naraçlarını da içerir.\n")
                print("Şahsi kullanım için \n"+Back.GREEN+"standart kullanıcı"+Style.RESET_ALL + Fore.RED+" hesabı ile \ngiriş yapmanız "+Back.GREEN+"tavsiye edilir.")
                print(Style.RESET_ALL)
            selection = int(UC.create_frame("🗁⚿  Kasa Kilidi Açık/Kilitli", menu_items, "menu"))
            if selection == 1:
                lock_folder(**kwargs)
            elif selection == 2:
                unlock_folder(**kwargs)
            elif selection == 3:
                admin(**kwargs)
            elif selection != 0:
                UC.create_frame("⚿ Dosya Kasası Modülü ⚠", f"Lütfen geçerli bir seçim yapınız.", "info")
                dosya_kasasi(**kwargs)

        try:
            if os.path.exists(user_unlock_temp_folder):
                subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{user_unlock_temp_folder}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{user_unlock_temp_folder}" /grant Everyone:(OI)(CI)F', shell=True)
                os.system(f'attrib -h -s "{user_unlock_temp_folder}"')
                os.rename(user_unlock_temp_folder, user_lock_folder)
                os.system(f'attrib +h +s "{user_lock_folder}"')
                if access_authorization == False:
                    subprocess.run(f'icacls "{user_lock_folder}" /grant Everyone:(OI)(CI)F', shell=True)
                    subprocess.run(f'icacls "{user_lock_folder}" /deny Everyone:(D)', shell=True)
                
        finally:
            if access_authorization == False:
                subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                for items in os.listdir(safe_dir):
                    full_path = os.path.join(safe_dir, items)
                    if os.path.isdir(full_path) and "Control Panel.{" in full_path:
                        os.system(f'attrib +h +s "{full_path}"')
                        subprocess.run(f'icacls "{full_path}" /grant Everyone:(OI)(CI)F', shell=True)
                        subprocess.run(f'icacls "{full_path}" /deny Everyone:(D)', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
            
def lock_folder(**kwargs):
    user_data = kwargs.get("user_data")
    cpassword = user_data[2]
    main_dir, safe_dir, user_unlock_folder, user_unlock_temp_folder, user_lock_folder = get_dir(**kwargs)
    if os.path.exists(user_unlock_folder) and not os.path.exists(user_unlock_temp_folder):
        selection = UC.create_frame("⚿ Kasa Kilitleme ⚠", "Kilitsiz kasanız kilitlenecek ve görüntülenmek istenildiğinde UltraConsole şifrenizi girmeniz istenecektir", "Devam edilsin mi? (E/H)")
        if selection.lower() == "e":
            subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
            os.rename(user_unlock_folder, user_lock_folder)
            os.system(f'attrib +h +s "{user_lock_folder}"')
            subprocess.run(f'icacls "{user_lock_folder}" /grant Everyone:(OI)(CI)F', shell=True)
            subprocess.run(f'icacls "{user_lock_folder}" /deny Everyone:(D)', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
            LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) kasasını kilitledi.")
            # UC.create_frame("⚿ Kasa Kilitlendi ☑", f"{user_unlock_folder} konumunda bulunan kasanız başarı ile kilitlendi.", "info")
            UC.create_frame("⚿  Kasa Kilitlendi ☑", "⚿  Kurtarma Anahtarınız: " + hashlib.md5(user_lock_folder.encode()).hexdigest())
    elif not os.path.exists(user_unlock_folder) and os.path.exists(user_unlock_temp_folder):
        selection = UC.create_frame("⚿ Kasa Kilitli ☑", "Kasanız zaten kilitli durumda. Kasanın kilidini açıp görüntülemek ister misiniz?", "(E/H)")
        if selection.lower() == "e":
            subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
            os.rename(user_unlock_temp_folder, user_lock_folder)
            os.system(f'attrib +h +s "{user_lock_folder}"')
            subprocess.run(f'icacls "{user_lock_folder}" /grant Everyone:(OI)(CI)F', shell=True)
            subprocess.run(f'icacls "{user_lock_folder}" /deny Everyone:(D)', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
            unlock_folder(**kwargs)
    elif os.path.exists(user_unlock_folder) and os.path.exists(user_unlock_temp_folder):
        UC.create_frame("⚿ Çift Kasa Mevcut ⚠", f"{safe_dir} konumunda hem kilitli hemde kilitsiz kasa bulundu! Lütfen bir sonraki adımda yapılacak işlemi seçin.")
        UC.cls()
        selection = int(UC.create_frame("⚿ Çift Kasa için Yapılacak İşlem ⚠", ["Kilitli Kasanın Üzerine Yaz", "Kilitli ve Kilitsiz Kasaları Aç", "Kilitli Kasayı Sil ve Yenisini Oluştur", "Geri Dön"], "menu"))
        if selection == 1:
            # UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için mevcut kasayı açmadan önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
            password = UC.get_pass(1)
            if cpassword == hashlib.md5(password.encode()).hexdigest():
                subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                os.rename(user_unlock_temp_folder, user_lock_folder)
                copy_directory(user_unlock_folder, user_lock_folder)
                delete_folder(user_unlock_folder)
                os.system(f'attrib +h +s "{user_lock_folder}"')
                subprocess.run(f'icacls "{user_lock_folder}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{user_lock_folder}" /deny Everyone:(D)', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) kilitsiz kasasındaki dosya ve klasörleri, kilitli kasasının üzerine yazarak kilitledi.")
                UC.create_frame("⚿ Kasa Kilitlendi ☑", f"{user_unlock_folder} konumunda bulunan kasanız, kilitsiz kasanızdaki dosya ve klasörler üzerine yazılarak başarı ile kilitlendi.", "info")
            else:
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) Dosya Kasası modülünde hatalı parola girdi.")
                UC.create_frame("⚿ Şifre Hatası ⛌", "Girdiğiniz Şifre Hatalıdır.", "info")
        elif selection == 2:
            # UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için mevcut kasayı açmadan önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
            password = UC.get_pass(1)
            if cpassword == hashlib.md5(password.encode()).hexdigest():
                subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.Popen(f'explorer "{user_unlock_folder}"')
                os.system(f'attrib -h -s "{user_unlock_temp_folder}"')
                subprocess.Popen(f'explorer "{user_unlock_temp_folder}"')
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) kilitli ve kilitsiz kasalarını görüntüledi.")
                UC.create_frame("⚿ Kasa Görüntüleme ☑", f"{user_unlock_folder} konumunda bulunan kilitsiz kasanız ve {user_unlock_temp_folder} konumunda bulunan kilitli kasanız düzenlemeleri yapabilmeniz için görüntülendi.", "info")
            else:
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) Dosya Kasası modülünde hatalı parola girdi.")
                UC.create_frame("⚿ Şifre Hatası ⛌", "Girdiğiniz Şifre Hatalıdır.", "info")
        elif selection == 3:
            # UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için kasayı silmeden önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
            password = UC.get_pass(1)
            if cpassword == hashlib.md5(password.encode()).hexdigest():
                subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                delete_folder(user_unlock_temp_folder)
                os.rename(user_unlock_folder, user_lock_folder)
                os.system(f'attrib +h +s "{user_lock_folder}"')
                subprocess.run(f'icacls "{user_lock_folder}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{user_lock_folder}" /deny Everyone:(D)', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) mevcut kilitli kasasını silerek kilitsiz kasasından yeni kilitli kasa oluşturdu.")
                UC.create_frame("⚿ Kasa Kilitlendi ☑", f"Mevcut kilitli kasanız, mevcut kilitsiz kasanız ile başarılı bir şekilde değiştirildi!", "info")
            else:
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) Dosya Kasası modülünde hatalı parola girdi.")
                UC.create_frame("⚿ Şifre Hatası ⛌", "Girdiğiniz Şifre Hatalıdır.", "info")
    else:
        LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) 'Kilitli yada kilitsiz herhangi bir kullanıcı kasaı bulunamadı!' hatası aldı.")
        UC.create_frame("⚿ Kasa Hatası ⛌", "Kilitli yada kilitsiz herhangi bir kullanıcı kasaı bulunamadı!", "info")
        
def unlock_folder(**kwargs):
    user_data = kwargs.get("user_data")
    cpassword = user_data[2]
    main_dir, safe_dir, user_unlock_folder, user_unlock_temp_folder, user_lock_folder = get_dir(**kwargs)
    if os.path.exists(user_unlock_folder) and not os.path.exists(user_unlock_temp_folder):
        subprocess.Popen(f'explorer "{user_unlock_folder}"')
        LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) kilitsiz olan kasasını görüntüledi.")
        selection = UC.create_frame("⚿ Kasa Kilidi Açık ☑", "Kasa kilidiniz açık! Şimdi kilitlemek ister misiniz?", "(E/H)")
        if selection.lower() == "e":
            lock_folder(**kwargs)
    elif os.path.exists(user_unlock_temp_folder) and not os.path.exists(user_unlock_folder):
        # UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için kilidi açmadan önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
        password = UC.get_pass(1)
        if cpassword == hashlib.md5(password.encode()).hexdigest():
            subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
            os.system(f'attrib -h -s "{user_unlock_temp_folder}"')
            os.rename(user_unlock_temp_folder, user_unlock_folder)
            subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
            subprocess.Popen(f'explorer "{user_unlock_folder}"')
            LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) kilitli olan kasasının kilidini açtı ve görüntüledi.")
            selection = UC.create_frame("⚿ Kasa Kilidi Açıldı ☑", "Kasanızın kilidi başarı ile açıldı! Tekrar kilitlemek ister misiniz?", "(E/H)")
            if selection.lower() == "e":
                lock_folder(**kwargs)
        else:
            LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) Dosya Kasası modülünde hatalı parola girdi.")
            UC.create_frame("⚿ Şifre Hatası ⛌", "Girdiğiniz Şifre Hatalıdır.", "info")
    elif os.path.exists(user_unlock_folder) and os.path.exists(user_unlock_temp_folder):
        UC.create_frame("⚿ Çift Kasa Mevcut ⚠", f"{safe_dir} konumunda hem kilitli hemde kilitsiz kasa bulundu! Lütfen bir sonraki adımda yapılacak işlemi seçin.")
        UC.cls()
        selection = int(UC.create_frame("⚿ Çift Kasa için Yapılacak İşlem ⚠", ["Kilitsiz Kasanın Üzerine Yaz", "Kilitli ve Kilitsiz Kasaları Aç", "Kilitsiz Kasayı Sil ve Yenisini Oluştur", "Geri Dön"], "menu"))
        if selection == 1:
            # UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için mevcut kasayı açmadan önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
            password = UC.get_pass(1)
            if cpassword == hashlib.md5(password.encode()).hexdigest():
                subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                copy_directory(user_unlock_temp_folder, user_unlock_folder)
                delete_folder(user_unlock_temp_folder)
                subprocess.Popen(f'explorer "{user_unlock_folder}"')
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) mevcut kilitsi kasasının kilidini açtı ve kilitsiz kasasındaki dosyalar ile birtleştirip görüntüledi.")
                selection = UC.create_frame("⚿ Kasa Kilidi Açıldı ☑", "Mevcut kilitli kasadaki dosyalar, kilitsiz kasadaki dosyalar ile başarılı bir şekilde birleştirildi! Tekrar kilitlemek ister misiniz?", "(E/H)")
                if selection.lower() == "e":
                    lock_folder(**kwargs)
            else:
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) Dosya Kasası modülünde hatalı parola girdi.")
                UC.create_frame("⚿ Şifre Hatası ⛌", "Girdiğiniz Şifre Hatalıdır.", "info")
        elif selection == 2:
            # UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için mevcut kasayı açmadan önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
            password = UC.get_pass(1)
            if cpassword == hashlib.md5(password.encode()).hexdigest():
                subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.Popen(f'explorer "{user_unlock_folder}"')
                os.system(f'attrib -h -s "{user_unlock_temp_folder}"')
                subprocess.Popen(f'explorer "{user_unlock_temp_folder}"')
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) kilitli ve kilitsiz kasalarını görüntüledi.")
                UC.create_frame("⚿ Kasa Kilidi Açıldı ☑", f"{user_unlock_folder} konumunda bulunan kilitsiz kasanız ve {user_unlock_temp_folder} konumunda bulunan kilitli kasanız düzenlemeleri yapabilmeniz için görüntülendi.", "info")
            else:
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) Dosya Kasası modülünde hatalı parola girdi.")
                UC.create_frame("⚿ Şifre Hatası ⛌", "Girdiğiniz Şifre Hatalıdır.", "info")
        elif selection == 3:
            # UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için kasayı silmeden önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
            password = UC.get_pass(1)
            if cpassword == hashlib.md5(password.encode()).hexdigest():
                subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                delete_folder(user_unlock_folder)
                os.system(f'attrib -h -s "{user_unlock_temp_folder}"')
                os.rename(user_unlock_temp_folder, user_unlock_folder)
                subprocess.Popen(f'explorer "{user_unlock_folder}"')
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) kilitli kasasının kilidini açarak mevcut kilitsiz kasası ile değiştirerek görüntüledi.")
                selection = UC.create_frame("⚿ Kasa Kilidi Açıldı ☑", "Mevcut kilitlisiz kasanız, mevcut kilitli kasanız ile değiştirildi! Kasanızı şimdi kilitlemek ister misiniz?", "(E/H)")
                if selection.lower() == "e":
                    lock_folder(**kwargs)
            else:
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) Dosya Kasası modülünde hatalı parola girdi.")
                UC.create_frame("⚿ Şifre Hatası ⛌", "Girdiğiniz Şifre Hatalıdır.", "info")
    else:
        LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) 'Kilitli yada kilitsiz herhangi bir kullanıcı kasaı bulunamadı!' hatası aldı.")
        UC.create_frame("⚿ Kasa Hatası ⛌", "Kilitli yada kilitsiz herhangi bir kullanıcı kasası bulunamadı!", "info")
    
def string_to_uuid3(string):
    md5_hash = hashlib.md5(string.encode()).hexdigest()
    return str(uuid.UUID(md5_hash))

def get_dir(**kwargs):
    user_data = kwargs.get("user_data")
    if getattr(sys, 'frozen', False):
        main_dir = os.path.dirname(sys.executable)
        safe_dir = os.path.join(os.path.dirname(sys.executable), "user_file_vaults")
        user_unlock_folder = os.path.join(os.path.dirname(sys.executable), "user_file_vaults",  user_data[1]+"_kilitsiz_kasa")
        user_unlock_temp_folder = os.path.join(os.path.dirname(sys.executable), "user_file_vaults",  user_data[1]+"_kilitli_kasa")
        user_lock_folder = os.path.join(os.path.dirname(sys.executable), "user_file_vaults", "Control Panel.{"+string_to_uuid3(user_data[1]+str(user_data[0]))+"}")
    else:
        main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        safe_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "user_file_vaults"))
        user_unlock_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "user_file_vaults", user_data[1]+"_kilitsiz_kasa"))
        user_unlock_temp_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "user_file_vaults", user_data[1]+"_kilitli_kasa"))
        user_lock_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "user_file_vaults","Control Panel.{"+string_to_uuid3(user_data[1]+str(user_data[0]))+"}"))

    if not os.path.exists(safe_dir):
        os.makedirs(safe_dir)
        subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
        subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
    else:
        subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
        subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)

    return main_dir, safe_dir, user_unlock_folder, user_unlock_temp_folder, user_lock_folder

def admin(**kwargs):
    user_data = kwargs.get("user_data")
    user_type = user_data[3]
    if user_type == 0:
        UC.cls()
        selection = int(UC.create_frame("⚿ Kasa Yönetici Menüsü", ["⚠ Ana Dizin Erişim Yetkisi", "🖿 Kasa Kurtarma"]+["Geri Dön"], "menu"))
        if selection == 1:
            remove_per(**kwargs)
        elif selection == 2:
            recovery(**kwargs)
        elif selection != 0:
            UC.create_frame("⚿ Dosya Kasası Modülü ⚠", f"Lütfen geçerli bir seçim yapınız.", "info")
            admin(**kwargs)
    else:
        LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) yetkisi bulunmadığı için ana kasa yönetim modülü girişi başarısız oldu.")
        UC.create_frame("⚿ Ana Kasa Erişimi ⛌", f"Bu işlem için yetkiniz yok! Lütfen sistem yöneticinize başvurun.")

def remove_per(**kwargs):
    user_data = kwargs.get("user_data")
    cpassword = user_data[2]
    user_type = user_data[3]
    global access_authorization
    if user_type == 0:
        password = UC.get_pass(1)
        if cpassword == hashlib.md5(password.encode()).hexdigest():
            main_dir, safe_dir, user_unlock_folder, user_unlock_temp_folder, user_lock_folder = get_dir(**kwargs)
            selecetion = UC.create_frame("⚿ Dizin Erişim Engeli ⚠", f"Devam ederseniz {safe_dir} kalsörü erişim engellemesi kısa süre için kaldırılacaktır. Bu işlem diğer kullanıcıların dosya kasalarına erişim yetkisi vermez. Bu seçeneği UltraConsole 'un konumunu değiştirmek yada sistemden kaldırmak gibi işlemler için kullanınız. Hatalı kullanım toplu veri kayıpları dahil büyük sorunlara yol açabilir!", "Devam edilsin mi? (E/H)")
            if selecetion.lower() == "e":
                subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                for items in os.listdir(safe_dir):
                    full_path = os.path.join(safe_dir, items)
                    if os.path.isdir(full_path):
                        subprocess.run(f'icacls "{full_path}" /remove:d Everyone', shell=True)
                        subprocess.run(f'icacls "{full_path}" /grant Everyone:(OI)(CI)F', shell=True)
                access_authorization = True
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) ana kasa dizini erişim yetkisi kısıtlama önlemlerini devre dışı bıraktı.")
                UC.create_frame("⚿ Dizin Erişimi Verildi ☑", f"{safe_dir} klasörü erişim kısıtlaması tekrar kasa şifreleme yada görüntüleme işlemi yapılana kadar kaldırıldı!")
        else:
            LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) Dosya Kasası modülünde hatalı parola girdi.")
            UC.create_frame("⚿ Şifre Hatası ⛌", "Girdiğiniz Şifre Hatalıdır.", "info")
    else:
        LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) yetkisi bulunmadığı için ana kasa dizini erişim yetkisi kısıtlama önlemlerini devre dışı bırakma girişiminde başarısız oldu.")
        UC.create_frame("⚿ Ana Kasa Erişimi ⛌", f"Bu işlem için yetkiniz yok! Lütfen sistem yöneticinize başvurun.")

def copy_with_merge(src, dest):
    if os.path.isfile(src):
        shutil.copy2(src, dest)
    elif os.path.isdir(src):
        if not os.path.exists(dest):
            os.makedirs(dest)
        
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dest, item)
            
            copy_with_merge(s, d)

def copy_directory(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for item in os.listdir(src_dir):
        source_item = os.path.join(src_dir, item)
        destination_item = os.path.join(dest_dir, item)
        
        if os.path.isfile(source_item):
            shutil.copy2(source_item, destination_item)
        elif os.path.isdir(source_item):
            copy_with_merge(source_item, destination_item)
    
def delete_folder(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        print(f"{folder_path} başarıyla silindi.")
    else:
        print(f"{folder_path} bulunamadı veya geçerli bir klasör değil.")

def recovery(**kwargs):
    user_data = kwargs.get("user_data")
    user_type = user_data[3]
    main_dir, safe_dir, user_unlock_folder, user_unlock_temp_folder, user_lock_folder = get_dir(**kwargs)
    if user_type == 0:
        UC.cls()
        selection = int(UC.create_frame("🖿 Kasa Kurtarma ⚠", ["Kurtarma Anahtarı ile Kurtar", "Kilidi Sıkışmış Kasaları Listele"]+["Geri Dön"], "menu"))
        if selection == 1:
            recovery_key = UC.create_frame("🖿 Anahtar ile Kasa Kurtarma ⚠", "Kasa Kurtarma İşlemi için Kasanız Kilitlendiğinde Ekrand Görünen Kurtarma Anahtarını Gereklidir!", "⚿ Kurtarma Anahtarınız: \n")
            subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
            subprocess.run(f'icacls "{user_unlock_temp_folder}" /remove:d Everyone', shell=True)
            subprocess.run(f'icacls "{user_unlock_temp_folder}" /grant Everyone:(OI)(CI)F', shell=True)
            os.system(f'attrib -h -s "{user_unlock_temp_folder}"')
            os.rename(user_unlock_temp_folder, user_lock_folder)
            os.system(f'attrib +h +s "{user_lock_folder}"')
            subprocess.run(f'icacls "{user_lock_folder}" /grant Everyone:(OI)(CI)F', shell=True)
            subprocess.run(f'icacls "{user_lock_folder}" /deny Everyone:(D)', shell=True)
            shell = win32com.client.Dispatch("Shell.Application")

            folders = []
            for items in os.listdir(safe_dir):
                full_path = os.path.join(safe_dir, items)
                # Sadece klasörleri al
                if os.path.isdir(full_path):
                    folders.append(full_path)
                    try:
                        # Eğer CLSID içeriyorsa, gerçek adını bul
                        shotcut = shell.Namespace(full_path)
                        if shotcut:
                            # folders.append(f"{full_path} ({shotcut.Title})")
                            # folders.append(shotcut.Title)
                            pass
                    except:
                        pass

            success = False
            for i in folders:
                if recovery_key == hashlib.md5(i.encode()).hexdigest():
                    success = True
                    recovery_path = i
                    rand_int = random.randint(10000, 99999)
                    ext_path = os.path.join(main_dir, "recovered_"+str(rand_int))
                    if recovery_path:
                        subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                        subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                        subprocess.run(f'icacls "{recovery_path}" /remove:d Everyone', shell=True)
                        subprocess.run(f'icacls "{recovery_path}" /grant Everyone:(OI)(CI)F', shell=True)
                        os.system(f'attrib -h -s "{recovery_path}"')
                        os.rename(recovery_path, ext_path)
                        subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                        subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                        subprocess.Popen(f'explorer "{ext_path}"')
                        LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) {recovery_path} kasasındaki verileri {ext_path} klasörüne kurtarma anahtarı kullanarak çıkardı.")
                        UC.create_frame("🖿 Kasa Kurtarma Başarılı ☑", f"Girilen Anahtarla Kilitlenmiş olan kasa {ext_path} konumuna çıkartıldı!")
            if success == False:
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) {recovery_key} anahtarı ile kurtarma denedi ancak kasa bulunamadı.")
                selection = UC.create_frame("🖿 Kasa Kurtarma ⛌", "Girilen Anahtarla Kilitlenmiş Bir Kasa Bulunamadı! Tam kilitlenmemiş kasalarda arama yapmak ister misiniz?","(E/H)")
                if selection.lower() == "e":
                    stack_lock(**kwargs)
        elif selection == 2:
            stack_lock(**kwargs)
        elif selection != 0:
            UC.create_frame("⚿ Dosya Kasası Modülü ⚠", f"Lütfen geçerli bir seçim yapınız.", "info")
            recovery(**kwargs)
    else:
        LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) yetkisi bulunmadığı için anahtar ile kasa kurtarma girişimi reddedildi.")
        UC.create_frame("⚿ Ana Kasa Erişimi ⛌", f"Bu işlem için yetkiniz yok! Lütfen sistem yöneticinize başvurun.")

def stack_lock(**kwargs):
    user_data = kwargs.get("user_data")
    cpassword = user_data[2]
    user_type = user_data[3]
    if user_type == 0:
        password = UC.get_pass(1)
        if cpassword == hashlib.md5(password.encode()).hexdigest():
            main_dir, safe_dir, user_unlock_folder, user_unlock_temp_folder, user_lock_folder = get_dir(**kwargs)
            folders = []
            items_ = []
            subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
            subprocess.run(f'icacls "{user_unlock_temp_folder}" /remove:d Everyone', shell=True)
            subprocess.run(f'icacls "{user_unlock_temp_folder}" /grant Everyone:(OI)(CI)F', shell=True)
            os.system(f'attrib -h -s "{user_unlock_temp_folder}"')
            os.rename(user_unlock_temp_folder, user_lock_folder)
            os.system(f'attrib +h +s "{user_lock_folder}"')
            subprocess.run(f'icacls "{user_lock_folder}" /grant Everyone:(OI)(CI)F', shell=True)
            subprocess.run(f'icacls "{user_lock_folder}" /deny Everyone:(D)', shell=True)
            for items in os.listdir(safe_dir):
                full_path = os.path.join(safe_dir, items)
                # Sadece klasörleri al
                if os.path.isdir(full_path) and "Control Panel.{" not in full_path:
                    folders.append(full_path)
                    items_.append(items)
            if folders != []:
                UC.cls()
                selection = int(UC.create_frame("🖿 Kilidi Sıkışmış Kasa Listesi ⚠", items_+["Geri Dön"], "menu"))
                if selection != 0:
                    recovery_path = folders[selection-1]
                    rand_int = random.randint(10000, 99999)
                    ext_path = os.path.join(main_dir, "recovered_"+str(rand_int))
                    if recovery_path:
                        subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                        subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                        subprocess.run(f'icacls "{recovery_path}" /remove:d Everyone', shell=True)
                        subprocess.run(f'icacls "{recovery_path}" /grant Everyone:(OI)(CI)F', shell=True)
                        os.system(f'attrib -h -s "{recovery_path}"')
                        os.rename(recovery_path, ext_path)
                        subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                        subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                        subprocess.Popen(f'explorer "{ext_path}"')
                        LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) sıkışmış olan {recovery_path} kasasındaki verileri {ext_path} klasörüne çıkardı.")
                        UC.create_frame("🖿 Kasa Kurtarma Başarılı ☑", f"{recovery_path} kasaındaki veriler {ext_path} konumuna çıkartıldı!")
            else:
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) sıkışmış kasalarda arama yaptı ancak hiç bir kasa bulunamadı.")
                UC.create_frame("🖿 Kasa Kurtarma ⛌", f"Kilidi sıkışmış hiç bir kasa bulunamadı!")
        else:
            LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) Dosya Kasası modülünde hatalı parola girdi.")
            UC.create_frame("⚿ Şifre Hatası ⛌", "Girdiğiniz Şifre Hatalıdır.", "info")
    else:
        LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) yetkisi bulunmadığı için sıkışmış kasa kurtarma girişimi reddedildi.")
        UC.create_frame("⚿ Ana Kasa Erişimi ⛌", f"Bu işlem için yetkiniz yok! Lütfen sistem yöneticinize başvurun.")