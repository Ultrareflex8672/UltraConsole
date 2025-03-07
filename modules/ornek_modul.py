from application.ultraconsole import UltraConsole as UC

menu_data = UC.load_json("modules/ornek_harici_menu.cfg")
def ornek_modul(**kwargs):
    if UC.from_main_menu(**kwargs):
        kwargs.update({"menu_data": menu_data})
        kwargs.update({"class_name": "OrnekClass"})
        kwargs.update({"func_name": "go_func"})
        kwargs.update({"init_data": {"parametre": 123}})
        UC.go_custom_menu(0, **kwargs)
    else:
        OrnekClass().go_func(**kwargs)

class OrnekClass(UC):
    def __init__(self, **kwargs):
        self.parametre = kwargs.get("parametre")
        UC.create_frame("Gelen Parametreler", "params: "+str(self.parametre))

    def go_func(self, **kwargs):
        user_data = kwargs.get("user_data")
        isim = user_data[4]  # 4. index isim bilgisi
        if UC.selected_key(1, **kwargs):
            UC.create_frame("Seçim 1", f"Merhaba {isim} Seçenek 1 Seçildi")