from config_menu import menus
from hesap_makinesi import HesapMakinesi

class Menu(HesapMakinesi):
    def __init__(self):
        pass

    def draw_menu(self, menu_name):
        menu_text = menus.get(menu_name, ["Geçersiz Menü"])
        width = max(len(line) for line in menu_text) + 4
        horizontal_border = "─" * width

        print("┌" + horizontal_border + "┐")
        for line in menu_text:
            print(f"│ {line.ljust(width - 2)} │")
        print("└" + horizontal_border + "┘")

    def get_selection(self):
        return input("Seçiminiz: ")

    def run(self, menu_name):
        while True:
            self.draw_menu(menu_name)
            secim = self.get_selection()

            
            if menu_name == "ana_menu":
                if secim == "2":
                    self.run("oyunlar")
                elif secim == "1":
                    self.run("hesap_makinesi")
                elif secim.lower() == "q":
                    print("Çıkış yapılıyor...")
                    break
            elif menu_name == "hesap_makinesi":
                if secim != "8":
                    print("İşlem Sonucunuz: " + HesapMakinesi().hesap_islemi(int(secim)) +  "\n")
                if secim == "8":
                    print("Ana menüye dönülüyor...\n")
                    break
            elif menu_name == "oyunlar":
                if secim == "4":
                    print("Ana menüye dönülüyor...\n")
                    break
            else:
                print(f"Seçiminiz: {secim}, işlem gerçekleştiriliyor...\n")
