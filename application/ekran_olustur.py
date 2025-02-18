class ScreenView:
    @staticmethod
    def create_frame(title, content, type="info"):
        if type == "info":
            pass

        elif type == "menu":
            num_list = []
            for i, key in enumerate(content, 1):
                if key == "Geri Dön" or key == "Çıkış":
                    num_list.append("0. "+str(key))
                else:
                    num_list.append(str(i)+". "+str(key))

            content_and_title = [title] + num_list
            width = max(len(line) for line in content_and_title) + 4
            horizontal_border = "─" * width

            print("┌" + horizontal_border + "┐")
            print(f"│ {str(title).center(width - 2)} │")

            for line in num_list:
                print(f"│ {line.ljust(width - 2)} │")
            print("└" + horizontal_border + "┘")

            return input("Seçiminizi yapın: ")
        
        else:
            pass