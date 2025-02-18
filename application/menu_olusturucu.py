import os
from application.modul_olusturucu import ModuleLoader
from application.ekran_olustur import ScreenView as SV

class MenuSystem(ModuleLoader,SV):
    def __init__(self, menu_data):
        self.menu_data = menu_data
        self.path = []  # Kullanıcının bulunduğu menü yolu

    def show_menu(self, title="Başlıksız Menü"):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle

            current_menu = self.menu_data # Kullanıcının bulunduğu menüyü al
            for key in self.path: # Menü yolu üzerinde ilerle
                current_menu = current_menu[key] # Alt menüye geç

            # Menü başlığını göster
            menu_title = " > ".join(self.path) if self.path else title
            # print(f"\n=== {menu_title} ===")

            # Seçenekleri listele
            options = list(current_menu.keys())

            # for i, key in enumerate(options, 1):
            #     print(f"{i}. {key}")

            if self.path:  # Eğer ana menüde değilsek "Geri Dön" seçeneği koy
                # print(f"{len(options) + 1}. Geri Dön")
                options.append("Geri Dön")
            else:  # Ana menüdeysek "Ayarlar" ve "Çıkış" seçenekleri ekle
                options.append("Ayarlar")
                options.append("Çıkış")
                # print(f"{len(options) + 1}. Ayarlar")
                # print(f"{len(options) + 2}. Çıkış")

            # choice = input("Seçiminizi yapın: ")
            choice = SV.create_frame(menu_title, options, "menu")

            try:
                choice = int(choice)
                if self.path and choice == len(options) - len(options):  # "Geri Dön" seçildi
                    self.path.pop()
                elif not self.path and choice == len(options) + 1:  # "Ayarlar" seçildi
                    print("Ayarlar açılıyor...")
                elif not self.path and choice == len(options) - len(options):  # "Çıkış" seçildi
                    print("Çıkış yapılıyor...")
                    exit()
                else:
                    selected_key = options[choice - 1]
                    if isinstance(current_menu[selected_key], dict):  # Alt menü varsa
                        self.path.append(selected_key)
                    else:  # Alt menü yoksa, ilgili fonksiyonu modül klasöründen çağır
                        print(f"{selected_key} fonksiyonu çağırılıyor...")
                        run_module = ModuleLoader.call_function(current_menu[selected_key], choice)
                        if run_module == None:
                            SV.create_frame("Modül: "+selected_key,selected_key+" modül uygulaması sona erdi.")
                        else:
                            SV.create_frame("Modül: "+selected_key,run_module)
                        # print(ModuleLoader.call_function(current_menu[selected_key], choice))
                        # input()
            except (ValueError, IndexError):
                print("Geçersiz seçim, tekrar deneyin.")
    