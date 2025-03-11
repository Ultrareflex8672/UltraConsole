import os
from application.modul_olusturucu import ModuleLoader
# from application.ekran_olustur import ScreenView as SV
from application.default_menu import DefaultMenu
from application.settings import SettingsMenu as SV
from application.settings import SettingsMenu
from application.log import log_ekle as LOG

class MenuSystem(ModuleLoader,SV,DefaultMenu):
    def __init__(self, menu_data_, type_=0, module_path_=[], module_name_=None, class_name_=None, init_data_=None, func_name_=None, **kwargs):
        self.menu_data = menu_data_
        self.type = type_
        self.module_path = module_path_
        self.module_name = module_name_
        self.class_name = class_name_
        self.init_data = init_data_
        self.func_name = func_name_
        self.kwargs = {}
        self.kwargs.update(kwargs)
        self.path = []  # Kullanıcının bulunduğu menü yolu

    def show_menu(self, title="Başlıksız Menü", **kwargs):
        if kwargs:
            title = kwargs.get("root", 0)
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle

            current_menu = self.menu_data # Kullanıcının bulunduğu menüyü al
            
            for key in self.path: # Menü yolu üzerinde ilerle
                current_menu = current_menu[key] # Alt menüye geç

            # Menü başlığını göster
            menu_title = " > ".join(self.path) if self.path else title

            # Seçenekleri listele
            if self.kwargs.get("module_path"):
                static_modul_path = self.kwargs.get("module_path")
            else:
                additional_configs = MenuSystem.read_config()
                static_modul_path = additional_configs.get("module_path")
            
            if os.path.isdir(static_modul_path):
                module_files = [f[:-3] for f in os.listdir(static_modul_path) if f.endswith(".py")]
            else:
                module_files = []
                SV.create_frame("Modül Hatası", static_modul_path+" adlı dizin bulunamadı! Lütfen uygulama ayarlarından 'module_path' yolunun doğru girildiğinden emin olun yada modüllerinizi "+static_modul_path+" klasörüne taşıyın!", "info")
                os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle

            options = []
            for key, value in self.menu_data.items():
                if isinstance(value, dict):  # Eğer value bir dict ise, key options listesine eklenir
                    options.append(key)
                else:  # Eğer value dict değilse (yani son seviyede ise)
                    if value in module_files:
                        options.append(key)  # module_files içinde varsa key eklenir
                    else:
                        SV.create_frame(f"{key} Modülü Hatası", f"Uyarı: {key} adlı modül için ({value}.py) dosyası {static_modul_path} klasöründe mevcut değil. Lütfen ayarlardan gerekli düzenlemeyi yapın yada {static_modul_path} klasörüne ({value}.py) dosyasını ekleyin!", "info")
                        os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle

            # options = []
            # for key, value in self.menu_data.items():
            #     if value in module_files:
            #         options.append(key)
            #     else:
            #         SV.create_frame(f"{key} Modülü Hatası", f"Uyarı: {key} adlı modül için ({value}.py) dosyası {static_modul_path} klasöründe mevcut değil. Lütfen ayarlardan gerekli düzenlemeyi yapın yada {static_modul_path} klasörüne ({value}.py) dosyasını ekleyin!", "info")
            #         os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle

            
            
            
            # options = list(current_menu.keys())
            
            if self.type == 1:  # Eğer modül çağrısı yapıldıysa geri dön seçeneği ekle
                options.append("Ana Menü")
            else:  # Modül çağrısı yapılmadıysa
                if self.path:  # Eğer ana menüde değilsek "Geri Dön" seçeneği koy
                    options.append("Geri Dön")
                else:  # Ana menüdeysek "Ayarlar" ve "Çıkış" seçenekleri ekle
                    options.append("Ayarlar")
                    options.append("Çıkış")

            # choice = input("Seçiminizi yapın: ")
            choice = SV.create_frame(menu_title, options, "menu")

            try:
                choice = int(choice)
                if self.type != 1:
                    if self.path and choice == len(options) - len(options):  # "Geri Dön" seçildi
                        # self.path.pop()
                        MenuSystem.main_menu(self)
                    elif self.path == [] and choice == len(options) - 1:  
                        # "Ayarlar" seçildi
                        print("Ayarlar açılıyor...")

                        # setting_menu_data = {
                        #     "Ayarlar": {
                        #                 "Ayarları Görüntüle": "settings",
                        #                 "Ayarları Değiştir": "settings",
                        #                 "Modül İşlemleri": "settings",
                        #                 "Profilim": "settings",
                        #                 "Kullanıcılar": "settings"
                        #                 }
                        #                     }

                        setting_menu_data = ["Ayarları Görüntüle", "Ayarları Değiştir", "Modül İşlemleri", "Profilim", "Kullanıcılar", "UC Hakkında"]+["Ana Menü"]
                        os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
                        setting_selection = int(SV.create_frame("Ayarlar", setting_menu_data, "menu"))
                        self.kwargs.update({"selected_key": setting_selection})
                        if setting_selection != 0:
                            my_profil_data = self.kwargs.get("user_data")
                            LOG(f"{my_profil_data[0]} ID numaralı {my_profil_data[1]} ({my_profil_data[4]} {my_profil_data[5]}) ayarlar menüsüne girdi.")
                            SettingsMenu().settings(**self.kwargs)
                            MenuSystem.main_menu(self)
                        

                        # module_path = "application"
                        # module_name = "settings"
                        # class_name = "SettingsMenu"
                        # func_name = "menu_goster"
                        

                        # # call_function(Modül Klasörü, Modül Adı, Sınıf Adı, Init Data, Fonksiyon Adı, Fonksiyon Argümanları **kwargs)
                        # run_module = ModuleLoader.call_function(module_path, module_name, class_name, None, func_name, **self.kwargs)
                        # self.module_name = None #############################
                        # self.func_name = None #############################

                    elif not self.path and choice == len(options) - len(options):  # "Çıkış" seçildi
                        # User.wellcome(**kwargs)
                        print("Çıkış yapılıyor...")
                        my_profil_data = self.kwargs.get("user_data")
                        LOG(f"{my_profil_data[0]} ID numaralı {my_profil_data[1]} ({my_profil_data[4]} {my_profil_data[5]}) UltraConsole 'u sonlandırdı.")
                        exit()
                    else:
                        selected_key = options[choice - 1]
                        if isinstance(current_menu[selected_key], dict):  # Alt menü varsa
                            self.path.append(selected_key)
                        else:  
                            # Alt menü yoksa, ilgili fonksiyonu modül klasöründen çağır
                            print(f"{selected_key} fonksiyonu çağırılıyor...")
                            if self.module_name == None:
                                self.module_name = current_menu[selected_key]
                            if self.func_name == None:
                                self.func_name = current_menu[selected_key]
                            self.kwargs["selected_key"] = choice
                            self.kwargs["selected_name"] = selected_key
                            self.kwargs["menu_type"] = self.type

                            my_profil_data = self.kwargs.get("user_data")
                            LOG(f"{my_profil_data[0]} ID numaralı {my_profil_data[1]} ({my_profil_data[4]} {my_profil_data[5]}) {selected_key} modülünü çalıştırdı.")

                            #call_function(Modül Klasörü, Modül Adı, Sınıf Adı, Init Data, Fonksiyon Adı, Fonksiyon Argümanları **kwargs)
                            run_module = ModuleLoader.call_function(self.module_path, self.module_name, self.class_name, self.init_data, self.func_name, **self.kwargs)
                            self.module_name = None #############################
                            self.func_name = None #############################
                            

                            if run_module == None:
                                LOG(f"{my_profil_data[0]} ID numaralı {my_profil_data[1]} ({my_profil_data[4]} {my_profil_data[5]}) {selected_key} modülünden ayrıldı.")
                                SV.create_frame("Modül: "+selected_key,selected_key+" modül uygulaması sona erdi.")
                                MenuSystem.main_menu(self)
                            else:
                                LOG(f"{my_profil_data[0]} ID numaralı {my_profil_data[1]} ({my_profil_data[4]} {my_profil_data[5]}) {selected_key} modülünden ayrıldı.")
                                SV.create_frame("Modül: "+selected_key,run_module)
                                MenuSystem.main_menu(self)
                else:
                    if self.path and choice == len(options) - len(options):  
                        # "Geri Dön" seçildi
                        # self.path.pop()
                        my_profil_data = self.kwargs.get("user_data")
                        LOG(f"{my_profil_data[0]} ID numaralı {my_profil_data[1]} ({my_profil_data[4]} {my_profil_data[5]}) ana menüye döndü.")
                        MenuSystem.main_menu(self)
                    elif not self.path and choice == len(options) - len(options):  
                        # "Çıkış" seçildi
                        # config = ModuleLoader.read_config()                                     # Ayarları oku
                        # menu_data = SV.load_json(config["menu_file"])                           # Menü verilerini yükle
                        # root = list(menu_data.keys())[int(config.get("menu_root"))]
                        # module_path = "application"
                        # module_name = "menu_olusturucu"
                        my_profil_data = self.kwargs.get("user_data")
                        LOG(f"{my_profil_data[0]} ID numaralı {my_profil_data[1]} ({my_profil_data[4]} {my_profil_data[5]}) ana menüye döndü.")
                        MenuSystem.main_menu(self)

                        #call_function(Modül Klasörü, Modül Adı, Sınıf Adı, Init Data, Fonksiyon Adı, Fonksiyon Argümanları **kwargs)
                        # ModuleLoader.call_function(module_path, module_name, "MenuSystem", menu_data[root], "show_menu", root=root, **self.kwargs)
                        # self.module_name = None #############################
                        # self.func_name = None #############################
                        # MenuSystem.main_menu(self)

                    else:
                        selected_key = options[choice - 1]
                        if isinstance(current_menu[selected_key], dict):  # Alt menü varsa
                            self.path.append(selected_key)
                        else:  
                            # Alt menü yoksa, ilgili fonksiyonu modül klasöründen çağır
                            print(f"{selected_key} fonksiyonu çağırılıyor...")
                            if self.module_name == None:
                                self.module_name = current_menu[selected_key]
                            if self.func_name == None:
                                self.func_name = current_menu[selected_key]
                            self.kwargs["selected_key"] = choice
                            self.kwargs["selected_name"] = selected_key
                            self.kwargs["menu_type"] = self.type

                            my_profil_data = self.kwargs.get("user_data")
                            LOG(f"{my_profil_data[0]} ID numaralı {my_profil_data[1]} ({my_profil_data[4]} {my_profil_data[5]}) {selected_key} modülünü çalıştırdı.")

                            #call_function(Modül Klasörü, Modül Adı, Sınıf Adı, Init Data, Fonksiyon Adı, Fonksiyon Argümanları **kwargs)
                            run_module = ModuleLoader.call_function(self.module_path, self.module_name, self.class_name, self.init_data, self.func_name, **self.kwargs)
                            
                            self.module_name = None #############################
                            self.func_name = None #############################
                            
                            if run_module == None:
                                LOG(f"{my_profil_data[0]} ID numaralı {my_profil_data[1]} ({my_profil_data[4]} {my_profil_data[5]}) {selected_key} modülünden ayrıldı.")
                                SV.create_frame("Modül: "+selected_key,selected_key+" modül uygulaması sona erdi.")
                                MenuSystem.main_menu(self)
                            else:
                                LOG(f"{my_profil_data[0]} ID numaralı {my_profil_data[1]} ({my_profil_data[4]} {my_profil_data[5]}) {selected_key} modülünden ayrıldı.")
                                SV.create_frame("Modül: "+selected_key,run_module)
                                MenuSystem.main_menu(self)
            except (ValueError, IndexError):
                    print("Geçersiz seçim, tekrar deneyin.")
                    
    def main_menu(self):
        configs = MenuSystem.read_config()
        menu_file = configs.get("menu_file")
        menu_root = configs.get("menu_root")
        module_path = configs.get("module_path")
        menu_data = MenuSystem.load_json(menu_file)
        root_key = list(menu_data.keys())[int(menu_root)]

        ms = MenuSystem(menu_data[root_key], **self.kwargs)  
        # input(self.kwargs))
        ms.show_menu(root_key)
    