import os
from application.modul_olusturucu import ModuleLoader
from application.ekran_olustur import ScreenView as SV
from application.default_menu import DefaultMenu

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
            options = list(current_menu.keys())
            
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
                        module_path = "application"
                        module_name = "settings"
                        class_name = "SettingsMenu"
                        func_name = "menu_goster"
                        self.kwargs.update({"selected_key": choice})

                        # call_function(Modül Klasörü, Modül Adı, Sınıf Adı, Init Data, Fonksiyon Adı, Fonksiyon Argümanları **kwargs)
                        run_module = ModuleLoader.call_function(module_path, module_name, class_name, None, func_name, **self.kwargs)
                        self.module_name = None #############################
                        self.func_name = None #############################

                    elif not self.path and choice == len(options) - len(options):  # "Çıkış" seçildi
                        # User.wellcome(**kwargs)
                        print("Çıkış yapılıyor...")
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

                            #call_function(Modül Klasörü, Modül Adı, Sınıf Adı, Init Data, Fonksiyon Adı, Fonksiyon Argümanları **kwargs)
                            run_module = ModuleLoader.call_function(self.module_path, self.module_name, self.class_name, self.init_data, self.func_name, **self.kwargs)
                            self.module_name = None #############################
                            self.func_name = None #############################
                            

                            if run_module == None:
                                SV.create_frame("Modül: "+selected_key,selected_key+" modül uygulaması sona erdi.")
                                MenuSystem.main_menu(self)
                            else:
                                SV.create_frame("Modül: "+selected_key,run_module)
                                MenuSystem.main_menu(self)
                else:
                    if self.path and choice == len(options) - len(options):  
                        # "Geri Dön" seçildi
                        # self.path.pop()
                        MenuSystem.main_menu(self)
                    elif not self.path and choice == len(options) - len(options):  
                        # "Çıkış" seçildi
                        # config = ModuleLoader.read_config()                                     # Ayarları oku
                        # menu_data = SV.load_json(config["menu_file"])                           # Menü verilerini yükle
                        # root = list(menu_data.keys())[int(config.get("menu_root"))]
                        # module_path = "application"
                        # module_name = "menu_olusturucu"
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

                            #call_function(Modül Klasörü, Modül Adı, Sınıf Adı, Init Data, Fonksiyon Adı, Fonksiyon Argümanları **kwargs)
                            run_module = ModuleLoader.call_function(self.module_path, self.module_name, self.class_name, self.init_data, self.func_name, **self.kwargs)
                            
                            self.module_name = None #############################
                            self.func_name = None #############################
                            
                            
                            # input(self.kwargs)
                            if run_module == None:
                                SV.create_frame("Modül: "+selected_key,selected_key+" modül uygulaması sona erdi.")
                                MenuSystem.main_menu(self)
                            else:
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
    