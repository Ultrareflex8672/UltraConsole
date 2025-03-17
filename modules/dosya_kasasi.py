from application.ultraconsole import UltraConsole as UC
from application.log import log_ekle as LOG
import os
import sys
import subprocess
import hashlib
import uuid
import shutil

menu_json = {
    "Kilitli Dosya Kasası": { 
        "Kasayı Kilitle": "dosya_kasasi", 
        "Kasayı Görüntüle": "dosya_kasasi"
    }
}

def dosya_kasasi(**kwargs):
        if UC.from_main_menu(**kwargs):
            user_data = kwargs.get("user_data")
            if user_data[3] == 0:
                menu_json["Kilitli Dosya Kasası"]["Ana Kasa Erişim Yetkisi"] = "dosya_kasasi"
            kwargs.update({"menu_data": menu_json})
            cpassword = user_data[2]
            main_dir, safe_dir, user_unlock_folder, user_unlock_temp_folder, user_lock_folder = get_dir(**kwargs)
            try:
                if not os.path.exists(user_unlock_temp_folder):
                    subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
                    subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                    subprocess.run(f'icacls "{user_lock_folder}" /remove:d Everyone', shell=True)
                    subprocess.run(f'icacls "{user_lock_folder}" /grant Everyone:(OI)(CI)F', shell=True)
                    os.rename(user_lock_folder, user_unlock_temp_folder)
            finally:
                if not os.path.exists(user_unlock_folder) and not os.path.exists(user_unlock_temp_folder):
                    os.makedirs(user_unlock_folder)
                    LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) için dosya kasası oluşturuldu.")
                    UC.create_frame("⚿ Yeni Dosya Kasası ☑", f"{user_data[1]} kullanıcısı için mevcut bir kilitli yada kilitsiz kasa bulunamadı. {user_unlock_folder} konumuna yeni kilitsiz bir kasa başarı ile oluşturuldu.", "info")
                subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
                subprocess.run(f'icacls "{safe_dir}" /deny Everyone:(D)', shell=True)
                UC.go_custom_menu(0, **kwargs)
        elif UC.selected_key(1, **kwargs):
            lock_folder(**kwargs)
        elif UC.selected_key(2, **kwargs):
            unlock_folder(**kwargs)
        elif UC.selected_key(3, **kwargs):
            remove_per(**kwargs)
        else:
            del kwargs["menu_data"]
        
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
            UC.create_frame("⚿ Kasa Kilitlendi ☑", f"{user_unlock_folder} konumunda bulunan kasanız başarı ile kilitlendi.", "info")
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
            UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için mevcut kasayı açmadan önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
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
            UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için mevcut kasayı açmadan önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
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
            UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için kasayı silmeden önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
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
        UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için kilidi açmadan önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
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
            UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için mevcut kasayı açmadan önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
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
            UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için mevcut kasayı açmadan önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
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
            UC.create_frame("⚿ Şifre Girişi ⚠", "Güvenliğiniz için kasayı silmeden önce UltraConsole hesap şifrenizi girimeniz gereklidir", "info")
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

def remove_per(**kwargs):
    user_data = kwargs.get("user_data")
    user_type = user_data[3]
    if user_type == 0:
        main_dir, safe_dir, user_unlock_folder, user_unlock_temp_folder, user_lock_folder = get_dir(**kwargs)
        selecetion = UC.create_frame("⚿ Ana Kasa Erişimi ⚠", f"Devam ederseniz {safe_dir} kalsörü erişim yetkileri kısa süre için açılacaktır. Ancak bu işlem diğer kullanıcıların dosya kasalarına erişim yetkisi vermez. Bu seçeneği UltraConsole konumunu değiştirmek yada sistemden kaldırmak gibi durumlarda kullanınız.", "Devam edilsin mi? (E/H)")
        if selecetion.lower() == "e":
            subprocess.run(f'icacls "{safe_dir}" /remove:d Everyone', shell=True)
            subprocess.run(f'icacls "{safe_dir}" /grant Everyone:(OI)(CI)F', shell=True)
            LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) ana kasa dizini erişim yetkisi kısıtlama önlemlerini devre dışı bıraktı.")
            UC.create_frame("⚿ Ana Kasa Erişimi ☑", f"{safe_dir} klasörü erişim yetki kısıtlaması tekrar kasa şifreleme yada görüntüleme işlemi yapılana kadar kaldırıldı!")
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

