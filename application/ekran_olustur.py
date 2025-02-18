from application.ayar_okuyucu import ConfigHandler as CH
import textwrap

class ScreenView(CH):
    @staticmethod
    def colored_text(text, color_code):
        return f"\033[{color_code}m{text}\033[0m"

    @staticmethod
    def create_frame(title, content, type="info"):
        screen_width = CH.read_config()["min_screen_width"]
        title_color = CH.read_config()["title_color"]
        content_color = CH.read_config()["content_color"]
        frame_color = CH.read_config()["frame_color"]

        # Bilgi tipindeki ekranlar için
        if type == "info":

            content_and_title = [title] + num_list
            max_width = max(len(line) for line in content_and_title) + 4
            if max_width > screen_width:
                width = max_width
            else:
                width = screen_width
            horizontal_border = "─" * width

            print("┌" + horizontal_border + "┐")
            print(f"│ {str(title).center(width - 2)} │")

            for line in num_list:
                print(f"│ {line.ljust(width - 2)} │")
            print("└" + horizontal_border + "┘")

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
            if max_width > int(screen_width):
                width = int(max_width)
            else:
                width = int(screen_width)

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