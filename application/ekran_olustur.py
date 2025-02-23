from application.ayar_okuyucu import ConfigHandler as CH
import textwrap
import os
import msvcrt

class ScreenView(CH):
    @staticmethod
    def colored_text(text, color_code):
        return f"\033[{color_code}m{text}\033[0m"

    @staticmethod
    def create_frame(title, content, type="info"):
        menu_min_width = CH.read_config()["menu_min_screen_width"]
        menu_max_width = CH.read_config()["menu_max_screen_width"]
        menu_title_color = CH.read_config()["menu_title_color"]
        menu_content_color = CH.read_config()["menu_content_color"]
        menu_frame_color = CH.read_config()["menu_frame_color"]
        info_title_color = CH.read_config()["info_title_color"]
        info_content_color = CH.read_config()["info_content_color"]
        info_frame_color = CH.read_config()["info_frame_color"]
        info_min_width = CH.read_config()["info_min_screen_width"]
        info_max_width = CH.read_config()["info_max_screen_width"]

        # Bilgi tipindeki ekranlar için
        if type != "menu":
            os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
            def format_text(text, max_width=100, indent=2, line_prefix=ScreenView.colored_text("│ ", info_frame_color)):
                wrapped_lines = textwrap.wrap(text, width=max_width - indent -2)  # Metni belirlenen genişlikte böl
                formatted_lines = []

                for i, line in enumerate(wrapped_lines):
                    if i != 0:
                        if len(line) < max_width - indent:  # Satır kısa ise boşluk ekleyerek tamamla
                            line = ScreenView.colored_text(line.ljust(max_width - indent), info_content_color) + ScreenView.colored_text(" │", info_frame_color)
                        else:
                            line = ScreenView.colored_text(line, info_content_color)+" |"  # Normal satırlar için sonda " |" ekle

                    if i == 0:  # İlk satır hariç diğer satırlara indent (girinti) ekle
                            line = ScreenView.colored_text((" " * indent + line).ljust(max_width - indent), info_content_color) + ScreenView.colored_text(" │", info_frame_color)

                    formatted_lines.append(line_prefix + line)

                return "\n".join(formatted_lines)
            
            if int(info_min_width) <= 50:
                width = 50
            elif len(title) >= int(info_min_width) - 2 and len(title) <= int(info_max_width) - 2:
                width = len(title) + 2
            elif len(title) >= int(info_max_width) - 2:
                width = int(info_max_width)
                title = title[:int(info_max_width) - 5] + "..."
            else:
                width = int(info_min_width)

            # Bu biraz eğreti oldu daha sonra daha iyi bir çözüm bulunabilir (Takvim ekranı için)
            if title == "Takvim":
                width = 22


            horizontal_border = "─" * width

            horizontal_border = ScreenView.colored_text("─" * width, info_frame_color)
            ltc_border  = ScreenView.colored_text("┌", info_frame_color)
            rtc_border  = ScreenView.colored_text("┐", info_frame_color)
            lv_border   = ScreenView.colored_text("│ ", info_frame_color)
            rv_border   = ScreenView.colored_text(" │", info_frame_color)
            lbc_border  = ScreenView.colored_text("└", info_frame_color)
            rbc_border  = ScreenView.colored_text("┘", info_frame_color)
            title_seperator = ScreenView.colored_text(("─"*(width-2)), info_frame_color)
            title_for_print = ScreenView.colored_text(str(title).center(width - 2), info_title_color)

            print(ltc_border+horizontal_border+rtc_border)

            print(lv_border+title_for_print+rv_border)
            print(lv_border+title_seperator+rv_border)

            print(format_text(content, width))

            print(lbc_border+horizontal_border+rbc_border)

            # Bilgi ekranları için Enter'a basılmasını bekleyen kısım
            if type == "info":
                print("Devam etmek için Enter'a basın...")
                while True:
                    char = msvcrt.getch()  # Tek karakter oku
                    if ord(char) == 13:
                        break

            # Bilgi ekranları için kullanıcıdan bir seçim bekleyen kısım
            else: 
                while True:
                    get_user_input = input(type+"\n")
                    if get_user_input:
                        break
                return get_user_input

        # Menü tipindeki ekranlar için
        elif type == "menu":
            num_list = []
            for i, key in enumerate(content, 1):
                if key == "Geri Dön" or key == "Çıkış":
                    num_list.append("0. "+str(key))
                else:
                    num_list.append(str(i)+". "+str(key))

            content_and_title = [title] + num_list
            max_width = max(len(line) for line in content_and_title) + 4

            if max_width < int(menu_min_width):
                width = int(menu_min_width)
            elif int(menu_max_width) > max_width > int(menu_max_width):
                width = int(max_width)
            elif max_width >= int(menu_max_width):
                width = int(menu_max_width)
            else:
                width = int(max_width)

            horizontal_border = ScreenView.colored_text("═" * width, menu_frame_color)
            ltc_border  = ScreenView.colored_text("╔", menu_frame_color)
            rtc_border  = ScreenView.colored_text("╗", menu_frame_color)
            lv_border   = ScreenView.colored_text("║ ", menu_frame_color)
            rv_border   = ScreenView.colored_text(" ║", menu_frame_color)
            lbc_border  = ScreenView.colored_text("╚", menu_frame_color)
            rbc_border  = ScreenView.colored_text("╝", menu_frame_color)
            title_seperator = ScreenView.colored_text(("─"*(width-2)), menu_frame_color)

            if len(title) >= width - 2:
                title = title[:width - 5] + "..."
            title_for_print = ScreenView.colored_text(str(title).center(width - 2), menu_title_color)

            print(ltc_border + horizontal_border + rtc_border) # Üst Çerçeve Yazdır
            
            print(lv_border+title_for_print+rv_border) # Başlık Yazır
            print(lv_border+title_seperator+rv_border) # Seperatör Yazdır

            for line in num_list: # Menü Yazdor
                if len(line) >= width - 2:
                    line = line[:width - 5] + "..."
                line_for_print = ScreenView.colored_text(str(line).ljust(width - 2), menu_content_color)
                print(lv_border+line_for_print+rv_border)
                
            print(lbc_border + horizontal_border + rbc_border) # Alt Çerçeve Yazır

            return input("Seçiminizi yapın: ")
        
        else:
            print("Geçersiz ekran tipi.")
            return None