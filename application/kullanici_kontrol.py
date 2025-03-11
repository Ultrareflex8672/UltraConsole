from application.ultraconsole import UltraConsole as UC
from application.sql_islem import SqlProcess as SQL
from application.updater import Updater
from application.log import log_ekle as LOG
import os
import re
import hashlib
import sys

class User(UC, SQL):
    def __init__(self, logedin=None, user_data=None):
        self.configs = UC.read_config()
        self.database_folder = self.configs.get("database_path")
        self.database_file = self.configs.get("users_db_file")

        self.logedin = logedin
        self.user_data = user_data

        # Dosya yolu belirleme
        self.database_path = os.path.join(self.database_folder, self.database_file)
                                    
        # Klasör yoksa oluştur
        if not os.path.exists(self.database_folder):
            os.makedirs(self.database_folder)
            LOG(f"{self.database_folder} klasörü oluşturuldu.")
        if not os.path.exists(self.database_path):
            open(self.database_path, 'w').close()  # Boş dosya oluştur
            LOG(f"{self.database_file} veri tabanı oluşturuldu.")

        SQL_ = SQL(self.database_path)
        setup = False

        is_table_exist = SQL_.is_user_table_exist("users")
        # SQL_.conncls()
        if is_table_exist == True:
            is_user_exist = SQL_.sql_read_users()
            # SQL_.conncls()
            if is_user_exist != False:
                while True:
                    if self.logedin == True and self.user_data != None:
                        SQL_.conncls()
                        UC.create_frame("GİRİŞ BAŞARILI", "Hoşgeldin "+self.user_data[4]+", ana menüye yönlendiriliyorsunuz.", "info")
                        UC.go_main_menu(user_data=self.user_data)
                        break
                    else:
                        SQL_.conncls()
                        # User.add_user(self, first_init="yes")
                        # User.login(self)
                        User.wellcome(self)
            else:
                setup = True
        else:
            setup = True

        if setup == True:
            LOG("UltraConsole ilk başlatma protokolü...")
            UC.create_frame("UltraConsole 'a Hoş Geldiniz.", "UltraConsole sisteminde kayıtlı kullanıcı bulunmuyor. Kuruluma yönlendiriliyorsunuz...", "info")
            User.add_user(self, first_init="yes")
            UC.create_frame("UltraConsole", "Kurulum tamamlandı. Not: Tekrar ana kullanıcı ayarlamak için "+self.database_folder+" klasörünü ve "+self.database_file+" dosyasını silin.", "info")
            # UC.go_main_menu(user_data=self.user_data)
            # User.login(self)
            LOG("UltraConsole kurulumu tamamlandı.")
            User.wellcome(self)

    def add_user(self, first_init=None, **kwargs):
        if kwargs.get("user_role"):
            c_user_role= int(kwargs.get("user_role"))
        else:
            c_user_role= 1
        while True:
            username = UC.create_frame("Kullanıcı Oluştur", "Lüten bir kullanıcı adı belirleyin.", "Kullanıcı adı: ")
            user_name_validation, user_name_validation_message = User.is_username_valid(self, username)
            if user_name_validation == True:
                SQL_ = SQL(self.database_path)
                if first_init:
                    existing_user = None
                else:
                    existing_user = SQL_.sql_read_users(username)
                if existing_user:
                    UC.create_frame("Kullanıcı Mevcut", username+" adlı kullanıcı mevcut. Lüten farklı bir kullanıcı adı belirleyin.", "info")
                else:

                    while True:  
                        password = UC.get_pass(1)
                        password_validation, password_validation_message = User.is_valid_password(password)
                        if password_validation == True:
                        # while True:
                            password2 = UC.get_pass(2)
                            password_validation, password_validation_message = User.is_valid_password(password, password2)
                            if password_validation == True:
                                while True:
                                    name = UC.create_frame("Kullanıcı Oluştur", "Lüten adınızı giriniz", "Adınız: ")
                                    if name != "" or name != None:
                                        while True:
                                            surname = UC.create_frame("Kullanıcı Oluştur", "Lüten soyadınızı giriniz", "Soyadınız: ")
                                            if surname != "" or surname != None:
                                                while True:
                                                    email = UC.create_frame("Kullanıcı Oluştur", "Lüten e-posta adresinizi giriniz", "E-Posta adresiniz: ")
                                                    email_validation, email_validation_message  = User.is_valid_email(email)
                                                    if email_validation == True:
                                                        while True:
                                                            tel = UC.create_frame("Kullanıcı Oluştur", "Lüten telefon numaranızı giriniz", "Telefon numaranız: ")
                                                            tel_validation, tel_validation_message = User.is_valid_phone_number(tel)
                                                            if tel_validation == True:
                                                                if first_init:
                                                                    role = 0
                                                                elif c_user_role == 0:
                                                                    role = int(UC.create_frame("Kullanıcı Oluştur", "Kullanıcı Rolü Giriniz (0 - 1)", "Rol değeri: "))
                                                                else:
                                                                    role = 1
                                                                SQL_ = SQL(self.database_path)
                                                                SQL_.sql_add_user(username, User.hash_password_md5(password), role, name, surname, email, tel)
                                                                SQL_.conncls()
                                                                if role == 0:
                                                                    UC.create_frame("Yönetici Oluşturuldu", username+" adlı yönetici başarı ile oluşturuldu.", "info")
                                                                    LOG(f"{username} adlı yönetici oluşturuldu.")
                                                                if role == 1:
                                                                    UC.create_frame("Kullanıcı Oluşturuldu", username+" adlı kullanıcı başarı ile oluşturuldu.", "info")
                                                                    LOG(f"{username} adlı kullanıcı oluşturuldu.")
                                                                break
                                                            else:
                                                                UC.create_frame("Telefon Numarası Hatası", tel_validation_message, "info")
                                                        break
                                                    else:
                                                        UC.create_frame("E-Posta Hatası", email_validation_message, "info")
                                                break
                                            else:
                                                UC.create_frame("İsim Hatası", "Soyad boş bırakılamaz", "info")
                                        break
                                    else:
                                        UC.create_frame("İsim Hatası", "Ad boş bırakılamaz", "info")
                                break
                            else:
                                UC.create_frame("Şifre Hatası", password_validation_message, "info")

                                    
                            # break
                        else:
                            UC.create_frame("Şifre Hatası", password_validation_message, "info")
                break   
            else:
                UC.create_frame("Kullanıcı Adı Hatası", user_name_validation_message, "info")

    def is_username_valid(self, username):
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
    
    def is_valid_password(password, password2=None):
        # Şifre en az 8 karakter olmalı
        if len(password) < 8:
            return False, "Şifre en az 8 karakter olmalı, en az bir harf içermeli, en az bir rakam içermeli ve en az bir özel karakter içermelidir."

        # Şifre en az bir büyük harf, bir küçük harf ve bir rakam içermeli
        if not re.search(r"[A-Za-z]", password):
            return False, "Şifre en az 8 karakter olmalı, en az bir harf içermeli, en az bir rakam içermeli ve en az bir özel karakter içermelidir."
        if not re.search(r"[0-9]", password):
            return False, "Şifre en az 8 karakter olmalı, en az bir harf içermeli, en az bir rakam içermeli ve en az bir özel karakter içermelidir."
        
        # Şifre en az bir özel karakter içermeli
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Şifre en az 8 karakter olmalı, en az bir harf içermeli, en az bir rakam içermeli ve en az bir özel karakter içermelidir."
        
        if password2:
            if password != password2:
                return False, "Girilen şifreler birbiri ile uyuşmuyor"
    
        return True, "Şifre geçerli"
    
    def is_valid_email(email):
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if not email:
            return False, "E-posta adresi boş bırakılamaz."

        if not re.match(email_regex, email):
            return False, "Geçersiz e-posta formatı!"

        return True, "Geçerli e-posta adresi."
    
    def is_valid_phone_number(phone):
        phone_regex = r"^(?:\+90|0)?\s?5[0-9]{2}[\s-]?[0-9]{3}[\s-]?[0-9]{4}$"

        if not phone:
            return False, "Telefon numarası boş bırakılamaz."

        if not re.match(phone_regex, phone):
            return False, "Geçersiz telefon numarası formatı!"

        return True, "Geçerli telefon numarası."
    
    def login(self):
        logedin = False
        while logedin == False:
            username = User.create_frame("Kullanıcı Girişi","Giriş Yapmak için lütfen kullanıcı adınızı ve şifrenizi girin.", "Kullanıcı adınız: ")
            password = User.get_pass(1)
            SQL_ = SQL(self.database_path)
            user_data = SQL_.sql_read_users(username)
            SQL_.conncls()
            if user_data == False:
                UC.create_frame("GİRİŞ BAŞARISIZ", "Hatalı Kullanıcı Adı ve/veya Şifre", "info")
                LOG(f"{username} kullanıcı adı ile başarısız giriş denemesi.")
            else:
                user_password = user_data[2]
                password = User.hash_password_md5(password)
                if user_password == password:
                    logedin = True
                    LOG(f"{user_data[0]} ID numaralı {user_data[1]} ({user_data[4]} {user_data[5]}) giriş yaptı.")
                    User(logedin, user_data)
                    return logedin, user_data
                else:
                    UC.create_frame("GİRİŞ BAŞARISIZ", "Hatalı Kullanıcı Adı ve/veya Şifre", "info")
                    LOG(f"{username} kullanıcı adı ile hatalı parola girişi nedeni ile başarısız giriş denemesi.")
                



    def hash_password_md5(password: str) -> str:
        md5_hash = hashlib.md5(password.encode()).hexdigest()
        return md5_hash
    
    def wellcome(self, **kwargs):
        updater = Updater()
        
        new_version, current_version = updater.version()
        str_new_version = ".".join(str(new_version))
        str_current_version =".".join(str(current_version))
        if new_version > current_version:
            LOG(f"{new_version} numarlı yeni versiyon güncellemesi bulundu.")
            do_u_want_update = UC.create_frame("Güncelleme Mevcut", "UltraConsole 'un V"+str_new_version+" versiyonu şuanda kullanılabilir. Şuanki sürümünüz: V"+str_current_version+"   Şimdi güncellemek ister misiniz?", "(E/H)")
            if do_u_want_update.lower() == "e":
                LOG(f"Otomatik güncelleştirme başlatıldı.")
                updater.update()

        reset_explain = "Tekrar ana kullanıcı ayarlamak için '"+self.database_folder+"' klasörünü ve '"+self.database_file+"' dosyasını silin. Uygulamayı yeniden başlatın. Not: Bu işlem uygulama ayarlarını sıfırlamaz ancak uygulamadaki tüm kullanıcıları da silecektir. Eğer yönetici olarak giriş yapmak ile ilgili sorun yaşıyprsanız önce sistem yöneeticinize başvurmanız önerilir."
        
        if self.logedin == False or self.logedin == None:
            if self.user_data == None:
                os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
                LOG("UltraConsole başlatıldı.")
                selection = UC.create_frame(f"UltraConsole 'a Hoş Geldiniz... (V{str_current_version})", ["Giriş Yap", "Hesap Oluştur", "Kullanıcı Sıfırlama", "Çıkış"], "menu")
                
                try:
                    selection = int(selection)
                except:
                    UC.create_frame("UltraConsole", "0 - 3 arasında bir seçim yapınız", "info")

                if selection == 1:
                    User.login(self)
                elif selection == 2:
                    User.add_user(self, first_init=None, **kwargs)
                elif selection == 3:
                    UC.create_frame("UltraConsole", reset_explain, "info")
                elif selection == 0:
                    LOG("UltraConsole sonlandırıldı.")
                    print("Çıkış yapılıyor...")
                    sys.exit()
                else:
                    UC.create_frame("UltraConsole", "0 - 3 arasında bir seçim yapınız", "info")
                
        return

                    
        
