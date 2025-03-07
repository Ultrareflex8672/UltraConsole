from application.ultraconsole import UltraConsole as UC

class OrnekClass():
    def __init__(self, **kwargs):
        pass
        
    def go_func(self, **kwargs):
        menu_data = UC.load_json("modules/ornek_harici_menu.cfg")
        kwargs.update({"menu_data": menu_data})
        kwargs.update({"module_path": "modules/ornek_modul_alt_fonksiyon"})
        del kwargs["class_name"]
        del kwargs["func_name"]
        del kwargs["init_data"]
        UC.go_custom_menu(1, **kwargs)