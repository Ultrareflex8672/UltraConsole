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
        min_width = CH.read_config()["min_screen_width"]
        title_color = CH.read_config()["menu_title_color"]
        content_color = CH.read_config()["menu_content_color"]
        frame_color = CH.read_config()["menu_frame_color"]
        info_title_color = CH.read_config()["info_title_color"]
        info_content_color = CH.read_config()["info_content_color"]
        info_frame_color = CH.read_config()["info_frame_color"]

        # Bilgi tipindeki ekranlar için
        if type != "menu":
            os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
            def format_text(text, max_width=100, indent=2, line_prefix=ScreenView.colored_text("│ ", info_frame_color)):
                wrapped_lines = textwrap.wrap(text, width=max_width - indent)  # Metni belirlenen genişlikte böl
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

            # content_and_title = [title, content]
            # max_width = max(len(line) for line in content_and_title) + 4
            # if max_width > min_width:
            #     width = max_width
            # else:
            #     width = min_width
            width = int(min_width)
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

            if type == "info":
                print("Devam etmek için Enter'a basın...")
                while True:
                    char = msvcrt.getch()  # Tek karakter oku
                    if ord(char) == 13:  # Enter tuşu ASCII 13'tür (CR - Carriage Return)
                        break
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
            if max_width > int(min_width):
                width = int(max_width)
            else:
                width = int(min_width)

            horizontal_border = ScreenView.colored_text("═" * width, frame_color)
            ltc_border  = ScreenView.colored_text("╔", frame_color)
            rtc_border  = ScreenView.colored_text("╗", frame_color)
            lv_border   = ScreenView.colored_text("║ ", frame_color)
            rv_border   = ScreenView.colored_text(" ║", frame_color)
            lbc_border  = ScreenView.colored_text("╚", frame_color)
            rbc_border  = ScreenView.colored_text("╝", frame_color)
            title_seperator = ScreenView.colored_text(("─"*(width-2)), frame_color)
            title_for_print = ScreenView.colored_text(str(title).center(width - 2), title_color)

            print(ltc_border + horizontal_border + rtc_border) # Üst Çerçeve Yazdır
            
            print(lv_border+title_for_print+rv_border) # Başlık Yazır
            print(lv_border+title_seperator+rv_border) # Seperatör Yazdır

            for line in num_list: # Menü Yazdor
                line_for_print = ScreenView.colored_text(str(line).ljust(width - 2), content_color)
                print(lv_border+line_for_print+rv_border)
                
            print(lbc_border + horizontal_border + rbc_border) # Alt Çerçeve Yazır

            return input("Seçiminizi yapın: ")
        
        else:
            print("Geçersiz ekran tipi.")
            return None