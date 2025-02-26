from application.menu_olusturucu import MenuSystem as MS
from application.sql_islem import SqlProcess as SQL
import os
import json
import re
import hashlib
import getpass
import sqlite3

class SettingsMenu():
    # def __init__(self, **kwargs):
    #     self.config = MS.read_config() 
    #     self.database_folder = self.config.get("database_path")
    #     self.database_file = self.config.get("users_db_file")
    #     self.database_path = os.path.join(self.database_folder, self.database_file)
    #     self.kwargs = kwargs

    def menu_goster(self, **kwargs):
        config = MS.read_config()                                   # Ayarları oku
        menu_data = MS.load_json(config["menu_file"])               # Menü verilerini yükle
        root = list(menu_data.keys())[int(config.get("settings_menu_root"))]

        settings_menu = MS(menu_data[root], 1, "application", "settings", "SettingsMenu", None, "settings", **kwargs)                                    # Menü sistemini başlat (init fonksiyonu çalışır ancak henüz menü gösterilmez)
        settings_menu.show_menu(root)
        
    def settings(self, **kwargs):
        # input(kwargs)
        my_profil_data = list(kwargs.get("user_data"))
        if kwargs.get("selected_key") == 1:
            SettingsMenu.ayarlari_goster(MS.read_config())
        elif kwargs.get("selected_key") == 2:
            SettingsMenu.ayar_degistir(MS.read_config())
        elif kwargs.get("selected_key") == 3:
            SettingsMenu.menu_islem()
        elif kwargs.get("selected_key") == 4:
            SettingsMenu.profil(**kwargs)
        elif kwargs.get("selected_key") == 5:
            if my_profil_data[3] == 0:
                SettingsMenu.users(**kwargs)
            else:
                MS.create_frame("Erişim Yetkisi Hatasu", "Bu menüye erişiminiz reddedildi. Yönetici yetkisi gerekli.")

    def ayarlari_goster(ayarlar):
        ayar_dokumu = "            ".join(f"{key}: {value}" for key, value in ayarlar.items())
        MS.create_frame("Mevcut Ayarlar", ayar_dokumu)
    
    def ayar_degistir(ayarlar):
        while True:
            ayarlar_listesi = [f"{key}: {value}" for key, value in ayarlar.items()]
            os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
            secim = MS.create_frame("Ayar Değiştirme Menüsü", ayarlar_listesi + ["Geri Dön"], "menu")
            
            if secim.lower() == "0":
                os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
                break
            
            if secim.isdigit() and 1 <= int(secim) <= len(ayarlar):
                secim_index = int(secim) - 1
                secilen_anahtar = list(ayarlar.keys())[secim_index]
                yeni_deger = MS.create_frame("Yeni Değer Girişi", f"Uyarı: {secilen_anahtar} için yeni değeri girişi yapılıyor ", "Yeni değer:\n")
                if yeni_deger:
                    eminmisiniz = MS.create_frame("Yeni Değer Girişi", f"Uyarı: {secilen_anahtar} değeri {yeni_deger} olarak değiştirilecektir. Bu değişikliği yapmak istediğinize emin misiniz?", "E/H\n")
                    if eminmisiniz.lower() == "e":
                        ayarlar[secilen_anahtar] = yeni_deger
                        SettingsMenu.ayarlari_kaydet(ayarlar)
            else:
                MS.create_frame("Hata", "Geçersiz seçim yapıldı. Lütfen tekrar deneyin.")

    
    def ayarlari_kaydet(ayarlar):
        MS.save_config(ayarlar)
        MS.create_frame("Ayarlar Kaydedildi", "Ayarlar başarıyla kaydedildi.")

    def menu_islem():
        config = MS.read_config()                                   # Ayarları oku
        menu_data = MS.load_json(config["menu_file"])               # Menü verilerini yükle
        root = list(menu_data.keys())[int(config.get("menu_root"))]

        no_submenu_keys = []

        for key, value in menu_data[root].items():
            if not isinstance(value, dict):  # Eğer değeri bir sözlük değilse (yani alt menüsü yoksa)
                no_submenu_keys = no_submenu_keys+[key]
        

        options_for_selection = ["Ekle", "Sil", "Değiştir", "Geri Dön"]
        os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
        operation = int(MS.create_frame("İşleminizi Seçin", options_for_selection, "menu"))
        if operation == 2 or operation == 3:
            os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
            selection  = MS.create_frame("İşlem Yapmak İstediğiniz Modülü Seçiniz", no_submenu_keys+["Geri Dön"], "menu")
            if operation == 2:
                if no_submenu_keys[int(selection)-1] in menu_data[root]:
                    warn = MS.create_frame("SİLME İŞLEMİ ONAYI!", str(no_submenu_keys[int(selection)-1])+" adlı modül menüden silinmek üzrere! İşleme devam etmek istiyormusunuz!", "(E/H)")
                    if warn.lower() == "e":
                        del menu_data[root][no_submenu_keys[int(selection)-1]]
                        SettingsMenu.save_menu(menu_data)
                        MS.create_frame("MODÜL SİLİNDİ!", str([no_submenu_keys[int(selection)-1]])+" adlı modül menüden başarı ile silindi", "info")
                    else:
                        MS.create_frame("Silme İşlemi İptal Edildi", str([no_submenu_keys[int(selection)-1]])+" adlı modül silinmedi!", "info")
                else:
                    MS.create_frame("Modül Bulunamadı", str([no_submenu_keys[int(selection)-1]])+" adlı modül bulunamadı!", "info")
                    
            if operation == 3:
                if no_submenu_keys[int(selection)-1] in menu_data[root]:
                    ckey = no_submenu_keys[int(selection)-1]
                    cvalue = menu_data[root][ckey]
                    os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
                    opt = MS.create_frame(ckey+" Modülünde Yapılacak Değişikliği Seçin", ["Modül Adı","Fonsiyon Adı","Her İkisi","Geri Dön"], "menu")
                    if int(opt) == 1:
                            while True:
                                new_name = MS.create_frame("Modül Adı Değiştirme", ckey+" adlı modül için yeni ad girin!", "")
                                if new_name not in menu_data[root]:
                                    warn = MS.create_frame("Modül Adı Değiştirme", ckey+" modülünün adını "+new_name+" olarak değiştirmek üzeresiniz! Devam etmek istiyor musunuz?", "(E/H)")
                                    if warn.lower() == "e":
                                        menu_data[root][new_name] = menu_data[root][ckey]
                                        del menu_data[root][ckey]
                                        SettingsMenu.save_menu(menu_data)
                                        MS.create_frame("Modül Adı Değiştirme", ckey+" modülünün adı "+new_name+" olarak başarı ile değiştirildi", "info")
                                        break
                                    else:
                                        MS.create_frame("Modül Adı Değiştirme", ckey+" modülünün adı "+new_name+" olarak değiştirme işlemi iptal edildi!", "info")
                                else:
                                    MS.create_frame("Modül Adı Değiştirme", new_name+" adında bir modüz zaten mevcut!", "info")
                

                    if int(opt) == 2:
                        new_fonk = MS.create_frame("Modül Fonksiyonu Değiştirme", ckey+" adlı modül için yeni fonksiyon adı girin! Not: Modül adı ve fonksiyon adı aynı olamk zorundadır.", "")
                        warn = MS.create_frame("Modül Fonksiyonu Değiştirme", ckey+" modülünün "+cvalue+" fonksiyonunu "+new_fonk +" olarak değiştirmek üzeresiniz! Devam etmek istiyor musunuz?", "(E/H)")
                        if warn.lower() == "e":
                            menu_data[root][ckey] = new_fonk 
                            SettingsMenu.save_menu(menu_data)
                            MS.create_frame("Modül Fonksiyonu Değiştirme", ckey+" modülünün fonksiyonu "+new_fonk+" olarak başarı ile değiştirildi", "info")
                        else:
                            MS.create_frame("Modül Adı Değiştirme", ckey+" modülünün fonksiyonu "+new_fonk+" olarak değiştirme işlemi iptal edildi!", "info")

                    if int(opt) == 3:
                            while True:
                                new_name = MS.create_frame("Modül Adı Değiştirme", ckey+" adlı modül için yeni ad girin!", "")
                                if new_name not in menu_data[root]:
                                    new_fonk = MS.create_frame("Modül Fonksiyonu Değiştirme", ckey+" adlı modül için yeni fonksiyon adı girin! Not: Modül adı ve fonksiyon adı aynı olamk zorundadır.", "")
                                    warn = MS.create_frame("Modül Adı ve Fonksiyon Değiştirme", ckey+" modülünün adını "+new_name+" olarak ve "+cvalue+" fonksiyonunu "+new_fonk +" olarak değiştirmek üzeresiniz! Devam etmek istiyor musunuz?", "(E/H)")
                                    if warn.lower() == "e":
                                        menu_data[root][new_name] = menu_data[root][ckey]
                                        del menu_data[root][ckey]
                                        menu_data[root][new_name] = new_fonk
                                        SettingsMenu.save_menu(menu_data)
                                        MS.create_frame("Modül Adı Değiştirme", ckey+" modülünün adı "+new_name+" olarak başarı ile değiştirildi", "info")
                                        break
                                    else:
                                        MS.create_frame("Modül Adı Değiştirme", ckey+" modülünün adı "+new_name+" olarak değiştirme işlemi iptal edildi!", "info")
                                else:
                                    MS.create_frame("Modül Adı Değiştirme", new_name+" adında bir modüz zaten mevcut!", "info")
                else:
                    MS.create_frame("Modül Bulunamadı", str(ckey)+" adlı modül bulunamadı!", "info")

        elif operation == 1:
            while True:
                new_key  = MS.create_frame("Mevcut Modüller", "|"+"|   |".join(f"{i+1}. {item}" for i, item in enumerate(no_submenu_keys))+"|", "Yeni Menü Adını Giriniz")
                if new_key not in no_submenu_keys:
                    break
                else:
                    MS.create_frame("Bu Menü Mevcut", new_key+" adında bir modül zaten mevcut!", "info")
            new_value = MS.create_frame("Fonksiyon Adı", new_key+" adlı modül seçeneği için fonksiyon adı girin. Not: Modül adı ve fonksiyon adı aynı olamk zorundadır.", "")
            warn = MS.create_frame("Modül Ekleme", new_key+" adlı modülü "+new_value+" fonksiyonu ile eklemek üzeresiniz! Devam etmek istiyor musunuz?", "(E/H)")
            if warn.lower() == "e":
                menu_data[root][new_key] = new_value
                SettingsMenu.save_menu(menu_data)
                MS.create_frame("Modül Ekleme", new_key+" adlı modül "+new_value+" fonksiyonu ile eklendi.", "info")
            else:
                MS.create_frame("Modül Ekleme", new_key+" adlı modül "+new_value+" fonksiyonu ile ekleme işlemi iptal edildi.", "info")

    def save_menu(menu_data):
        config = MS.read_config()
        with open(config["menu_file"], 'w', encoding='utf-8') as file:
            json.dump(menu_data, file, indent=4, ensure_ascii=False)

    def profil(**kwargs):
        configs = MS.read_config()
        database_folder = configs.get("database_path")
        database_file = configs.get("users_db_file")
        database_path = os.path.join(database_folder, database_file)
        menu_file = configs.get("menu_file")
        menu_root = configs.get("menu_root")
        menu_data = MS.load_json(menu_file)
        root = list(menu_data.keys())[int(menu_root)]

        my_profil_data = list(kwargs.get("user_data"))
        profil_options = [f"İsim: {my_profil_data[4]}", f"Soyisim: {my_profil_data[5]}", f"Kullanıcı adı: {my_profil_data[1]}", "Şifre: ****", f"E-Posta: {my_profil_data[6]}", f"Telefon: {my_profil_data[7]}"]+["Ana Menü"]
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
        selection = int(MS.create_frame("Değiştirmek İstediğiniz Seçeneği Seçin", profil_options, "menu"))
        
        if selection == 0:
            ms = MS(menu_data[root], 0, [], None, None, None, None, **kwargs)
            ms.show_menu(root)

        if selection == 1:
            new_name = MS.create_frame("İsim Değiştirme", my_profil_data[4]+" ile değiştirilecek yeni isim giriniz.", "")
            if new_name:
                my_profil_data[4] = new_name
            are_u_sure=MS.create_frame("Kaydet", "Değişikliği Kaydetmek İstediğinize Emin misiniz?", "(E/H)\n")
            if are_u_sure.lower() == "e":
                SQL_ = SQL(database_path)
                SQL_.sql_update_user(my_profil_data[0], my_profil_data[1], my_profil_data[2], my_profil_data[3], my_profil_data[4], my_profil_data[5], my_profil_data[6], my_profil_data[7])
                MS.create_frame("Başarılı", "Değişiklik İşlemi Başarı ile Yapıldı", "info")
                kwargs["user_data"] = tuple(my_profil_data)
                ms = MS(menu_data[root], 0, [], None, None, None, None, **kwargs)
                ms.show_menu(root)
            else:
                MS.create_frame("İptal", "Değişiklik İşlemi İptal Edildi", "info")

        if selection == 2:
            new_name = MS.create_frame("Soysim Değiştirme", my_profil_data[5]+" ile değiştirilecek yeni soyisim giriniz.", "")
            if new_name:
                my_profil_data[5] = new_name
            are_u_sure=MS.create_frame("Kaydet", "Değişikliği Kaydetmek İstediğinize Emin misiniz?", "(E/H)\n")
            if are_u_sure.lower() == "e":
                SQL_ = SQL(database_path)
                SQL_.sql_update_user(my_profil_data[0], my_profil_data[1], my_profil_data[2], my_profil_data[3], my_profil_data[4], my_profil_data[5], my_profil_data[6], my_profil_data[7])
                MS.create_frame("Başarılı", "Değişiklik İşlemi Başarı ile Yapıldı", "info")
                kwargs["user_data"] = tuple(my_profil_data)
                ms = MS(menu_data[root], 0, [], None, None, None, None, **kwargs)
                ms.show_menu(root)
            else:
                MS.create_frame("İptal", "Değişiklik İşlemi İptal Edildi", "info")

        if selection == 3:
            while True:
                new_name = MS.create_frame("Kullanıcı Adı Değiştirme", my_profil_data[1]+" ile değiştirilecek yeni kullanıcı adı giriniz.", "")
                SQL_ = SQL(database_path)
                if SQL_.sql_read_users(new_name) == False:
                    if new_name:
                        my_profil_data[1] = new_name
                    are_u_sure=MS.create_frame("Kaydet", "Değişikliği Kaydetmek İstediğinize Emin misiniz?", "(E/H)\n")
                    if are_u_sure.lower() == "e":
                        SQL_ = SQL(database_path)
                        SQL_.sql_update_user(my_profil_data[0], my_profil_data[1], my_profil_data[2], my_profil_data[3], my_profil_data[4], my_profil_data[5], my_profil_data[6], my_profil_data[7])
                        MS.create_frame("Başarılı", "Değişiklik İşlemi Başarı ile Yapıldı", "info")
                        kwargs["user_data"] = tuple(my_profil_data)
                        ms = MS(menu_data[root], 0, [], None, None, None, None, **kwargs)
                        ms.show_menu(root)
                        break
                    else:
                        MS.create_frame("İptal", "Değişiklik İşlemi İptal Edildi", "info")
                    break
                else:
                    MS.create_frame("Kullanımda", new_name+" kullanıcı adı kullanılabilir değil. Lütfen farklı bir kullanıcı adı girin.", "info")

        if selection == 4:
            while True:
                print("Mevcut")
                cur_pass = SettingsMenu.get_pass(1)
                if SettingsMenu.hash_password_md5(cur_pass) == my_profil_data[2]:
                    print("Yeni")
                    new_pass = SettingsMenu.get_pass(1)
                    new_pass_valid, message = SettingsMenu.is_valid_password(new_pass)
                    if new_pass_valid == True:
                        new_pass2 = SettingsMenu.get_pass(2)
                        new_pass2_valid, message = SettingsMenu.is_valid_password(new_pass, new_pass2)
                        if new_pass2_valid == True:
                            are_u_sure=MS.create_frame("Kaydet", "Değişikliği Kaydetmek İstediğinize Emin misiniz?", "(E/H)\n")
                            if are_u_sure.lower() == "e":
                                my_profil_data[2] = SettingsMenu.hash_password_md5(new_pass)
                                SQL_ = SQL(database_path)
                                SQL_.sql_update_user(my_profil_data[0], my_profil_data[1], my_profil_data[2], my_profil_data[3], my_profil_data[4], my_profil_data[5], my_profil_data[6], my_profil_data[7])
                                MS.create_frame("Başarılı", "Değişiklik İşlemi Başarı ile Yapıldı", "info")
                                kwargs["user_data"] = tuple(my_profil_data)
                                ms = MS(menu_data[root], 0, [], None, None, None, None, **kwargs)
                                ms.show_menu(root)
                                break
                            else:
                                MS.create_frame("İptal", "Değişiklik İşlemi İptal Edildi", "info")
                            break
                        else:
                            MS.create_frame("Şifre Hatası", message, "info")
                    else:
                        MS.create_frame("Geçersiz Şifre", message, "info")
                else:
                    MS.create_frame("Hatalı Şifre", "Mevcut Şifreniz Hatalı. Lütfen Tekrar Deneyiniz.", "info")

        if selection == 5:
            while True:
                new_mail = MS.create_frame("E-posta Değiştirme", my_profil_data[6]+" ile değiştirilecek yeni e-postanızı giriniz.", "")
                mail_valid, message = SettingsMenu.is_valid_email(new_mail)
                if mail_valid == True:
                    if new_mail:
                        my_profil_data[6] = new_mail
                    are_u_sure=MS.create_frame("Kaydet", "Değişikliği Kaydetmek İstediğinize Emin misiniz?", "(E/H)\n")
                    if are_u_sure.lower() == "e":
                        SQL_ = SQL(database_path)
                        SQL_.sql_update_user(my_profil_data[0], my_profil_data[1], my_profil_data[2], my_profil_data[3], my_profil_data[4], my_profil_data[5], my_profil_data[6], my_profil_data[7])
                        MS.create_frame("Başarılı", "Değişiklik İşlemi Başarı ile Yapıldı", "info")
                        kwargs["user_data"] = tuple(my_profil_data)
                        ms = MS(menu_data[root], 0, [], None, None, None, None, **kwargs)
                        ms.show_menu(root)
                        break
                    else:
                        MS.create_frame("İptal", "Değişiklik İşlemi İptal Edildi", "info")
                    break
                else:
                    MS.create_frame("Geçersiz E-Posta", message, "info")

        if selection == 6:
            while True:
                new_tel = MS.create_frame("Telefon Değiştirme", my_profil_data[7]+" ile değiştirilecek yeni telefon numaranızı giriniz.", "")
                tel_valid, message = SettingsMenu.is_valid_phone_number(new_tel)
                if tel_valid == True:
                    if new_tel:
                        my_profil_data[7] = new_tel
                    are_u_sure=MS.create_frame("Kaydet", "Değişikliği Kaydetmek İstediğinize Emin misiniz?", "(E/H)\n")
                    if are_u_sure.lower() == "e":
                        SQL_ = SQL(database_path)
                        SQL_.sql_update_user(my_profil_data[0], my_profil_data[1], my_profil_data[2], my_profil_data[3], my_profil_data[4], my_profil_data[5], my_profil_data[6], my_profil_data[7])
                        MS.create_frame("Başarılı", "Değişiklik İşlemi Başarı ile Yapıldı", "info")
                        kwargs["user_data"] = tuple(my_profil_data)
                        ms = MS(menu_data[root], 0, [], None, None, None, None, **kwargs)
                        ms.show_menu(root)
                        break
                    else:
                        MS.create_frame("İptal", "Değişiklik İşlemi İptal Edildi", "info")
                    break
                else:
                    MS.create_frame("Geçersiz Telefon", message, "info")
                    

    def is_valid_password(password, password2=None):
        # Şifre en az 8 karakter olmalı
        if len(password) < 8:
            return False, "Şifre en az 8 karakter olmalıdır."

        # Şifre en az bir büyük harf, bir küçük harf ve bir rakam içermeli
        if not re.search(r"[A-Za-z]", password):
            return False, "Şifre en az bir harf içermelidir."
        if not re.search(r"[0-9]", password):
            return False, "Şifre en az bir rakam içermelidir."
        
        # Şifre en az bir özel karakter içermeli
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Şifre en az bir özel karakter içermelidir."
        
        if password2:
            if password != password2:
                return False, "Girilen şifreler birbiri ile uyuşmuyor"
    
        return True, "Şifre geçerli"
    
    def hash_password_md5(password: str) -> str:
        md5_hash = hashlib.md5(password.encode()).hexdigest()
        return md5_hash

    def is_valid_email(email):
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if not email:
            return False, "E-posta adresi boş bırakılamaz."

        if not re.match(email_regex, email):
            return False, "Geçersiz e-posta formatı!"

        return True, "Geçerli e-posta adresi."
    
    def get_pass(i):
        if i == 1:
            return getpass.getpass("Şifrenizi girin: ")
        if i == 2:
            return getpass.getpass("Şifrenizi tekar girin: ")
        
    def is_valid_phone_number(phone):
        phone_regex = r"^(?:\+90|0)?\s?5[0-9]{2}[\s-]?[0-9]{3}[\s-]?[0-9]{4}$"

        if not phone:
            return False, "Telefon numarası boş bırakılamaz."

        if not re.match(phone_regex, phone):
            return False, "Geçersiz telefon numarası formatı!"

        return True, "Geçerli telefon numarası."
    
    def is_username_valid(username):
        # Kullanıcı adı en az 3, en fazla 20 karakter olmalı
        if len(username) < 3 or len(username) > 20:
            return False, "Kullanıcı adı 3 ile 20 karakter arasında olmalıdır."

        # Kullanıcı adı sadece harf, rakam ve alt çizgi içerebilir
        if not re.match("^[A-Za-z0-9_]+$", username):
            return False, "Kullanıcı adı yalnızca harfler, rakamlar ve alt çizgi içerebilir."

        # Kullanıcı adı bir rakamla başlayamaz
        if username[0].isdigit():
            return False, "Kullanıcı adı bir rakamla başlayamaz."

        return True, "Kullanıcı adı geçerli"
    
    def users(**kwargs):
        configs = MS.read_config()
        database_folder = configs.get("database_path")
        database_file = configs.get("users_db_file")
        database_path = os.path.join(database_folder, database_file)
        menu_file = configs.get("menu_file")
        menu_root = configs.get("menu_root")
        menu_data = MS.load_json(menu_file)
        root = list(menu_data.keys())[int(menu_root)]
        # my_profil_data = list(kwargs.get("user_data"))
        # c_user_role= my_profil_data[3]


        # Veritabanına bağlan
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Tüm kullanıcıları getir
        cursor.execute("SELECT * FROM users;")
        users_data = cursor.fetchall()

        user_list_data = []
        [user_list_data.append(list(line)) for line in users_data]

        user_list = []
        for user in user_list_data:
            user_list.append("Kullanıcı Adı: "+user[1]+" - Ad-Soyad: "+user[4]+" "+user[5]+" - E-Posta: "+user[6]+" - Tel: "+user[7])

        conn.close()

        user_list = user_list + ["####### Yeni Kullanıcı Ekle #######"] + ["#######    Kullanıcı Sil    #######"] + ["Ana Menü"]
        selection = int(MS.create_frame("Kullanıcı Listesi", user_list, "menu"))

        if selection == len(user_list_data) + 1:
            first_init=None
            if kwargs.get("user_data"):
                my_profil_data = list(kwargs.get("user_data"))
                c_user_role= my_profil_data[3]
            while True:
                username = MS.create_frame("Kullanıcı Oluştur", "Lüten bir kullanıcı adı belirleyin.", "Kullanıcı adı: ")
                user_name_validation, user_name_validation_message = SettingsMenu.is_username_valid(username)
                if user_name_validation == True:
                    SQL_ = SQL(database_path)
                    existing_user = SQL_.sql_read_users(username)
                    if existing_user != False:
                        MS.create_frame("Kullanıcı Mevcut", username+" adlı kullanıcı mevcut. Lüten farklı bir kullanıcı adı belirleyin.", "info")
                    else:
                        while True:  
                            password = SettingsMenu.get_pass(1)
                            password_validation, password_validation_message = SettingsMenu.is_valid_password(password)
                            if password_validation == True:

                                while True:
                                    password2 = SettingsMenu.get_pass(2)
                                    password_validation, password_validation_message = SettingsMenu.is_valid_password(password, password2)
                                    if password_validation == True:
                                        while True:
                                            name = MS.create_frame("Kullanıcı Oluştur", "Lüten adınızı giriniz", "Adınız: ")
                                            if name != "" or name != None:
                                                while True:
                                                    surname = MS.create_frame("Kullanıcı Oluştur", "Lüten soyadınızı giriniz", "Soyadınız: ")
                                                    if surname != "" or surname != None:
                                                        while True:
                                                            email = MS.create_frame("Kullanıcı Oluştur", "Lüten e-posta adresinizi giriniz", "E-Posta adresiniz: ")
                                                            email_validation, email_validation_message  = SettingsMenu.is_valid_email(email)
                                                            if email_validation == True:
                                                                while True:
                                                                    tel = MS.create_frame("Kullanıcı Oluştur", "Lüten telefon numaranızı giriniz", "Telefon numaranız: ")
                                                                    tel_validation, tel_validation_message = SettingsMenu.is_valid_phone_number(tel)
                                                                    if tel_validation == True:
                                                                        if first_init:
                                                                            role = 0
                                                                        elif c_user_role == 0:
                                                                            role = int(MS.create_frame("Kullanıcı Oluştur", "Kullanıcı Rolü Giriniz (0 - 1)", "Rol değeri: "))
                                                                        else:
                                                                            role = 1
                                                                        SQL_ = SQL(database_path)
                                                                        SQL_.sql_add_user2(username, SettingsMenu.hash_password_md5(password), role, name, surname, email, tel)
                                                                        SQL_.conncls()
                                                                        break
                                                                    else:
                                                                        MS.create_frame("Telefon Numarası Hatası", tel_validation_message, "info")
                                                                break
                                                            else:
                                                                MS.create_frame("E-Posta Hatası", email_validation_message, "info")
                                                        break
                                                    else:
                                                        MS.create_frame("İsim Hatası", "Soyad boş bırakılamaz", "info")
                                                break
                                            else:
                                                MS.create_frame("İsim Hatası", "Ad boş bırakılamaz", "info")
                                        break
                                    else:
                                        MS.create_frame("Şifre Hatası", password_validation_message, "info")
                                break
                            else:
                                MS.create_frame("Şifre Hatası", password_validation_message, "info")
                    break   
                else:
                    MS.create_frame("Kullanıcı Adı Hatası", user_name_validation_message, "info")
        
        os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
        selection = int(MS.create_frame("Kullanıcı Listesi", user_list, "menu"))
        
        if selection == 0:
            ms = MS(menu_data[root], 0, [], None, None, None, None, **kwargs)
            ms.show_menu(root)


        
       

